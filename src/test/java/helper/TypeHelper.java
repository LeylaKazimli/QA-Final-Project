package helper;

import org.openqa.selenium.Keys;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.Select;

import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

// Form əməliyyatları: yazmaq, klaviatura, dropdown, checkbox/radio, fayl yükləmə
public class TypeHelper extends BaseHelper {

    private static final String FILES_DIR = "src/test/resources/files";

    public void type(String elementName, String text) {
        WebElement element = visible(elementName);
        element.clear();
        element.sendKeys(resolve(text));
    }

    // Köhnə step-lər üçün: sahəni təmizləmədən yazır və sonra düymə basır
    public void typeAndPressKey(String elementName, String text, String keyName) {
        visible(elementName).sendKeys(resolve(text), key(keyName));
    }

    public void clear(String elementName) {
        WebElement element = visible(elementName);
        element.clear();
        // Bəzi React/Angular input-ları clear()-dən sonra köhnə dəyəri qaytarır — klaviatura ilə də təmizlə
        if (!element.getAttribute("value").isEmpty()) {
            element.sendKeys(Keys.chord(Keys.CONTROL, "a"), Keys.DELETE);
            element.sendKeys(Keys.chord(Keys.COMMAND, "a"), Keys.DELETE);
        }
    }

    public void pressKey(String elementName, String keyName) {
        visible(elementName).sendKeys(key(keyName));
    }

    // Fokusda olan elementə düymə göndərir (məs. modalı ESCAPE ilə bağlamaq)
    public void pressKeyOnPage(String keyName) {
        driver().switchTo().activeElement().sendKeys(key(keyName));
    }

    public void selectByText(String elementName, String text) {
        new Select(visible(elementName)).selectByVisibleText(resolve(text));
    }

    public void selectByValue(String elementName, String value) {
        new Select(visible(elementName)).selectByValue(resolve(value));
    }

    public void selectByIndex(String elementName, int index) {
        new Select(visible(elementName)).selectByIndex(index);
    }

    public void setChecked(String elementName, boolean checked) {
        WebElement element = present(elementName);
        if (element.isSelected() != checked) {
            scrollIntoView(element);
            try {
                element.click();
            } catch (RuntimeException e) {
                // Custom checkbox-larda input gizli olur — JS ilə klik
                js().executeScript("arguments[0].click();", element);
            }
        }
    }

    // <input type="file"> çox vaxt gizli olur, ona görə görünürlük yox, mövcudluq gözlənilir
    public void uploadFile(String elementName, String fileName) {
        Path file = Paths.get(FILES_DIR, fileName).toAbsolutePath();
        if (!Files.exists(file)) throw new IllegalArgumentException("Yüklənəcək fayl tapılmadı: " + file);
        present(elementName).sendKeys(file.toString());
    }

    // "ENTER", "TAB", "ESCAPE", "ARROW_DOWN", "BACK_SPACE" ... — org.openqa.selenium.Keys adları
    static Keys key(String keyName) {
        String normalized = keyName.trim().toUpperCase().replace(' ', '_');
        if (normalized.equals("ESC")) normalized = "ESCAPE";
        if (normalized.equals("BACKSPACE")) normalized = "BACK_SPACE";
        try {
            return Keys.valueOf(normalized);
        } catch (IllegalArgumentException e) {
            throw new IllegalArgumentException("Naməlum düymə: " + keyName + " (nümunə: ENTER, TAB, ESCAPE, ARROW_DOWN)");
        }
    }
}