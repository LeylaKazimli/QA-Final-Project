package imp;

import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.Table;
import helper.ApiHelper;

// API sorğusunun qurulması və göndərilməsi.
// Bütün parametrlərdə ${dəyişən} işləyir: "/users/${userId}", "{\"email\":\"${random.email}\"}"
public class ApiRequestImp {

    private ApiHelper api() {
        return ApiHelper.getInstance();
    }

    // ---------- Hazırlıq ----------

    @Step({"Set base Url to <url>", "API base URL <url> olsun"})
    public void setBaseUrl(String url) {
        api().setBaseUrl(url);
    }

    @Step({"Initalize request specification", "Yeni API sorğusu hazırla"})
    public void initalizeRequestSpecification() {
        api().resetRequestSpecification();
    }

    @Step({"Add Endpoint <endpoint>", "Endpoint <endpoint> olsun"})
    public void addEndpoint(String endpoint) {
        api().addEndpoint(endpoint);
    }

    @Step("Query parametri elave et <key> = <value>")
    public void addQueryParam(String key, String value) {
        api().queryParam(key, value);
    }

    @Step("Path parametri elave et <key> = <value>")
    public void addPathParam(String key, String value) {
        api().pathParam(key, value);
    }

    @Step("Form parametri elave et <key> = <value>")
    public void addFormParam(String key, String value) {
        api().formParam(key, value);
    }

    @Step("Multipart fayl elave et <field> = <fileName>")
    public void addMultipartFile(String field, String fileName) {
        api().multiPartFile(field, fileName);
    }

    // ---------- Body ----------

    @Step({"Add body as file resource <fileName>", "Body olaraq <fileName> faylını elave et"})
    public void addBodyFromResource(String fileName) {
        api().addBodyFromFile(fileName);
    }

    @Step({"Add body as text <jsonBody>", "Body olaraq <jsonBody> metnini elave et"})
    public void addBodyAsText(String jsonBody) {
        api().addBodyAsJson(jsonBody);
    }

    @Step("Body-ni cedvelden qur <table>")
    public void addBodyFromTable(Table table) {
        api().addBodyFromTable(table);
    }

    // ---------- Göndərmə ----------

    // Əvvəlki sorğunun header/body-si olmadan birbaşa GET göndərir
    @Step("API e GET request gönder <url>")
    public void sendGetRequest(String url) {
        api().resetRequestSpecification();
        api().send("GET", url);
    }

    @Step("<method> sorğusu gönder")
    public void sendRequest(String method) {
        api().send(method);
    }

    @Step("<method> sorğusu gönder <endpoint>")
    public void sendRequestTo(String method, String endpoint) {
        api().addEndpoint(endpoint);
        api().send(method);
    }

    @Step("Get request and display respons")
    public void getRequestandDisplay() {
        api().send("GET");
    }

    @Step("Post request and display respons")
    public void sendPostRequestandDisplayResponse() {
        api().send("POST");
    }

    @Step("Put request and display respons")
    public void sendPutRequestandDisplayResponse() {
        api().send("PUT");
    }

    @Step("Patch request and display respons")
    public void sendPatchRequestandDisplayResponse() {
        api().send("PATCH");
    }

    @Step("Delete request and display response")
    public void sendDeleteRequestandDisplayResponse() {
        api().send("DELETE");
    }

    @Step("Cavabı çap et")
    public void printResponse() {
        api().getResponse().prettyPrint();
    }
}
