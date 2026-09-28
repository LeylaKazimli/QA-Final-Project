package helper;

import org.openqa.selenium.Alert;
import org.openqa.selenium.Cookie;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.WindowType;
import org.openqa.selenium.support.ui.ExpectedConditions;
import utils.Config;
import utils.DriverManager;
import utils.WebDriverFactory;

import java.util.ArrayList;
import java.util.List;

// Brauzer səviyyəli əməliyyatlar: açmaq, naviqasiya, tab/pəncərə, iframe, alert, cookie, storage, JS
public class BrowserHelper extends BaseHelper {

    public void openBrowser(String browserType, String url) {
        if (!DriverManager.hasDriver()) {
            DriverManager.setDriver(WebDriverFactory.create(browserType));
        }
        navigate(url);
    }

    // Nisbi ünvan ("/login") env-dəki ui_base_url-ə birləşdirilir
    public void navigate(String url) {
        driver().get(Config.resolveUrl(Config.uiBaseUrl(), resolve(url)));
    }

    public void closeBrowser() {
        DriverManager.quitDriver();
    }

    public void refresh() {
        driver().navigate().refresh();
    }

    public void back() {
        driver().navigate().back();
    }

    public void forward() {
        driver().navigate().forward();
    }

    public void resizeWindow(int width, int height) {
        driver().manage().window().setSize(new Dimension(width, height));
    }

    // ---------- URL / başlıq yoxlamaları ----------

    public void verifyTitleEquals(String title) {
        String expected = resolve(title);
        assertEventually(() -> expected.equals(driver().getTitle()),
                () -> "Səhifə başlığı gözlənilən: \"" + expected + "\", faktiki: \"" + driver().getTitle() + "\"");
    }

    public void verifyTitleContains(String text) {
        String expected = resolve(text);
        assertEventually(() -> driver().getTitle().contains(expected),
                () -> "Səhifə başlığı \"" + expected + "\" ehtiva etmir. Faktiki: \"" + driver().getTitle() + "\"");
    }

    public void verifyUrlContains(String text) {
        String expected = resolve(text);
        assertEventually(() -> driver().getCurrentUrl().contains(expected),
                () -> "URL \"" + expected + "\" ehtiva etmir. Faktiki: " + driver().getCurrentUrl());
    }

    public void verifyUrlEquals(String url) {
        String expected = Config.resolveUrl(Config.uiBaseUrl(), resolve(url));
        assertEventually(() -> driver().getCurrentUrl().equals(expected),
                () -> "URL gözlənilən: " + expected + ", faktiki: " + driver().getCurrentUrl());
    }

    // ---------- Tab / pəncərə ----------

    public void switchToNewestWindow() {
        List<String> handles = handles();
        driver().switchTo().window(handles.get(handles.size() - 1));
    }

    public void switchToWindow(int index) {
        List<String> handles = handles();
        if (index < 1 || index > handles.size()) {
            throw new AssertionError(index + ". tab yoxdur (açıq tab sayı: " + handles.size() + ")");
        }
        driver().switchTo().window(handles.get(index - 1));
    }

    public void closeCurrentWindowAndReturn() {
        driver().close();
        driver().switchTo().window(handles().get(0));
    }

    public void openNewTab(String url) {
        driver().switchTo().newWindow(WindowType.TAB);
        navigate(url);
    }

    private List<String> handles() {
        return new ArrayList<>(driver().getWindowHandles());
    }

    // ---------- iframe ----------

    public void switchToFrame(String elementName) {
        try {
            defaultWait().until(ExpectedConditions.frameToBeAvailableAndSwitchToIt(by(elementName)));
        } catch (TimeoutException e) {
            throw new AssertionError("\"" + elementName + "\" iframe-inə keçid alınmadı");
        }
    }

    public void switchToMainContent() {
        driver().switchTo().defaultContent();
    }

    // ---------- Alert ----------

    private Alert alert() {
        try {
            return defaultWait().until(ExpectedConditions.alertIsPresent());
        } catch (TimeoutException e) {
            throw new AssertionError("Alert açılmadı");
        }
    }

    public void acceptAlert() {
        alert().accept();
    }

    public void dismissAlert() {
        alert().dismiss();
    }

    public void verifyAlertText(String text) {
        String expected = resolve(text);
        String actual = alert().getText();
        if (!actual.contains(expected)) {
            throw new AssertionError("Alert mətni \"" + expected + "\" ehtiva etmir. Faktiki: \"" + actual + "\"");
        }
    }

    public void typeIntoAlertAndAccept(String text) {
        Alert alert = alert();
        alert.sendKeys(resolve(text));
        alert.accept();
    }

    // ---------- Cookie / Storage ----------

    public void addCookie(String name, String value) {
        driver().manage().addCookie(new Cookie(name, resolve(value)));
    }

    public void deleteAllCookies() {
        driver().manage().deleteAllCookies();
    }

    public void verifyCookieExists(String name) {
        if (driver().manage().getCookieNamed(name) == null) {
            throw new AssertionError("\"" + name + "\" cookie-si tapılmadı");
        }
    }

    public void setLocalStorage(String key, String value) {
        js().executeScript("window.localStorage.setItem(arguments[0], arguments[1]);", key, resolve(value));
    }

    public void clearStorage() {
        js().executeScript("window.localStorage.clear(); window.sessionStorage.clear();");
    }

    // ---------- Digər ----------

    public Object executeScript(String script) {
        return js().executeScript(resolve(script));
    }

    public static void hardWait(int seconds) {
        try {
            Thread.sleep(seconds * 1000L);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}
