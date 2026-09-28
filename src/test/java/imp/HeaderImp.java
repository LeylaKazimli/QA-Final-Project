package imp;

import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import helper.ApiHelper;
import utils.ScenarioContext;

// Header və autentifikasiya məlumatlarının sorğuya əlavə edilməsi
public class HeaderImp {

    private ApiHelper api() {
        return ApiHelper.getInstance();
    }

    // value = "token" → login zamanı saxlanılan "Bearer ..." tokeni (geriyə uyğunluq üçün)
    @Step("Add as a header <key> = <value>")
    public void addHeaderToRequest(String key, String value) {
        if (value.equals("token")) value = ScenarioContext.getString("token");
        api().header(key, value);
    }

    @Step("Header elave et <key> = <value>")
    public void addHeader(String key, String value) {
        addHeaderToRequest(key, value);
    }

    // | key | value | cədvəli
    @Step("Headerleri elave et <table>")
    public void addHeaders(Table table) {
        String keyColumn = table.getColumnNames().get(0);
        String valueColumn = table.getColumnNames().get(1);
        for (TableRow row : table.getTableRows()) {
            addHeaderToRequest(row.getCell(keyColumn), row.getCell(valueColumn));
        }
    }

    @Step("Authorization header-ine tokeni elave et")
    public void addSavedToken() {
        api().header("Authorization", ScenarioContext.getString("token"));
    }

    @Step("Bearer token elave et <token>")
    public void addBearerToken(String token) {
        api().bearerToken(token);
    }

    @Step("Basic auth elave et istifadeci <username> şifre <password>")
    public void addBasicAuth(String username, String password) {
        api().basicAuth(username, password);
    }

    @Step("API key header elave et <headerName> = <apiKey>")
    public void addApiKey(String headerName, String apiKey) {
        api().header(headerName, apiKey);
    }
}