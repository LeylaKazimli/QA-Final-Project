package helper;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.thoughtworks.gauge.Gauge;
import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import io.restassured.RestAssured;
import io.restassured.config.EncoderConfig;
import io.restassured.config.HttpClientConfig;
import io.restassured.config.RestAssuredConfig;
import io.restassured.http.ContentType;
import io.restassured.http.Method;
import io.restassured.response.Response;
import io.restassured.specification.RequestSpecification;
import utils.Config;
import utils.ScenarioContext;

import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.LinkedHashMap;
import java.util.Map;

// API sorğusunun qurulması, göndərilməsi və cavabın saxlanması.
//
// Hər ssenarinin öz ApiHelper obyekti var (ThreadLocal + Hooks-da təmizlənir) —
// əvvəlki ssenarinin header/body/response-u növbətiyə keçmir, parallel icra təhlükəsizdir.
// Bütün parametrlərdə ${dəyişən} əvəzlənməsi işləyir.
public class ApiHelper {

    private static final ThreadLocal<ApiHelper> CURRENT = ThreadLocal.withInitial(ApiHelper::new);
    private static final String BODY_DIR = "src/test/resources/body";
    private static final String FILES_DIR = "src/test/resources/files";
    private static final ObjectMapper JSON = new ObjectMapper();

    private String baseUrl = Config.apiBaseUrl();
    private RequestSpecification request;
    private String endpoint = "";
    private Response response;

    private ApiHelper() {
    }

    public static ApiHelper getInstance() {
        return CURRENT.get();
    }

    // Hooks tərəfindən hər ssenaridən əvvəl çağırılır
    public static void clear() {
        CURRENT.remove();
    }

    public RequestSpecification getRequestSpecification() {
        if (request == null) resetRequestSpecification();
        return request;
    }

    public void resetRequestSpecification() {
        // UTF-8: form/JSON body-lərində Azərbaycan hərfləri (ə, ş, ı) düzgün getsin (RestAssured default-u ISO-8859-1-dir)
        // Timeout: server cavab verməsə test sonsuz gözləmir
        int timeoutMillis = Config.apiTimeoutSeconds() * 1000;
        request = RestAssured.given().config(RestAssuredConfig.config()
                .encoderConfig(EncoderConfig.encoderConfig().defaultContentCharset(StandardCharsets.UTF_8.name()))
                .httpClient(HttpClientConfig.httpClientConfig()
                        .setParam("http.connection.timeout", timeoutMillis)
                        .setParam("http.socket.timeout", timeoutMillis)));
        if (Config.apiRelaxedHttps()) request.relaxedHTTPSValidation();
        if (Config.apiLogAll()) request.log().all();
        endpoint = "";
    }

    public void setBaseUrl(String url) {
        this.baseUrl = ScenarioContext.resolve(url);
    }

    public String getBaseUrl() {
        return baseUrl;
    }

    // ---------- Sorğunun qurulması ----------

    // "/users/{id}?page=1" — path parametri və query string dəstəklənir
    public void addEndpoint(String endpoint) {
        this.endpoint = ScenarioContext.resolve(endpoint);
    }

    public void header(String key, String value) {
        getRequestSpecification().header(key, ScenarioContext.resolve(value));
    }

    public void bearerToken(String token) {
        String value = ScenarioContext.resolve(token);
        header("Authorization", value.startsWith("Bearer ") ? value : "Bearer " + value);
    }

    public void basicAuth(String username, String password) {
        getRequestSpecification().auth().preemptive()
                .basic(ScenarioContext.resolve(username), ScenarioContext.resolve(password));
    }

    public void queryParam(String key, String value) {
        getRequestSpecification().queryParam(key, ScenarioContext.resolve(value));
    }

    public void pathParam(String key, String value) {
        getRequestSpecification().pathParam(key, ScenarioContext.resolve(value));
    }

    public void formParam(String key, String value) {
        getRequestSpecification().contentType(ContentType.URLENC).formParam(key, ScenarioContext.resolve(value));
    }

    public void multiPartFile(String fieldName, String fileName) {
        File file = Paths.get(FILES_DIR, fileName).toFile();
        if (!file.exists()) throw new IllegalArgumentException("Fayl tapılmadı: " + file.getAbsolutePath());
        getRequestSpecification().multiPart(fieldName, file);
    }

    public void addBodyAsJson(String jsonBody) {
        getRequestSpecification().contentType(ContentType.JSON).body(ScenarioContext.resolve(jsonBody));
    }

    // body/ qovluğundakı fayl şablon kimi oxunur: içindəki ${dəyişən}-lər əvəzlənir
    public void addBodyFromFile(String fileName) {
        Path file = Paths.get(BODY_DIR, fileName);
        if (!Files.exists(file)) throw new IllegalArgumentException("Body faylı tapılmadı: " + file.toAbsolutePath());
        String content;
        try {
            content = Files.readString(file, StandardCharsets.UTF_8);
        } catch (IOException e) {
            throw new IllegalStateException("Body faylı oxuna bilmədi: " + file, e);
        }
        String name = fileName.toLowerCase();
        ContentType type = name.endsWith(".json") ? ContentType.JSON : name.endsWith(".xml") ? ContentType.XML : ContentType.TEXT;
        getRequestSpecification().contentType(type).body(ScenarioContext.resolve(content));
    }

    // | key | value | cədvəlindən JSON body qurur. "address.city" kimi açarlar iç-içə obyekt yaradır.
    // Dəyərlər avtomatik tip alır: 12 → rəqəm, true/false → boolean, null → null, qalanı → string.
    public void addBodyFromTable(Table table) {
        Map<String, Object> body = new LinkedHashMap<>();
        String keyColumn = table.getColumnNames().get(0);
        String valueColumn = table.getColumnNames().get(1);
        for (TableRow row : table.getTableRows()) {
            putNested(body, row.getCell(keyColumn), typed(ScenarioContext.resolve(row.getCell(valueColumn))));
        }
        try {
            getRequestSpecification().contentType(ContentType.JSON).body(JSON.writeValueAsString(body));
        } catch (JsonProcessingException e) {
            throw new IllegalStateException("Cədvəldən JSON qurula bilmədi", e);
        }
    }

    @SuppressWarnings("unchecked")
    private static void putNested(Map<String, Object> root, String dottedKey, Object value) {
        String[] parts = dottedKey.split("\\.");
        Map<String, Object> current = root;
        for (int i = 0; i < parts.length - 1; i++) {
            current = (Map<String, Object>) current.computeIfAbsent(parts[i], k -> new LinkedHashMap<String, Object>());
        }
        current.put(parts[parts.length - 1], value);
    }

    private static Object typed(String value) {
        if (value.equals("null")) return null;
        if (value.equals("true") || value.equals("false")) return Boolean.parseBoolean(value);
        if (value.matches("-?\\d{1,18}")) return Long.parseLong(value);
        if (value.matches("-?\\d+\\.\\d+")) return Double.parseDouble(value);
        return value;
    }

    // ---------- Göndərmə ----------

    public Response send(String method) {
        return send(method, endpoint);
    }

    // 429 (Too Many Requests) və 503 cavablarında Retry-After / eksponensial gözləmə ilə təkrar cəhd edir
    public Response send(String method, String urlOrPath) {
        Method httpMethod = Method.valueOf(method.trim().toUpperCase());
        String url = Config.resolveUrl(baseUrl, ScenarioContext.resolve(urlOrPath));
        RequestSpecification spec = getRequestSpecification();

        Response result = spec.request(httpMethod, url);
        for (int attempt = 1; attempt <= Config.apiMaxRetries() && isRetryable(result); attempt++) {
            long waitMillis = retryDelayMillis(result, attempt);
            System.out.println(result.getStatusCode() + " alındı, " + waitMillis + " ms sonra təkrar cəhd (" + attempt + ")");
            sleep(waitMillis);
            result = spec.request(httpMethod, url);
        }
        response = result;
        report(httpMethod, url, result);
        return result;
    }

    public Response getResponse() {
        if (response == null) throw new IllegalStateException("Hələ heç bir API sorğusu göndərilməyib");
        return response;
    }

    private static boolean isRetryable(Response response) {
        return response.getStatusCode() == 429 || response.getStatusCode() == 503;
    }

    private static long retryDelayMillis(Response response, int attempt) {
        long maxMillis = Config.apiRetryMaxWaitSeconds() * 1000L;
        String retryAfter = response.getHeader("Retry-After");
        if (retryAfter != null && retryAfter.matches("\\d+")) return Math.min(Long.parseLong(retryAfter) * 1000L, maxMillis);
        return Math.min(1000L * (1L << (attempt - 1)), maxMillis);
    }

    private static void sleep(long millis) {
        try {
            Thread.sleep(millis);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }

    // Sorğu/cavab xülasəsini Gauge HTML hesabatına yazır
    private static void report(Method method, String url, Response response) {
        String body = response.asString();
        if (body.length() > 3000) body = body.substring(0, 3000) + "... (" + body.length() + " simvol)";
        Gauge.writeMessage(method + " " + url + " → " + response.getStatusCode() + " (" + response.getTime() + " ms)");
        Gauge.writeMessage("Response: " + body);
        System.out.println(method + " " + url + " → " + response.getStatusCode() + " (" + response.getTime() + " ms)");
        System.out.println("Response Body: " + body);
    }
}
