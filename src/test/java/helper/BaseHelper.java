package helper;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.StaleElementReferenceException;
import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import utils.Config;
import utils.DriverManager;
import utils.LocatorReader;
import utils.ScenarioContext;

import java.time.Duration;
import java.util.List;
import java.util.function.BooleanSupplier;
import java.util.function.Supplier;

// Bütün UI helper-lərin ortaq bazası.
// Driver konstruktorda YOX, hər çağırışda DriverManager-dən götürülür — beləliklə
// Gauge step sinfini brauzer açılmamış yaratsa belə problem olmur.
public abstract class BaseHelper {

    protected WebDriver driver() {
        return DriverManager.requireDriver();
    }

    protected WebDriverWait waitFor(int seconds) {
        return new WebDriverWait(driver(), Duration.ofSeconds(seconds));
    }

    protected WebDriverWait defaultWait() {
        return waitFor(Config.explicitWaitSeconds());
    }

    protected JavascriptExecutor js() {
        return (JavascriptExecutor) driver();
    }

    protected By by(String elementName) {
        return LocatorReader.getBy(ScenarioContext.resolve(elementName));
    }

    // Spec parametrindəki ${dəyişən}-ləri əvəz edir
    protected String resolve(String text) {
        return ScenarioContext.resolve(text);
    }

    protected WebElement visible(String elementName) {
        return visible(elementName, Config.explicitWaitSeconds());
    }

    protected WebElement visible(String elementName, int seconds) {
        try {
            return waitFor(seconds).until(ExpectedConditions.visibilityOfElementLocated(by(elementName)));
        } catch (TimeoutException e) {
            throw new AssertionError("\"" + elementName + "\" " + seconds + " saniyə ərzində görünmədi (" + by(elementName) + ")");
        }
    }

    protected WebElement present(String elementName) {
        try {
            return defaultWait().until(ExpectedConditions.presenceOfElementLocated(by(elementName)));
        } catch (TimeoutException e) {
            throw new AssertionError("\"" + elementName + "\" DOM-da tapılmadı (" + by(elementName) + ")");
        }
    }

    protected WebElement clickable(String elementName) {
        try {
            return defaultWait().until(ExpectedConditions.elementToBeClickable(by(elementName)));
        } catch (TimeoutException e) {
            throw new AssertionError("\"" + elementName + "\" kliklənə bilən vəziyyətə gəlmədi (" + by(elementName) + ")");
        }
    }

    protected List<WebElement> all(String elementName) {
        return driver().findElements(by(elementName));
    }

    protected void scrollIntoView(WebElement element) {
        js().executeScript("arguments[0].scrollIntoView({block:'center', inline:'nearest'});", element);
    }

    // Şərt default wait müddətində doğru olana qədər təkrar yoxlanılır; olmasa aydın mesajla düşür.
    // Asinxron yenilənən UI-da (AJAX, animasiya) flaky testlərin qarşısını alır.
    protected void assertEventually(BooleanSupplier condition, Supplier<String> failureMessage) {
        try {
            defaultWait()
                    .ignoring(NoSuchElementException.class)
                    .ignoring(StaleElementReferenceException.class)
                    .until(d -> condition.getAsBoolean());
        } catch (TimeoutException e) {
            throw new AssertionError(failureMessage.get());
        }
    }
}