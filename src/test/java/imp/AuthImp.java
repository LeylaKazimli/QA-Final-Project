package imp;

import com.thoughtworks.gauge.Step;
import helper.ApiHelper;
import helper.AuthHelper;
import io.restassured.response.Response;
import utils.ScenarioContext;

// Login step-ləri. Uğurlu login-dən sonra ${token} ("Bearer ...") və ${rawToken} dəyişənləri yaranır.
// Nümunə (concept faylında):
//   * "/auth/login" ünvanına "login.json" ile login ol ve "token" tokenini yadda saxla
//   * Authorization header-ine tokeni elave et
public class AuthImp extends AuthHelper {

    // Token suite boyu keşlənir — hər ssenaridə təkrar login sorğusu getmir
    @Step("<endpoint> ünvanına <bodyFile> ile login ol ve <tokenPath> tokenini yadda saxla")
    public void loginCached(String endpoint, String bodyFile, String tokenPath) {
        login(endpoint, bodyFile, tokenPath, true);
    }

    // Keşsiz, həmişə yeni sessiya (logout, token ləğvi, çox istifadəçili testlər üçün)
    @Step("<endpoint> ünvanına <bodyFile> ile yeni sessiya açaraq login ol ve <tokenPath> tokenini yadda saxla")
    public void loginFresh(String endpoint, String bodyFile, String tokenPath) {
        login(endpoint, bodyFile, tokenPath, false);
    }

    @Step("Token keşini temizle")
    public void clearTokenCache() {
        clearCache();
    }

    // Geriyə uyğunluq: son göndərilən sorğunun cavabından "token" və ya "accessToken" götürür
    @Step("Login cavabından accesTokeni yadda saxla <response>")
    public void savedToken(Object responseObj) {
        Response response = ApiHelper.getInstance().getResponse();
        String token = response.jsonPath().getString("token");
        if (token == null) token = response.jsonPath().getString("accessToken");
        if (token == null) throw new AssertionError("Cavabda token/accessToken tapılmadı: " + response.asString());
        ScenarioContext.put("rawToken", token);
        ScenarioContext.put("token", "Bearer " + token);
    }
}