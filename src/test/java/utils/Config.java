package utils;

// Bütün konfiqurasiya bir yerdən oxunur.
// Gauge env/<mühit>/*.properties fayllarındakı açarları environment variable kimi ötürür
// (`mvn test -Denv=ci` → env/default + env/ci). Shell-dən override: `headless=true mvn test`.
public final class Config {

    private Config() {
    }

    public static String get(String key, String fallback) {
        String value = System.getenv(key);
        if (value == null || value.isBlank()) value = System.getProperty(key);
        return (value == null || value.isBlank()) ? fallback : value.trim();
    }

    public static String require(String key) {
        String value = get(key, null);
        if (value == null) {
            throw new IllegalStateException("Konfiqurasiya açarı təyin edilməyib: " + key + " (env/default/app.properties)");
        }
        return value;
    }

    public static int getInt(String key, int fallback) {
        String value = get(key, null);
        return value == null ? fallback : Integer.parseInt(value);
    }

    public static boolean getBool(String key, boolean fallback) {
        String value = get(key, null);
        return value == null ? fallback : Boolean.parseBoolean(value);
    }

    // ---------- UI ----------
    public static String uiBaseUrl() {
        return get("ui_base_url", null);
    }

    public static String browser() {
        return get("browser", "chrome");
    }

    public static boolean headless() {
        return getBool("headless", false);
    }

    public static int explicitWaitSeconds() {
        return getInt("explicit_wait_seconds", 10);
    }

    public static boolean keepBrowserOpen() {
        return getBool("keep_browser_open", false);
    }

    // ---------- API ----------
    public static String apiBaseUrl() {
        return get("api_base_url", null);
    }

    public static int apiMaxRetries() {
        return getInt("api_max_retries", 2);
    }

    // Server cavab vermədikdə sorğunun sonsuz asılı qalmaması üçün (bağlantı və cavab gözləmə)
    public static int apiTimeoutSeconds() {
        return getInt("api_timeout_seconds", 30);
    }

    // Retry-After nə qədər böyük olsa da bir cəhd üçün maksimum gözləmə
    public static int apiRetryMaxWaitSeconds() {
        return getInt("api_retry_max_wait_seconds", 10);
    }

    public static boolean apiLogAll() {
        return getBool("api_log_all", true);
    }

    public static boolean apiRelaxedHttps() {
        return getBool("api_relaxed_https", false);
    }

    // "https://...", "file:..." kimi tam ünvanı olduğu kimi qaytarır, "/path" olduqda base URL-ə birləşdirir.
    public static String resolveUrl(String baseUrl, String urlOrPath) {
        if (urlOrPath.matches("^[a-zA-Z][a-zA-Z0-9+.-]*:.*")) return urlOrPath;
        if (baseUrl == null) {
            throw new IllegalStateException("Nisbi ünvan \"" + urlOrPath + "\" üçün base URL təyin edilməyib "
                    + "(env/default/app.properties və ya \"Set base Url to\" step-i)");
        }
        String base = baseUrl.endsWith("/") ? baseUrl.substring(0, baseUrl.length() - 1) : baseUrl;
        if (urlOrPath.isEmpty()) return base;
        return base + (urlOrPath.startsWith("/") || urlOrPath.startsWith("?") ? urlOrPath : "/" + urlOrPath);
    }
}