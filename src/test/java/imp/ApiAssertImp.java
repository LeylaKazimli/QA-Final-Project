package imp;

import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.Table;
import helper.ApiAssertHelper;

// API cavabının yoxlanması və cavabdan dəyər saxlanması
public class ApiAssertImp extends ApiAssertHelper {

    // ---------- Status ----------

    @Step("Status kodunun <statusCode> olmalıdır")
    public void validateStatusCode(int statusCode) {
        statusCodeIs(statusCode);
    }

    @Step("Status kodu <from> ile <to> arasında olmalıdır")
    public void validateStatusCodeRange(int from, int to) {
        statusCodeBetween(from, to);
    }

    // ---------- Dəyər müqayisəsi ----------

    @Step("Json cavabında <key> deyeri <expectedValue> beraberdir")
    public void jsonKeyEqualsString(String key, String expectedValue) {
        jsonEquals(key, expectedValue);
    }

    @Step("Json cavabında <key> deyeri integer <expectedValue> beraberdir")
    public void jsonKeyEqualsInteger(String key, String expectedValue) {
        jsonCompare(key, "==", expectedValue);
    }

    @Step("Json cavabında <key> deyeri <value> olmamalıdır")
    public void jsonKeyNotEquals(String key, String value) {
        jsonNotEquals(key, value);
    }

    @Step("Json cavabında <key> deyerinde <text> olmalıdır")
    public void jsonKeyContains(String key, String text) {
        jsonContains(key, text);
    }

    @Step("Json cavabında <key> deyeri <regex> regex-ine uyğun olmalıdır")
    public void jsonKeyMatches(String key, String regex) {
        jsonMatches(key, regex);
    }

    // operator: >  >=  <  <=  ==  !=
    @Step("Json cavabında <key> deyeri <operator> <number> olmalıdır")
    public void jsonKeyCompare(String key, String operator, String number) {
        jsonCompare(key, operator, number);
    }

    // ---------- Mövcudluq / tip ----------

    @Step("Json cavabında <key> deyeri boş olmamalıdır")
    public void jsonKeyShouldNotBeEmpty(String key) {
        jsonNotEmpty(key);
    }

    @Step("Json cavabında <key> deyeri null olmalıdır")
    public void jsonKeyShouldBeNull(String key) {
        jsonIsNull(key);
    }

    @Step("Json cavabında <key> açarı mövcud olmalıdır")
    public void jsonKeyShouldExist(String key) {
        jsonHasKey(key, true);
    }

    @Step("Json cavabında <key> açarı olmamalıdır")
    public void jsonKeyShouldNotExist(String key) {
        jsonHasKey(key, false);
    }

    @Step("Json cavabında verilen <key> deyeri ededdir")
    public void jsonValueInNumber(String key) {
        jsonIsNumber(key);
    }

    // type: string | number | boolean | array | object | null
    @Step("Json cavabında <key> deyerinin tipi <type> olmalıdır")
    public void jsonKeyType(String key, String type) {
        jsonHasType(key, type);
    }

    // ---------- Massivlər ----------

    @Step("Json cavabında <key> massivinin ölçüsü <size> olmalıdır")
    public void jsonArraySizeIs(String key, int size) {
        jsonArraySize(key, size);
    }

    @Step("Json cavabında <key> massivinin ölçüsü en az <size> olmalıdır")
    public void jsonArraySizeMin(String key, int size) {
        jsonArraySizeAtLeast(key, size);
    }

    @Step("Json cavabında <key> siyahısındakı bütün deyerler <value> olmalıdır")
    public void jsonAllValues(String key, String value) {
        jsonAllItemsEqual(key, value);
    }

    // ---------- Tam body yoxlaması ----------

    // | path | value | cədvəli; value-da matcher-lər: @notNull @number @string @regex:... @contains:...
    @Step("Json cavabını cedvel ile yoxla <table>")
    public void jsonTable(Table table) {
        jsonMatchesTable(table);
    }

    // src/test/resources/expected/<fayl> ilə müqayisə (faylda olan hər sahə cavabda olmalıdır)
    @Step("Json cavabı <fileName> faylındakı gözlenilen JSON-a uyğun olmalıdır")
    public void jsonFile(String fileName) {
        jsonMatchesFile(fileName);
    }

    @Step("Json cavabında <responsePath> deyeri <bodyFile> request body-sindeki <requestPath> ile eyni olmalıdır")
    public void jsonEqualsRequest(String responsePath, String bodyFile, String requestPath) {
        jsonEqualsRequestBody(responsePath, bodyFile, requestPath);
    }

    @Step("Json cavabında <key> siyahısı artan sırada olmalıdır")
    public void listAscending(String key) {
        jsonListSorted(key, true);
    }

    @Step("Json cavabında <key> siyahısı azalan sırada olmalıdır")
    public void listDescending(String key) {
        jsonListSorted(key, false);
    }

    @Step("Json cavabında <key> siyahısındakı deyerler unikal olmalıdır")
    public void listUnique(String key) {
        jsonListUnique(key);
    }

    // ---------- Body / header / vaxt / schema ----------

    @Step("Cavab body-sinde <text> olmalıdır")
    public void responseBodyContains(String text) {
        bodyContains(text);
    }

    @Step("Header <headerKey> movcud olmalıdır")
    public void headerShouldExist(String headerKey) {
        headerExists(headerKey);
    }

    @Step("Header <headerKey> deyerinde <text> olmalıdır")
    public void headerShouldContain(String headerKey, String text) {
        headerContains(headerKey, text);
    }

    @Step("Respons cavab müddeti <maxMillis> milliSaniyeden az olmalıdır")
    public void responseTimeLessThanMilliSecond(String maxMillis) {
        responseTimeLessThan(Long.parseLong(maxMillis));
    }

    @Step("Cavab <schemaFile> JSON schema-sına uyğun olmalıdır")
    public void responseMatchesSchema(String schemaFile) {
        matchesSchema(schemaFile);
    }

    // ---------- Dəyər saxlamaq və müqayisə ----------

    @Step({"Save value of <key> as <variableName>", "Json cavabında <key> deyerini <variableName> olaraq yadda saxla"})
    public void saveValueAs(String key, String variableName) {
        saveJsonValue(key, variableName, false);
    }

    @Step("Json cavabında <key> deyerini <variableName> olaraq bütün testler üçün yadda saxla")
    public void saveValueForSuite(String key, String variableName) {
        saveJsonValue(key, variableName, true);
    }

    @Step("Header <headerKey> deyerini <variableName> olaraq yadda saxla")
    public void saveHeader(String headerKey, String variableName) {
        saveHeaderValue(headerKey, variableName);
    }

    @Step("Json cavabında <key> deyeri <savedKey> ile ferqlidir")
    public void jsonValueIsDifferentFromSaved(String key, String savedKey) {
        jsonEqualsSaved(key, savedKey, false);
    }

    @Step("Json cavabında <key> deyeri <savedKey> ile eynidir")
    public void jsonValueIsSameAsSaved(String key, String savedKey) {
        jsonEqualsSaved(key, savedKey, true);
    }
}