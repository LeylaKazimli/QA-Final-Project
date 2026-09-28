package helper;

import org.openqa.selenium.By;
import org.openqa.selenium.ElementClickInterceptedException;
import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;

import java.util.List;

// Klik və mouse əməliyyatları
public class ClickHelper extends BaseHelper {

    public void clickElement(String elementName) {
        WebElement element = clickable(elementName);
        try {
            element.click();
        } catch (ElementClickInterceptedException e) {
            // Element sticky header / overlay altında qalıbsa: ortaya scroll et və yenidən cəhd et
            scrollIntoView(element);
            clickable(elementName).click();
        }
    }

    // Normal klik işləməyəndə (görünməz overlay, custom komponent) son çarə
    public void jsClick(String elementName) {
        js().executeScript("arguments[0].click();", present(elementName));
    }

    public void doubleClick(String elementName) {
        new Actions(driver()).doubleClick(clickable(elementName)).perform();
    }

    public void rightClick(String elementName) {
        new Actions(driver()).contextClick(clickable(elementName)).perform();
    }

    public void hover(String elementName) {
        new Actions(driver()).moveToElement(visible(elementName)).perform();
    }

    public void dragAndDrop(String sourceName, String targetName) {
        new Actions(driver()).dragAndDrop(visible(sourceName), visible(targetName)).perform();
    }

    // Eyni locator-a uyğun elementlər siyahısından mətni uyğun gələnə klik edir (menyu, list, cədvəl sətri)
    public void clickElementWithText(String elementName, String text) {
        String expected = resolve(text);
        visible(elementName);
        List<WebElement> elements = all(elementName);
        for (WebElement element : elements) {
            if (element.getText().trim().equals(expected)) {
                scrollIntoView(element);
                element.click();
                return;
            }
        }
        throw new AssertionError("\"" + elementName + "\" siyahısında \"" + expected + "\" mətnli element tapılmadı ("
                + elements.size() + " element yoxlanıldı)");
    }

    public void clickElementAtIndex(String elementName, int index) {
        visible(elementName);
        List<WebElement> elements = all(elementName);
        if (index < 1 || index > elements.size()) {
            throw new AssertionError("\"" + elementName + "\" üçün " + index + ". element yoxdur (cəmi " + elements.size() + ")");
        }
        WebElement element = elements.get(index - 1);
        scrollIntoView(element);
        element.click();
    }

    // Locator yazmadan görünən mətnə görə klik (düymə, link, menyu bəndi)
    public void clickByVisibleText(String text) {
        String expected = resolve(text);
        String literal = expected.contains("'") ? "concat('" + expected.replace("'", "', \"'\", '") + "')" : "'" + expected + "'";
        By by = By.xpath("//*[normalize-space(.)=" + literal + " and not(.//*[normalize-space(.)=" + literal + "])]");
        try {
            defaultWait().until(ExpectedConditions.elementToBeClickable(by)).click();
        } catch (TimeoutException e) {
            throw new AssertionError("\"" + expected + "\" mətnli kliklənə bilən element tapılmadı");
        }
    }

    // Cookie banner, reklam popup-u kimi bəzən çıxan elementlər üçün: varsa klik et, yoxdursa keç
    public void clickIfPresent(String elementName, int seconds) {
        try {
            visible(elementName, seconds).click();
        } catch (AssertionError ignored) {
            System.out.println("\"" + elementName + "\" görünmədi, klik ötürüldü");
        }
    }
}