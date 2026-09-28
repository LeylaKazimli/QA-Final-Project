package imp;

import com.thoughtworks.gauge.Step;
import helper.VerifyHelper;

public class VerifyElementImp extends VerifyHelper {

    // ---------- Gözləmələr ----------

    @Step("<element> görsensin deye maksimum <second> saniye gözle")
    public void waitForElement(String element, int second) {
        waitUntilElementIsVisible(element, second);
    }

    @Step("<element> yox olana qeder maksimum <second> saniye gözle")
    public void waitForElementToDisappear(String element, int second) {
        waitUntilElementDisappears(element, second);
    }

    @Step("<element> kliklene bilene qeder gözle")
    public void waitForClickable(String element) {
        waitUntilClickable(element);
    }

    @Step("Sehifenin tam yüklenmesini gözle")
    public void waitForPage() {
        waitForPageLoad();
    }

    // ---------- Mətn ----------

    @Step("<element> elementin içinde <text> yazısı var")
    public void verifyElementContain(String element, String text) {
        verifElementTextContains(element, text);
    }

    @Step("<element> elementinin metni <text> olmalıdır")
    public void verifyElementText(String element, String text) {
        verifyElementTextEquals(element, text);
    }

    @Step("Sehifede <text> yazısı olmalıdır")
    public void verifyPageText(String text) {
        verifyPageContainsText(text);
    }

    // ---------- Vəziyyət ----------

    @Step("<element> görünür olmalıdır")
    public void shouldBeVisible(String element) {
        verifyVisible(element);
    }

    @Step("<element> görünmemelidir")
    public void shouldNotBeVisible(String element) {
        verifyNotVisible(element);
    }

    @Step("<element> sehifede mövcud olmamalıdır")
    public void shouldNotExist(String element) {
        verifyNotPresent(element);
    }

    @Step("<element> aktiv olmalıdır")
    public void shouldBeEnabled(String element) {
        verifyEnabled(element, true);
    }

    @Step("<element> deaktiv olmalıdır")
    public void shouldBeDisabled(String element) {
        verifyEnabled(element, false);
    }

    @Step("<element> seçilmiş olmalıdır")
    public void shouldBeSelected(String element) {
        verifySelected(element, true);
    }

    @Step("<element> seçilmemiş olmalıdır")
    public void shouldNotBeSelected(String element) {
        verifySelected(element, false);
    }

    // ---------- Atribut / dəyər / say ----------

    @Step("<element> elementinin <attribute> atributu <value> olmalıdır")
    public void attributeShouldBe(String element, String attribute, String value) {
        verifyAttributeEquals(element, attribute, value);
    }

    @Step("<element> elementinin <attribute> atributunda <value> olmalıdır")
    public void attributeShouldContain(String element, String attribute, String value) {
        verifyAttributeContains(element, attribute, value);
    }

    @Step("<element> input deyeri <value> olmalıdır")
    public void inputValueShouldBe(String element, String value) {
        verifyInputValue(element, value);
    }

    @Step("<element> elementlerinin sayı <count> olmalıdır")
    public void countShouldBe(String element, int count) {
        verifyElementCount(element, count);
    }

    @Step("<element> elementlerinin sayı en az <count> olmalıdır")
    public void countShouldBeAtLeast(String element, int count) {
        verifyElementCountAtLeast(element, count);
    }

    // ---------- Dəyəri yadda saxlamaq ----------

    @Step("<element> elementinin metnini <variable> olaraq yadda saxla")
    public void saveText(String element, String variable) {
        saveElementText(element, variable);
    }

    @Step("<element> elementinin <attribute> atributunu <variable> olaraq yadda saxla")
    public void saveAttribute(String element, String attribute, String variable) {
        saveElementAttribute(element, attribute, variable);
    }
}