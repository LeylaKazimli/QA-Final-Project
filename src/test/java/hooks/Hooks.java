package hooks;

import com.thoughtworks.gauge.AfterScenario;
import com.thoughtworks.gauge.BeforeScenario;
import helper.ApiHelper;
import utils.Config;
import utils.DriverManager;

// Hər ssenarinin təmiz başlaması və təmiz bitməsi.
// Test ortada düşsə belə brauzer bağlanır — açıq qalmış Chrome prosesləri yığılmır.
public class Hooks {

    @BeforeScenario
    public void beforeScenario() {
        ApiHelper.clear();
    }

    @AfterScenario
    public void afterScenario() {
        ApiHelper.clear();
        if (!Config.keepBrowserOpen()) {
            try {
                DriverManager.quitDriver();
            } catch (RuntimeException e) {
                System.out.println("Driver bağlanarkən xəta: " + e.getMessage());
            }
        }
    }
}
