package utils;

import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import org.openqa.selenium.By;

import java.io.IOException;
import java.io.Reader;
import java.nio.charset.StandardCharsets;
import java.nio.file.DirectoryStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// Locator repository: src/test/resources/locator/ qovluğundakı BÜTÜN *.json fayllarını
// bir dəfə oxuyub yaddaşda saxlayır. Hər səhifə üçün ayrıca json faylı yaratmaq olar.
// Eyni element adı iki faylda olarsa xəta verir (səssizcə səhv locator işlətməmək üçün).
//
// Fayl formatı:
//   "Element Adı": { "locatorType": "ID", "locatorValue": "fullName" }
// Dəstəklənən tiplər: ID, NAME, XPATH, CSS (CSS_SELECTOR), CLASS_NAME, TAG_NAME, LINK_TEXT, PARTIAL_LINK_TEXT
public final class LocatorReader {

    private static final Path LOCATOR_DIR = Paths.get("src/test/resources/locator");
    private static volatile Map<String, String[]> locators;

    private LocatorReader() {
    }

    // Element adı json-da yoxdursa və "tip=dəyər" formasındadırsa inline locator kimi işlənir:
    //   "id=username"   "css=button.primary"   "xpath=//a[text()='Giriş']"   "name=email"
    public static By getBy(String elementName) {
        String[] locator = locators().get(elementName);
        if (locator == null) {
            int separator = elementName.indexOf('=');
            if (separator > 0 && elementName.substring(0, separator).matches("(?i)[a-z_ ]+")) {
                return toBy(elementName.substring(0, separator), elementName.substring(separator + 1));
            }
            throw new IllegalArgumentException("Locator tapılmadı: \"" + elementName + "\" (" + LOCATOR_DIR + "/*.json)");
        }
        return toBy(locator[0], locator[1]);
    }

    public static String getLocatorType(String elementName) {
        return require(elementName)[0];
    }

    public static String getLocatorValue(String elementName) {
        return require(elementName)[1];
    }

    private static String[] require(String elementName) {
        String[] locator = locators().get(elementName);
        if (locator == null) throw new IllegalArgumentException("Locator tapılmadı: \"" + elementName + "\"");
        return locator;
    }

    static By toBy(String type, String value) {
        switch (type.toUpperCase().replace("_", "").replace(" ", "")) {
            case "ID":
                return By.id(value);
            case "NAME":
                return By.name(value);
            case "XPATH":
                return By.xpath(value);
            case "CSS":
            case "CSSSELECTOR":
                return By.cssSelector(value);
            case "CLASSNAME":
                return By.className(value);
            case "TAGNAME":
                return By.tagName(value);
            case "LINKTEXT":
                return By.linkText(value);
            case "PARTIALLINKTEXT":
                return By.partialLinkText(value);
            default:
                throw new IllegalArgumentException("Bu locator tipi dəstəklənmir: " + type);
        }
    }

    private static Map<String, String[]> locators() {
        if (locators == null) {
            synchronized (LocatorReader.class) {
                if (locators == null) locators = load();
            }
        }
        return locators;
    }

    private static Map<String, String[]> load() {
        Map<String, String[]> result = new HashMap<>();
        Map<String, Path> origin = new HashMap<>();
        List<Path> files = new ArrayList<>();
        try (DirectoryStream<Path> stream = Files.newDirectoryStream(LOCATOR_DIR, "*.json")) {
            stream.forEach(files::add);
        } catch (IOException e) {
            throw new IllegalStateException("Locator qovluğu oxuna bilmədi: " + LOCATOR_DIR.toAbsolutePath(), e);
        }
        Collections.sort(files);

        for (Path file : files) {
            try (Reader reader = Files.newBufferedReader(file, StandardCharsets.UTF_8)) {
                JsonObject json = JsonParser.parseReader(reader).getAsJsonObject();
                for (Map.Entry<String, JsonElement> entry : json.entrySet()) {
                    String name = entry.getKey();
                    if (origin.containsKey(name)) {
                        throw new IllegalStateException("Təkrarlanan locator adı \"" + name + "\": "
                                + origin.get(name).getFileName() + " və " + file.getFileName());
                    }
                    JsonObject locator = entry.getValue().getAsJsonObject();
                    result.put(name, new String[]{
                            locator.get("locatorType").getAsString(),
                            locator.get("locatorValue").getAsString()});
                    origin.put(name, file);
                }
            } catch (IOException e) {
                throw new IllegalStateException("Locator faylı oxuna bilmədi: " + file, e);
            }
        }
        return Collections.unmodifiableMap(result);
    }
}