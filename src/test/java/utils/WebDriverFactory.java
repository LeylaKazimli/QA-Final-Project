package utils;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.edge.EdgeOptions;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxOptions;
import org.openqa.selenium.safari.SafariDriver;

// Brauzer növünə görə WebDriver yaradır.
// Driver binary-lərini WebDriverManager brauzerin versiyasına uyğun avtomatik yükləyir
// (PATH-da qalmış köhnə chromedriver "only supports Chrome version X" xətası vermir).
// "-headless" suffiksi və ya `headless = true` konfiqurasiyası brauzeri headless açır.
public final class WebDriverFactory {

    private WebDriverFactory() {
    }

    public static WebDriver create(String browserType) {
        String type = browserType.trim().toLowerCase();
        boolean headless = Config.headless() || type.endsWith("-headless");
        String browser = type.replace("-headless", "");

        WebDriver driver;
        switch (browser) {
            case "chrome":
                WebDriverManager.chromedriver().setup();
                ChromeOptions chrome = new ChromeOptions();
                chrome.addArguments("--disable-notifications", "--disable-search-engine-choice-screen");
                if (headless) chrome.addArguments("--headless=new", "--window-size=1920,1080");
                driver = new ChromeDriver(chrome);
                break;

            case "firefox":
                WebDriverManager.firefoxdriver().setup();
                FirefoxOptions firefox = new FirefoxOptions();
                firefox.addPreference("dom.webnotifications.enabled", false);
                if (headless) firefox.addArguments("-headless");
                driver = new FirefoxDriver(firefox);
                break;

            case "edge":
                WebDriverManager.edgedriver().setup();
                EdgeOptions edge = new EdgeOptions();
                edge.addArguments("--disable-notifications");
                if (headless) edge.addArguments("--headless=new", "--window-size=1920,1080");
                driver = new EdgeDriver(edge);
                break;

            case "safari":
                // safaridriver macOS-da daxilidir; bir dəfə `safaridriver --enable` lazımdır. Headless dəstəkləmir.
                driver = new SafariDriver();
                break;

            default:
                throw new IllegalArgumentException("Dəstəklənməyən brauzer: " + browserType
                        + ". Mövcud seçimlər: chrome, firefox, edge, safari (+ \"-headless\")");
        }

        if (headless) {
            driver.manage().window().setSize(new Dimension(1920, 1080));
        } else {
            driver.manage().window().maximize();
        }
        return driver;
    }
}