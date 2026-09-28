package utils;

import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.options.UiAutomator2Options;

import java.net.MalformedURLException;
import java.net.URL;
import java.time.Duration;

public class AppiumDriverFactory {

    public static AndroidDriver createAndroidDriver() {
        String serverUrl = Config.get("APPIUM_SERVER", "http://127.0.0.1:4723");
        String deviceName = Config.get("ANDROID_DEVICE", "emulator-5554");
        String platformVersion = Config.get("ANDROID_PLATFORM_VERSION", "");
        String appPackage = Config.get("ANDROID_APP_PACKAGE", "");
        String appActivity = Config.get("ANDROID_APP_ACTIVITY", "");
        String appPath = Config.get("ANDROID_APP", "");
        String browserName = Config.get("ANDROID_BROWSER", "");

        UiAutomator2Options options = new UiAutomator2Options()
                .setDeviceName(deviceName)
                .setNewCommandTimeout(Duration.ofSeconds(120))
                .setAutoGrantPermissions(true);

        if (!platformVersion.isBlank()) options.setPlatformVersion(platformVersion);
        if (!appPath.isBlank()) options.setApp(appPath);
        if (!appPackage.isBlank()) options.setAppPackage(appPackage);
        if (!appActivity.isBlank()) options.setAppActivity(appActivity);
        if (!browserName.isBlank()) options.setCapability("browserName", browserName);

        try {
            return new AndroidDriver(new URL(serverUrl), options);
        } catch (MalformedURLException e) {
            throw new IllegalStateException("Yanlış Appium server URL: " + serverUrl, e);
        }
    }
}