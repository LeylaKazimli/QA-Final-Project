package helper;

import org.openqa.selenium.WebElement;

// Scroll əməliyyatları. Selenium-un öz scroll komandası olmadığı üçün JavascriptExecutor işlədilir.
public class ScrollHelper extends BaseHelper {

    // scrollIntoView daxili scroll konteynerlərində də işləyir (window.scrollTo işləmir)
    public void scrollToElement(String elementName) {
        scrollIntoView(present(elementName));
    }

    public void scrollToElementAndClick(String elementName) {
        WebElement element = present(elementName);
        scrollIntoView(element);
        clickable(elementName).click();
    }

    public void scrollToTop() {
        js().executeScript("window.scrollTo({top: 0, behavior: 'instant'});");
    }

    public void scrollToBottom() {
        js().executeScript("window.scrollTo({top: document.body.scrollHeight, behavior: 'instant'});");
    }

    // Müsbət dəyər aşağı/sağa, mənfi yuxarı/sola
    public void scrollVerticalByPixels(int pixels) {
        js().executeScript("window.scrollBy({top: arguments[0], behavior: 'instant'});", pixels);
    }

    public void scrollHorizontalByPixels(int pixels) {
        js().executeScript("window.scrollBy({left: arguments[0], behavior: 'instant'});", pixels);
    }
}
