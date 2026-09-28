package helper;

import org.openqa.selenium.By;
import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import utils.ScenarioContext;

// Gözləmə və yoxlama (assertion) əməliyyatları.
// Bütün yoxlamalar default wait müddətində təkrar cəhd edir — asinxron UI üçün etibarlıdır.
public class VerifyHelper extends BaseHelper {

    public void waitUntilElementIsVisible(String elementName, int timeoutSeconds) {
        visible(elementName, timeoutSeconds);
    }

    public void waitUntilElementDisappears(String elementName, int timeoutSeconds) {
        try {
            waitFor(timeoutSeconds).until(ExpectedConditions.invisibilityOfElementLocated(by(elementName)));
        } catch (TimeoutException e) {
            throw new AssertionError("\"" + elementName + "\" " + timeoutSeconds + " saniyə ərzində yox olmadı");
        }
    }

    public void waitUntilClickable(String elementName) {
        clickable(elementName);
    }

    public void waitForPageLoad() {
        defaultWait().until(d -> "complete".equals(js().executeScript("return document.readyState")));
    }

    public void verifElementTextContains(String elementName, String expectedText) {
        String expected = resolve(expectedText);
        visible(elementName);
        assertEventually(() -> text(elementName).contains(expected),
                () -> "\"" + elementName + "\" mətni \"" + expected + "\" ehtiva etmir. Faktiki: \"" + text(elementName) + "\"");
    }

    public void verifyElementTextEquals(String elementName, String expectedText) {
        String expected = resolve(expectedText);
        visible(elementName);
        assertEventually(() -> text(elementName).equals(expected),
                () -> "\"" + elementName + "\" mətni gözlənilən deyil. Gözlənilən: \"" + expected + "\", faktiki: \"" + text(elementName) + "\"");
    }

    public void verifyVisible(String elementName) {
        visible(elementName);
    }

    public void verifyNotVisible(String elementName) {
        assertEventually(() -> all(elementName).stream().noneMatch(WebElement::isDisplayed),
                () -> "\"" + elementName + "\" görünməməli idi, amma görünür");
    }

    public void verifyNotPresent(String elementName) {
        assertEventually(() -> all(elementName).isEmpty(),
                () -> "\"" + elementName + "\" səhifədə olmamalı idi, amma " + all(elementName).size() + " ədəd tapıldı");
    }

    public void verifyEnabled(String elementName, boolean expected) {
        visible(elementName);
        assertEventually(() -> driver().findElement(by(elementName)).isEnabled() == expected,
                () -> "\"" + elementName + "\" " + (expected ? "aktiv" : "deaktiv") + " olmalı idi");
    }

    public void verifySelected(String elementName, boolean expected) {
        present(elementName);
        assertEventually(() -> driver().findElement(by(elementName)).isSelected() == expected,
                () -> "\"" + elementName + "\" " + (expected ? "seçilmiş" : "seçilməmiş") + " olmalı idi");
    }

    public void verifyAttributeEquals(String elementName, String attribute, String expectedValue) {
        String expected = resolve(expectedValue);
        present(elementName);
        assertEventually(() -> expected.equals(attribute(elementName, attribute)),
                () -> "\"" + elementName + "\" [" + attribute + "] gözlənilən: \"" + expected + "\", faktiki: \"" + attribute(elementName, attribute) + "\"");
    }

    public void verifyAttributeContains(String elementName, String attribute, String expectedValue) {
        String expected = resolve(expectedValue);
        present(elementName);
        assertEventually(() -> String.valueOf(attribute(elementName, attribute)).contains(expected),
                () -> "\"" + elementName + "\" [" + attribute + "] \"" + expected + "\" ehtiva etmir. Faktiki: \"" + attribute(elementName, attribute) + "\"");
    }

    public void verifyInputValue(String elementName, String expectedValue) {
        verifyAttributeEquals(elementName, "value", expectedValue);
    }

    public void verifyElementCount(String elementName, int expectedCount) {
        assertEventually(() -> all(elementName).size() == expectedCount,
                () -> "\"" + elementName + "\" sayı " + expectedCount + " olmalı idi, faktiki: " + all(elementName).size());
    }

    public void verifyElementCountAtLeast(String elementName, int minimumCount) {
        assertEventually(() -> all(elementName).size() >= minimumCount,
                () -> "\"" + elementName + "\" sayı ən azı " + minimumCount + " olmalı idi, faktiki: " + all(elementName).size());
    }

    public void verifyPageContainsText(String text) {
        String expected = resolve(text);
        assertEventually(() -> driver().findElement(By.tagName("body")).getText().contains(expected),
                () -> "Səhifədə \"" + expected + "\" mətni tapılmadı");
    }

    public void saveElementText(String elementName, String variableName) {
        String value = visible(elementName).getText().trim();
        ScenarioContext.put(variableName, value);
        System.out.println(variableName + " = " + value);
    }

    public void saveElementAttribute(String elementName, String attribute, String variableName) {
        String value = present(elementName).getAttribute(attribute);
        ScenarioContext.put(variableName, value);
        System.out.println(variableName + " = " + value);
    }

    private String text(String elementName) {
        return driver().findElement(by(elementName)).getText().trim();
    }

    private String attribute(String elementName, String attribute) {
        return driver().findElement(by(elementName)).getAttribute(attribute);
    }
}