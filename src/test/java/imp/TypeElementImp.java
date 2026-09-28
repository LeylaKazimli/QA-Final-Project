package imp;

import com.thoughtworks.gauge.Step;
import helper.TypeHelper;

public class TypeElementImp extends TypeHelper {

    @Step("<elementName> elementine <text> yaz")
    public void typeText(String elementName, String text) {
        type(elementName, text);
    }

    @Step("<elementName> elementine <text> yaz ve Enter düymesine bas")
    public void typeAndEnter(String elementName, String text) {
        typeAndPressKey(elementName, text, "ENTER");
    }

    @Step("<elementName> elementine <text> yaz ve Tab düymesine bas")
    public void typeAndTab(String elementName, String text) {
        typeAndPressKey(elementName, text, "TAB");
    }

    @Step("<elementName> elementine <text> yaz ve Shift düymesine bas")
    public void typeAndShift(String elementName, String text) {
        typeAndPressKey(elementName, text, "SHIFT");
    }

    @Step("<elementName> elementini temizle")
    public void clearElement(String elementName) {
        clear(elementName);
    }

    @Step("<elementName> elementinde <key> düymesine bas")
    public void pressKeyOnElement(String elementName, String key) {
        pressKey(elementName, key);
    }

    @Step("Sehifede <key> düymesine bas")
    public void pressKeyOnActiveElement(String key) {
        pressKeyOnPage(key);
    }

    @Step("<elementName> dropdown-undan <text> metnini seç")
    public void dropdownByText(String elementName, String text) {
        selectByText(elementName, text);
    }

    @Step("<elementName> dropdown-undan <value> deyerini seç")
    public void dropdownByValue(String elementName, String value) {
        selectByValue(elementName, value);
    }

    @Step("<elementName> dropdown-undan <index> indeksli seçimi seç")
    public void dropdownByIndex(String elementName, int index) {
        selectByIndex(elementName, index);
    }

    @Step("<elementName> checkbox-unu işaretle")
    public void check(String elementName) {
        setChecked(elementName, true);
    }

    @Step("<elementName> checkbox-unun işaretini kaldır")
    public void uncheck(String elementName) {
        setChecked(elementName, false);
    }

    @Step("<elementName> elementine <fileName> faylını yükle")
    public void upload(String elementName, String fileName) {
        uploadFile(elementName, fileName);
    }
}