package imp;

import com.thoughtworks.gauge.Step;
import utils.ScenarioContext;

// Test dəyişənləri. Saxlanılan dəyərlər istənilən step parametrində ${ad} kimi işlədilir.
// Dəyərdə xüsusi dəyişənlər də ola bilər: ${random.email}, ${random.number}, ${timestamp} ...
public class DataImp {

    @Step("<name> deyişenine <value> deyerini ver")
    public void setVariable(String name, String value) {
        ScenarioContext.put(name, ScenarioContext.resolve(value));
    }

    @Step("<name> global deyişenine <value> deyerini ver")
    public void setSuiteVariable(String name, String value) {
        ScenarioContext.putSuite(name, ScenarioContext.resolve(value));
    }

    @Step("<name> deyişeni <value> olmalıdır")
    public void variableShouldBe(String name, String value) {
        String actual = ScenarioContext.getString(name);
        String expected = ScenarioContext.resolve(value);
        if (!actual.equals(expected)) {
            throw new AssertionError(name + " gözlənilən: \"" + expected + "\", faktiki: \"" + actual + "\"");
        }
    }

    @Step("<name> deyişeninin deyerini çap et")
    public void printVariable(String name) {
        System.out.println(name + " = " + ScenarioContext.getString(name));
    }
}
