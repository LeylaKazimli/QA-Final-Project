package utils;

import com.thoughtworks.gauge.datastore.ScenarioDataStore;
import com.thoughtworks.gauge.datastore.SpecDataStore;

import java.time.LocalDate;
import java.util.Map;
import java.util.Random;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

// Testlər arası dəyişənlərin saxlanması və spec parametrlərində ${ad} əvəzlənməsi.
//
// Axtarış ardıcıllığı: ssenari → spec → suite → xüsusi dəyişənlər → env/*.properties
//
// Xüsusi (hər dəfə yeni dəyər) dəyişənlər:
//   ${random.uuid}   ${random.email}   ${random.number}   ${random.name}   ${random.phone}
//   ${timestamp}     ${today}     ${projectDir}
//   ${env.api_base_url}  → env/*.properties-dən istənilən açar
public final class ScenarioContext {

    private static final Map<String, Object> SUITE = new ConcurrentHashMap<>();
    private static final Pattern VARIABLE = Pattern.compile("\\$\\{([^}]+)}");
    private static final Random RANDOM = new Random();

    private ScenarioContext() {
    }

    public static void put(String name, Object value) {
        ScenarioDataStore.put(name, value);
    }

    // Bütün suite boyu (bütün spec/ssenarilərdə) görünən dəyişən
    public static void putSuite(String name, Object value) {
        SUITE.put(name, value);
    }

    public static Object get(String name) {
        Object value = ScenarioDataStore.get(name);
        if (value == null) value = SpecDataStore.get(name);
        if (value == null) value = SUITE.get(name);
        return value;
    }

    public static String getString(String name) {
        Object value = get(name);
        if (value == null) throw new IllegalArgumentException("Dəyişən tapılmadı: " + name);
        return String.valueOf(value);
    }

    // Mətndəki bütün ${ad} ifadələrini dəyərləri ilə əvəz edir
    public static String resolve(String text) {
        if (text == null || !text.contains("${")) return text;
        Matcher matcher = VARIABLE.matcher(text);
        StringBuffer result = new StringBuffer();
        while (matcher.find()) {
            String name = matcher.group(1).trim();
            String value = lookup(name);
            if (value == null) throw new IllegalArgumentException("Dəyişən tapılmadı: ${" + name + "}");
            matcher.appendReplacement(result, Matcher.quoteReplacement(value));
        }
        matcher.appendTail(result);
        return result.toString();
    }

    private static String lookup(String name) {
        Object stored = get(name);
        if (stored != null) return String.valueOf(stored);

        String shortId = UUID.randomUUID().toString().substring(0, 8);
        switch (name) {
            case "random.uuid":
                return UUID.randomUUID().toString();
            case "random.email":
                return "test_" + shortId + "@test.com";
            case "random.number":
                return String.valueOf(100000 + RANDOM.nextInt(900000));
            case "random.name":
                return "User_" + shortId;
            case "random.phone":
                return "+99450" + (1000000 + RANDOM.nextInt(9000000));
            case "timestamp":
                return String.valueOf(System.currentTimeMillis());
            case "today":
                return LocalDate.now().toString();
            case "projectDir":
                return System.getProperty("user.dir");
            default:
                if (name.startsWith("env.")) return Config.get(name.substring(4), null);
                return null;
        }
    }
}