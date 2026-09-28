package helper;

import io.restassured.response.Response;
import utils.ScenarioContext;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

// Login və token idarəsi.
// Token bütün suite üçün keşlənir: 50 ssenari = 1 login sorğusu. Bu həm testləri sürətləndirir,
// həm də API-nin rate limit-inə (429 Too Many Requests) düşməyin qarşısını alır.
// Alınan token ssenari dəyişəni kimi saxlanılır: ${token} = "Bearer ...", ${rawToken} = "...".
public class AuthHelper {

    private static final Map<String, String> TOKEN_CACHE = new ConcurrentHashMap<>();

    public void login(String endpoint, String bodyFile, String tokenPath, boolean useCache) {
        ApiHelper api = ApiHelper.getInstance();
        String cacheKey = api.getBaseUrl() + "|" + endpoint + "|" + bodyFile + "|" + tokenPath;

        String token = useCache ? TOKEN_CACHE.get(cacheKey) : null;
        if (token == null) {
            api.resetRequestSpecification();
            api.addBodyFromFile(bodyFile);
            Response response = api.send("POST", endpoint);
            if (response.getStatusCode() >= 300) {
                throw new AssertionError("Login uğursuz oldu: " + response.getStatusCode() + " " + response.asString());
            }
            token = response.jsonPath().getString(tokenPath);
            if (token == null || token.isBlank()) {
                throw new AssertionError("Login cavabında \"" + tokenPath + "\" tapılmadı: " + response.asString());
            }
            if (useCache) TOKEN_CACHE.put(cacheKey, token);
        }

        ScenarioContext.put("rawToken", token);
        ScenarioContext.put("token", "Bearer " + token);
        // Login-dən sonra ssenari təmiz sorğu ilə davam edir
        api.resetRequestSpecification();
    }

    // Logout / token ləğvi testlərindən sonra növbəti login yenidən real sorğu göndərsin
    public static void clearCache() {
        TOKEN_CACHE.clear();
    }
}