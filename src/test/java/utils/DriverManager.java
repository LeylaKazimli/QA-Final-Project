package utils;

import org.openqa.selenium.WebDriver;

// Aktiv driver (web və ya Appium) üçün tək saxlama yeri.
// ThreadLocal — hər thread öz driver-ini saxlayır, ona görə parallel icra təhlükəsizdir.
public final class DriverManager {

    private static final ThreadLocal<WebDriver> DRIVER = new ThreadLocal<>();

    private DriverManager() {
    }

    public static WebDriver getDriver() {
        return DRIVER.get();
    }

    public static boolean hasDriver() {
        return DRIVER.get() != null;
    }

    // Driver olmadan element addımı çağırılanda NullPointerException əvəzinə aydın xəta verir.
    public static WebDriver requireDriver() {
        WebDriver driver = DRIVER.get();
        if (driver == null) {
            throw new IllegalStateException("Aktiv brauzer/cihaz yoxdur. Əvvəlcə brauzeri və ya tətbiqi açın.");
        }
        return driver;
    }

    public static void setDriver(WebDriver driver) {
        DRIVER.set(driver);
    }

    public static void quitDriver() {
        WebDriver driver = DRIVER.get();
        if (driver == null) return;
        try {
            driver.quit();
        } finally {
            DRIVER.remove();
        }
    }
}