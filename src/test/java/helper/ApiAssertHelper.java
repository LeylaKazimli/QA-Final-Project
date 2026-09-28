package helper;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import io.restassured.module.jsv.JsonSchemaValidator;
import io.restassured.response.Response;
import utils.ScenarioContext;

import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.concurrent.TimeUnit;

import static org.hamcrest.Matchers.lessThan;

// API cavabının yoxlanması. JSON path sintaksisi RestAssured (Groovy GPath) ilədir:
//   "id"   "user.email"   "data[0].name"   "items.size()"   "data.findAll { it.price > 100 }.size()"
// Gözlənilən dəyərlərdə ${dəyişən} əvəzlənməsi işləyir.
public class ApiAssertHelper {

    private static final String SCHEMA_DIR = "src/test/resources/schema";
    private static final String EXPECTED_DIR = "src/test/resources/expected";
    private static final ObjectMapper JSON = new ObjectMapper();

    protected Response response() {
        return ApiHelper.getInstance().getResponse();
    }

    protected Object value(String path) {
        return response().jsonPath().get(path);
    }

    private String describe() {
        String body = response().asString();
        return " | Status: " + response().getStatusCode() + " | Body: " + (body.length() > 500 ? body.substring(0, 500) + "..." : body);
    }

    // ---------- Status ----------

    public void statusCodeIs(int expected) {
        int actual = response().getStatusCode();
        if (actual != expected) throw new AssertionError("Status kodu " + expected + " olmalı idi, faktiki: " + actual + describe());
    }

    public void statusCodeBetween(int from, int to) {
        int actual = response().getStatusCode();
        if (actual < from || actual > to) {
            throw new AssertionError("Status kodu " + from + "-" + to + " aralığında olmalı idi, faktiki: " + actual + describe());
        }
    }

    // ---------- JSON dəyərləri ----------

    // Dəyər tipindən asılı olmayaraq mətn kimi müqayisə edir: 5 == "5", true == "true"
    public void jsonEquals(String path, String expectedValue) {
        String expected = ScenarioContext.resolve(expectedValue);
        Object actual = value(path);
        if (!String.valueOf(actual).equals(expected)) {
            throw new AssertionError("\"" + path + "\" gözlənilən: \"" + expected + "\", faktiki: \"" + actual + "\"");
        }
    }

    public void jsonNotEquals(String path, String unexpectedValue) {
        String unexpected = ScenarioContext.resolve(unexpectedValue);
        Object actual = value(path);
        if (String.valueOf(actual).equals(unexpected)) {
            throw new AssertionError("\"" + path + "\" \"" + unexpected + "\" olmamalı idi");
        }
    }

    public void jsonContains(String path, String text) {
        String expected = ScenarioContext.resolve(text);
        Object actual = value(path);
        boolean ok = actual instanceof Collection
                ? ((Collection<?>) actual).stream().anyMatch(item -> String.valueOf(item).equals(expected))
                : String.valueOf(actual).contains(expected);
        if (!ok) throw new AssertionError("\"" + path + "\" \"" + expected + "\" ehtiva etmir. Faktiki: " + actual);
    }

    public void jsonMatches(String path, String regex) {
        Object actual = value(path);
        if (actual == null || !String.valueOf(actual).matches(regex)) {
            throw new AssertionError("\"" + path + "\" \"" + regex + "\" regex-inə uyğun deyil. Faktiki: " + actual);
        }
    }

    public void jsonNotEmpty(String path) {
        Object actual = value(path);
        boolean empty = actual == null
                || (actual instanceof String && ((String) actual).isBlank())
                || (actual instanceof Collection && ((Collection<?>) actual).isEmpty())
                || (actual instanceof Map && ((Map<?, ?>) actual).isEmpty());
        if (empty) throw new AssertionError("\"" + path + "\" boş olmamalı idi. Faktiki: " + actual + describe());
    }

    public void jsonIsNull(String path) {
        Object actual = value(path);
        if (actual != null) throw new AssertionError("\"" + path + "\" null olmalı idi. Faktiki: " + actual);
    }

    // Açarın varlığını yoxlayır (dəyəri null olsa belə)
    public void jsonHasKey(String path, boolean shouldExist) {
        int dot = path.lastIndexOf('.');
        String parent = dot < 0 ? "$" : path.substring(0, dot);
        String key = path.substring(dot + 1);
        Object container = parent.equals("$") ? response().jsonPath().get() : value(parent);
        boolean exists = container instanceof Map && ((Map<?, ?>) container).containsKey(key);
        if (exists != shouldExist) {
            throw new AssertionError("\"" + path + "\" açarı " + (shouldExist ? "mövcud olmalı idi" : "olmamalı idi"));
        }
    }

    public void jsonIsNumber(String path) {
        Object actual = value(path);
        if (!(actual instanceof Number)) throw new AssertionError("\"" + path + "\" rəqəm deyil. Faktiki: " + actual);
    }

    // string | number | boolean | array | object | null
    public void jsonHasType(String path, String type) {
        Object actual = value(path);
        String actualType = actual == null ? "null"
                : actual instanceof String ? "string"
                : actual instanceof Number ? "number"
                : actual instanceof Boolean ? "boolean"
                : actual instanceof List ? "array"
                : actual instanceof Map ? "object" : actual.getClass().getSimpleName();
        if (!actualType.equalsIgnoreCase(type.trim())) {
            throw new AssertionError("\"" + path + "\" tipi " + type + " olmalı idi, faktiki: " + actualType);
        }
    }

    public void jsonCompare(String path, String operator, String expectedNumber) {
        Object actual = value(path);
        if (!(actual instanceof Number)) throw new AssertionError("\"" + path + "\" rəqəm deyil. Faktiki: " + actual);
        double a = ((Number) actual).doubleValue();
        double e = Double.parseDouble(ScenarioContext.resolve(expectedNumber));
        boolean ok;
        switch (operator.trim()) {
            case ">": ok = a > e; break;
            case ">=": ok = a >= e; break;
            case "<": ok = a < e; break;
            case "<=": ok = a <= e; break;
            case "==": ok = a == e; break;
            case "!=": ok = a != e; break;
            default: throw new IllegalArgumentException("Naməlum operator: " + operator + " (>, >=, <, <=, ==, !=)");
        }
        if (!ok) throw new AssertionError("\"" + path + "\" " + operator + " " + e + " şərtini ödəmir. Faktiki: " + a);
    }

    public void jsonArraySize(String path, int expected) {
        int actual = list(path).size();
        if (actual != expected) throw new AssertionError("\"" + path + "\" elementlərinin sayı " + expected + " olmalı idi, faktiki: " + actual);
    }

    public void jsonArraySizeAtLeast(String path, int minimum) {
        int actual = list(path).size();
        if (actual < minimum) throw new AssertionError("\"" + path + "\" elementlərinin sayı ən azı " + minimum + " olmalı idi, faktiki: " + actual);
    }

    // Məs. "data.status" → bütün elementlərin status-u "completed" olmalıdır (filter testləri üçün)
    public void jsonAllItemsEqual(String path, String expectedValue) {
        String expected = ScenarioContext.resolve(expectedValue);
        List<?> values = list(path);
        if (values.isEmpty()) throw new AssertionError("\"" + path + "\" siyahısı boşdur");
        for (int i = 0; i < values.size(); i++) {
            if (!String.valueOf(values.get(i)).equals(expected)) {
                throw new AssertionError("\"" + path + "\"[" + i + "] = \"" + values.get(i) + "\", gözlənilən: \"" + expected + "\"");
            }
        }
    }

    private List<?> list(String path) {
        Object actual = value(path);
        if (!(actual instanceof List)) throw new AssertionError("\"" + path + "\" massiv deyil. Faktiki: " + actual);
        return (List<?>) actual;
    }

    // ---------- Çoxlu yoxlama / tam body müqayisəsi ----------

    // | path | value | cədvəli — hər sətir üçün dəyər yoxlanılır, bütün uyğunsuzluqlar birlikdə göstərilir.
    // value sütununda matcher-lər də işləyir (aşağıdakı matchesExpected-ə bax).
    public void jsonMatchesTable(Table table) {
        String pathColumn = table.getColumnNames().get(0);
        String valueColumn = table.getColumnNames().get(1);
        List<String> errors = new ArrayList<>();
        for (TableRow row : table.getTableRows()) {
            String path = row.getCell(pathColumn);
            String expected = ScenarioContext.resolve(row.getCell(valueColumn));
            Object actual = value(path);
            JsonNode actualNode = actual == null ? null : JSON.valueToTree(actual);
            String error = matchesExpected(JSON.getNodeFactory().textNode(expected), actualNode, path);
            if (error != null) errors.add(error);
        }
        if (!errors.isEmpty()) throw new AssertionError("Uyğunsuzluqlar:\n  " + String.join("\n  ", errors));
    }

    // expected/ qovluğundakı JSON faylı ilə cavabı müqayisə edir.
    // Faylda olan hər sahə cavabda olmalıdır (cavabdakı əlavə sahələr nəzərə alınmır).
    // Faylda ${dəyişən} və aşağıdakı matcher-lər işlədilə bilər:
    //   "@ignore"  "@notNull"  "@notEmpty"  "@string"  "@number"  "@boolean"  "@array"  "@object"
    //   "@regex:^[a-z]+$"   "@contains:mətn"
    public void jsonMatchesFile(String fileName) {
        Path file = Paths.get(EXPECTED_DIR, fileName);
        if (!Files.exists(file)) throw new IllegalArgumentException("Gözlənilən JSON faylı tapılmadı: " + file.toAbsolutePath());
        JsonNode expected;
        try {
            expected = JSON.readTree(ScenarioContext.resolve(Files.readString(file, StandardCharsets.UTF_8)));
        } catch (IOException e) {
            throw new IllegalStateException("Gözlənilən JSON oxuna bilmədi: " + file, e);
        }
        List<String> errors = new ArrayList<>();
        compare(expected, responseTree(), "$", errors);
        if (!errors.isEmpty()) {
            throw new AssertionError(fileName + " ilə " + errors.size() + " uyğunsuzluq:\n  " + String.join("\n  ", errors));
        }
    }

    // Göndərilən request body-sindəki sahə cavabda eyni dəyərlə qayıtmalıdır (POST/PUT yoxlaması)
    public void jsonEqualsRequestBody(String responsePath, String requestBodyFile, String requestPath) {
        Path file = Paths.get("src/test/resources/body", requestBodyFile);
        try {
            JsonNode request = JSON.readTree(ScenarioContext.resolve(Files.readString(file, StandardCharsets.UTF_8)));
            JsonNode expected = request.at("/" + requestPath.replace(".", "/"));
            if (expected.isMissingNode()) throw new IllegalArgumentException(requestBodyFile + " faylında \"" + requestPath + "\" yoxdur");
            jsonEquals(responsePath, expected.isTextual() ? expected.asText() : expected.toString());
        } catch (IOException e) {
            throw new IllegalStateException("Request body faylı oxuna bilmədi: " + file, e);
        }
    }

    private void compare(JsonNode expected, JsonNode actual, String path, List<String> errors) {
        if (expected.isObject()) {
            if (actual == null || !actual.isObject()) {
                errors.add(path + ": obyekt gözlənilirdi, faktiki: " + actual);
                return;
            }
            Iterator<Map.Entry<String, JsonNode>> fields = expected.fields();
            while (fields.hasNext()) {
                Map.Entry<String, JsonNode> field = fields.next();
                String childPath = path + "." + field.getKey();
                if (!actual.has(field.getKey())) {
                    if (!"@ignore".equals(field.getValue().asText(null))) errors.add(childPath + ": sahə cavabda yoxdur");
                    continue;
                }
                compare(field.getValue(), actual.get(field.getKey()), childPath, errors);
            }
        } else if (expected.isArray()) {
            if (actual == null || !actual.isArray()) {
                errors.add(path + ": massiv gözlənilirdi, faktiki: " + actual);
                return;
            }
            if (expected.size() > actual.size()) {
                errors.add(path + ": ən azı " + expected.size() + " element gözlənilirdi, faktiki: " + actual.size());
                return;
            }
            for (int i = 0; i < expected.size(); i++) compare(expected.get(i), actual.get(i), path + "[" + i + "]", errors);
        } else {
            String error = matchesExpected(expected, actual, path);
            if (error != null) errors.add(error);
        }
    }

    // null qaytarırsa uyğundur, əks halda xəta mətni
    private static String matchesExpected(JsonNode expected, JsonNode actual, String path) {
        String rule = expected.isTextual() ? expected.asText() : null;
        boolean isNull = actual == null || actual.isNull();
        if (rule != null && rule.startsWith("@")) {
            switch (rule) {
                case "@ignore": return null;
                case "@notNull": return isNull ? path + ": null olmamalı idi" : null;
                case "@notEmpty":
                    return isNull || (actual.isTextual() && actual.asText().isBlank()) || (actual.isContainerNode() && actual.size() == 0)
                            ? path + ": boş olmamalı idi, faktiki: " + actual : null;
                case "@string": return !isNull && actual.isTextual() ? null : path + ": string gözlənilirdi, faktiki: " + actual;
                case "@number": return !isNull && actual.isNumber() ? null : path + ": rəqəm gözlənilirdi, faktiki: " + actual;
                case "@boolean": return !isNull && actual.isBoolean() ? null : path + ": boolean gözlənilirdi, faktiki: " + actual;
                case "@array": return !isNull && actual.isArray() ? null : path + ": massiv gözlənilirdi, faktiki: " + actual;
                case "@object": return !isNull && actual.isObject() ? null : path + ": obyekt gözlənilirdi, faktiki: " + actual;
                default:
                    if (rule.startsWith("@regex:")) {
                        String regex = rule.substring(7);
                        return !isNull && text(actual).matches(regex) ? null : path + ": \"" + regex + "\" regex-inə uyğun deyil, faktiki: " + actual;
                    }
                    if (rule.startsWith("@contains:")) {
                        String part = rule.substring(10);
                        return !isNull && text(actual).contains(part) ? null : path + ": \"" + part + "\" ehtiva etmir, faktiki: " + actual;
                    }
            }
        }
        String expectedText = expected.isNull() ? "null" : text(expected);
        String actualText = isNull ? "null" : text(actual);
        return expectedText.equals(actualText) ? null : path + ": gözlənilən \"" + expectedText + "\", faktiki \"" + actualText + "\"";
    }

    private static String text(JsonNode node) {
        return node.isValueNode() ? node.asText() : node.toString();
    }

    private JsonNode responseTree() {
        try {
            return JSON.readTree(response().asString());
        } catch (IOException e) {
            throw new AssertionError("Cavab etibarlı JSON deyil: " + response().asString());
        }
    }

    // ---------- Siyahı xüsusiyyətləri ----------

    // Sıralama testləri: ?sort=price&order=asc
    @SuppressWarnings({"unchecked", "rawtypes"})
    public void jsonListSorted(String path, boolean ascending) {
        List<?> values = list(path);
        for (int i = 1; i < values.size(); i++) {
            Comparable prev = comparable(values.get(i - 1));
            Comparable curr = comparable(values.get(i));
            int cmp = prev.compareTo(curr);
            if (ascending ? cmp > 0 : cmp < 0) {
                throw new AssertionError("\"" + path + "\" " + (ascending ? "artan" : "azalan") + " sırada deyil: ["
                        + (i - 1) + "]=" + values.get(i - 1) + ", [" + i + "]=" + values.get(i));
            }
        }
    }

    private static Comparable<?> comparable(Object value) {
        if (value instanceof Number) return ((Number) value).doubleValue();
        return String.valueOf(value);
    }

    public void jsonListUnique(String path) {
        List<?> values = list(path);
        if (new HashSet<>(values).size() != values.size()) {
            throw new AssertionError("\"" + path + "\" siyahısında təkrarlanan dəyərlər var: " + values);
        }
    }

    // ---------- Body / header / vaxt / schema ----------

    public void bodyContains(String text) {
        String expected = ScenarioContext.resolve(text);
        if (!response().asString().contains(expected)) throw new AssertionError("Cavab \"" + expected + "\" ehtiva etmir" + describe());
    }

    public void headerExists(String name) {
        if (response().getHeader(name) == null) throw new AssertionError("\"" + name + "\" header-i cavabda yoxdur");
    }

    public void headerContains(String name, String text) {
        String actual = response().getHeader(name);
        String expected = ScenarioContext.resolve(text);
        if (actual == null || !actual.contains(expected)) {
            throw new AssertionError("\"" + name + "\" header-i \"" + expected + "\" ehtiva etmir. Faktiki: " + actual);
        }
    }

    public void responseTimeLessThan(long maxMillis) {
        response().then().time(lessThan(maxMillis), TimeUnit.MILLISECONDS);
    }

    // schema/ qovluğundakı JSON Schema faylı ilə bütün cavab strukturunu yoxlayır
    public void matchesSchema(String schemaFile) {
        File file = new File(SCHEMA_DIR, schemaFile);
        if (!file.exists()) throw new IllegalArgumentException("Schema faylı tapılmadı: " + file.getAbsolutePath());
        response().then().assertThat().body(JsonSchemaValidator.matchesJsonSchema(file));
    }

    // ---------- Dəyərləri saxlamaq ----------

    public void saveJsonValue(String path, String variableName, boolean suiteScope) {
        Object actual = value(path);
        if (actual == null) throw new AssertionError("\"" + path + "\" cavabda tapılmadı, saxlanıla bilmədi");
        if (suiteScope) ScenarioContext.putSuite(variableName, String.valueOf(actual));
        else ScenarioContext.put(variableName, String.valueOf(actual));
        System.out.println(variableName + " = " + actual);
    }

    public void saveHeaderValue(String headerName, String variableName) {
        String actual = response().getHeader(headerName);
        if (actual == null) throw new AssertionError("\"" + headerName + "\" header-i cavabda yoxdur");
        ScenarioContext.put(variableName, actual);
    }

    public void jsonEqualsSaved(String path, String variableName, boolean shouldEqual) {
        String saved = ScenarioContext.getString(variableName);
        String actual = String.valueOf(value(path));
        if (saved.equals(actual) != shouldEqual) {
            throw new AssertionError("\"" + path + "\" (" + actual + ") " + variableName + " (" + saved + ") ilə "
                    + (shouldEqual ? "eyni olmalı idi" : "fərqli olmalı idi"));
        }
    }
}
