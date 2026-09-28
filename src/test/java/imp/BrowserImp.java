package imp;

import com.thoughtworks.gauge.Gauge;
import com.thoughtworks.gauge.Step;
import helper.BrowserHelper;
import utils.Config;

// Brauzer, naviqasiya, tab, iframe, alert, cookie və storage step-ləri
public class BrowserImp extends BrowserHelper {

    // ---------- Açmaq / bağlamaq / naviqasiya ----------

    @Step("<browserType> brauzeri aç ve keçid et <url>")
    public void openBrowserWithType(String browserType, String url) {
        openBrowser(browserType, url);
    }

    @Step("Brauzeri aç ve keçid et <url>")
    public void openDefaultBrowser(String url) {
        openBrowser(Config.browser(), url);
    }

    @Step("Brauzeri bağla")
    public void closeBrowserStep() {
        closeBrowser();
    }

    @Step("<url> adresine keçid et")
    public void navigateTo(String url) {
        navigate(url);
    }

    @Step("Sehifeni yenile")
    public void refreshPage() {
        refresh();
    }

    @Step("Evvelki sehifeye qayıt")
    public void goBack() {
        back();
    }

    @Step("Növbeti sehifeye keç")
    public void goForward() {
        forward();
    }

    @Step("Pencere ölçüsünü <width> x <height> et")
    public void setWindowSize(int width, int height) {
        resizeWindow(width, height);
    }

    // ---------- URL / başlıq ----------

    @Step("Sehife başlığı <title> olmalıdır")
    public void titleShouldBe(String title) {
        verifyTitleEquals(title);
    }

    @Step("Sehife başlığında <text> olmalıdır")
    public void titleShouldContain(String text) {
        verifyTitleContains(text);
    }

    @Step("URL <text> içermelidir")
    public void urlShouldContain(String text) {
        verifyUrlContains(text);
    }

    @Step("URL <url> olmalıdır")
    public void urlShouldBe(String url) {
        verifyUrlEquals(url);
    }

    // ---------- Tab / pəncərə ----------

    @Step("Yeni açılan taba keç")
    public void switchToNewTab() {
        switchToNewestWindow();
    }

    @Step("<index> nömreli taba keç")
    public void switchToTab(int index) {
        switchToWindow(index);
    }

    @Step("Cari tabı bağla ve esas taba qayıt")
    public void closeTab() {
        closeCurrentWindowAndReturn();
    }

    @Step("Yeni tabda <url> aç")
    public void openUrlInNewTab(String url) {
        openNewTab(url);
    }

    // ---------- iframe ----------

    @Step("<element> iframe-ine keç")
    public void enterFrame(String element) {
        switchToFrame(element);
    }

    @Step("Iframe-den esas sehifeye qayıt")
    public void leaveFrame() {
        switchToMainContent();
    }

    // ---------- Alert ----------

    @Step("Alert-i qebul et")
    public void acceptAlertStep() {
        acceptAlert();
    }

    @Step("Alert-i legv et")
    public void dismissAlertStep() {
        dismissAlert();
    }

    @Step("Alert metninde <text> olmalıdır")
    public void alertShouldContain(String text) {
        verifyAlertText(text);
    }

    @Step("Alert-e <text> yaz ve qebul et")
    public void typeIntoAlert(String text) {
        typeIntoAlertAndAccept(text);
    }

    // ---------- Cookie / storage / JS ----------

    @Step("Cookie elave et <name> = <value>")
    public void addCookieStep(String name, String value) {
        addCookie(name, value);
    }

    @Step("Bütün cookie-leri sil")
    public void deleteCookies() {
        deleteAllCookies();
    }

    @Step("<name> cookie-si mövcud olmalıdır")
    public void cookieShouldExist(String name) {
        verifyCookieExists(name);
    }

    @Step("LocalStorage-e yaz <key> = <value>")
    public void localStorageSet(String key, String value) {
        setLocalStorage(key, value);
    }

    @Step("LocalStorage ve SessionStorage-i temizle")
    public void clearStorages() {
        clearStorage();
    }

    @Step("JavaScript icra et <script>")
    public void runScript(String script) {
        executeScript(script);
    }

    // ---------- Digər ----------

    @Step("Ekran görüntüsü çek")
    public void takeScreenshot() {
        Gauge.captureScreenshot();
    }

    // Yalnız son çarə kimi — mümkün olduqda "görsensin deye ... gözle" step-lərini işlədin
    @Step("<seconds> saniye gözle")
    public void waitSeconds(int seconds) {
        hardWait(seconds);
    }
}