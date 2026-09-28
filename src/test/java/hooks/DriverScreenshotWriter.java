package hooks;

import com.thoughtworks.gauge.screenshot.CustomScreenshotWriter;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import utils.Config;
import utils.DriverManager;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.UUID;

// Uğursuz step-də Gauge bu sinfi avtomatik çağırır (classpath-da tapır).
// Bütün ekranın yox, brauzerin/cihazın öz screenshot-unu hesabata əlavə edir.
// Aktiv driver yoxdursa (API testləri) boş 1x1 şəkil yazır — lazımsız ekran şəkilləri yığılmır.
public class DriverScreenshotWriter implements CustomScreenshotWriter {

    @Override
    public String takeScreenshot() {
        String fileName = "screenshot-" + UUID.randomUUID() + ".png";
        Path dir = Paths.get(Config.get("gauge_screenshots_dir", ".gauge/screenshots"));
        try {
            Files.createDirectories(dir);
            Files.write(dir.resolve(fileName), capture());
        } catch (IOException e) {
            throw new IllegalStateException("Screenshot yazıla bilmədi", e);
        }
        return fileName;
    }

    private byte[] capture() throws IOException {
        WebDriver driver = DriverManager.getDriver();
        if (driver instanceof TakesScreenshot) {
            try {
                return ((TakesScreenshot) driver).getScreenshotAs(OutputType.BYTES);
            } catch (RuntimeException e) {
                System.out.println("Driver screenshot alınmadı: " + e.getMessage());
            }
        }
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        ImageIO.write(new BufferedImage(1, 1, BufferedImage.TYPE_INT_ARGB), "png", out);
        return out.toByteArray();
    }
}
