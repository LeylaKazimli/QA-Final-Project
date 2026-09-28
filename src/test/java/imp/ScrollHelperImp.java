package imp;

import com.thoughtworks.gauge.Step;
import helper.ScrollHelper;

public class ScrollHelperImp extends ScrollHelper {

    @Step("<elementName> elementine scroll et")
    public void elementineScrollEt(String elementName) {
        scrollToElement(elementName);
    }

    @Step("<elementName> elementine scroll et ve klik et")
    public void elementineScrollEtVeKlikEt(String elementName) {
        scrollToElementAndClick(elementName);
    }

    @Step("Sehifenin yuxarısına scroll et")
    public void sehifeninYuxarisinaScrollEt() {
        scrollToTop();
    }

    @Step("Sehifenin aşağısına scroll et")
    public void sehifeninAsagisinaScrollEt() {
        scrollToBottom();
    }

    @Step("<pixels> piksel horizontal scroll et")
    public void horizontalScroll(int pixels) {
        scrollHorizontalByPixels(pixels);
    }

    @Step("<pixels> piksel vertical scroll et")
    public void verticalScroll(int pixels) {
        scrollVerticalByPixels(pixels);
    }
}