package imp;

import
        com.thoughtworks.gauge.Step;
import io.appium.java_client.android.AndroidDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import utils.AppiumDriverFactory;
import utils.DriverManager;

import java.time.Duration;

public class MobileImp {

    private static AndroidDriver androidDriver() {
        return (AndroidDriver) DriverManager.getDriver();
    }

    @Step("Android tətbiqini aç")
    public void openAndroidApp() {
        if (DriverManager.getDriver() == null) {
            AndroidDriver driver = AppiumDriverFactory.createAndroidDriver();
            DriverManager.setDriver(driver);
        }
    }

    @Step("Android elementi <accessibilityId> görsənsin deyə maksimum <seconds> saniyə gözlə")
    public void waitForAccessibilityId(String accessibilityId, String seconds) {
        WebDriverWait wait = new WebDriverWait(androidDriver(), Duration.ofSeconds(Long.parseLong(seconds)));
        wait.until(ExpectedConditions.visibilityOfElementLocated(
                By.xpath("//*[@content-desc='" + accessibilityId + "']")));
    }

    @Step("Android elementi <accessibilityId> üzərinə klik et")
    public void tapAccessibilityId(String accessibilityId) {
        androidDriver()
                .findElement(
                By.xpath("//*[@content-desc='" + accessibilityId + "']")).click();
    }

    @Step("Android mətni <text> görsənsin deyə maksimum <seconds> saniyə gözlə")
    public void waitForText(String text, String seconds) {
        WebDriverWait wait = new WebDriverWait(androidDriver(), Duration.ofSeconds(Long.parseLong(seconds)));
        wait.until(ExpectedConditions.visibilityOfElementLocated(
                By.xpath("//*[@text='" + text + "']")));
    }

    @Step("Android mətni <text> üzərinə klik et")
    public void tapText(String text) {
        androidDriver().findElement(
                By.xpath("//*[@text='" + text + "']")).click();
    }

    @Step("Android tətbiqini bağla")
    public void quitAndroidApp() {
        DriverManager.quitDriver();
    }
}