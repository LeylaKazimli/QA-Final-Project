package imp;

import com.thoughtworks.gauge.Step;
import helper.ClickHelper;

public class ClickElementImp extends ClickHelper {

    @Step("<element> elementine klik et")
    public void elementineKlikEt(String element) {
        clickElement(element);
    }

    @Step("<element> elementine JavaScript ile klik et")
    public void elementineJsKlikEt(String element) {
        jsClick(element);
    }

    @Step("<element> elementine iki defe klik et")
    public void elementineIkiDefeKlikEt(String element) {
        doubleClick(element);
    }

    @Step("<element> elementine sağ klik et")
    public void elementineSagKlikEt(String element) {
        rightClick(element);
    }

    @Step("<element> elementinin üzerine gel")
    public void elementinUzerineGel(String element) {
        hover(element);
    }

    @Step("<source> elementini <target> elementinin üzerine sürükle")
    public void surukleVeBurax(String source, String target) {
        dragAndDrop(source, target);
    }

    @Step("<element> siyahısında <text> metnli elemente klik et")
    public void siyahidaMetneGoreKlik(String element, String text) {
        clickElementWithText(element, text);
    }

    @Step("<element> siyahısında <index> nömreli elemente klik et")
    public void siyahidaIndekseGoreKlik(String element, int index) {
        clickElementAtIndex(element, index);
    }

    @Step("<element> elementi <seconds> saniye içinde görünerse klik et")
    public void gorunerseKlikEt(String element, int seconds) {
        clickIfPresent(element, seconds);
    }

    @Step("<text> metnli elemente klik et")
    public void metneGoreKlik(String text) {
        clickByVisibleText(text);
    }
}
