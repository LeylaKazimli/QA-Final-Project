# Gauge Test Automation Framework (Web UI + API)

Bitirmə işi üçün hazır test avtomatlaşdırma framework-ü. Öz layihənizi (istənilən sayt və ya REST API) seçin,
konfiqurasiyanı dəyişin və testləri **Java kodu yazmadan**, hazır step-lərlə `.spec` fayllarında yazın.

> 🇬🇧 English version (arxitektura diaqramları ilə): [README.md](README.md)

| Texnologiya | Məqsəd |
|---|---|
| [Gauge](https://gauge.org) | Test ssenariləri (Markdown `.spec`), HTML hesabat |
| Selenium 4 + WebDriverManager | Web UI (Chrome, Firefox, Edge, Safari, headless) |
| RestAssured 5 + JSON Schema Validator | REST API |
| Appium | Android (ayrıca modul, `MobileImp`) |
| Maven, Java 11+ | Build |

---

## 1. Tez başlanğıc

```bash
# Quraşdırma (bir dəfə)
brew install gauge maven          # Windows: choco install gauge maven
gauge install java && gauge install html-report

# Bütün spec-lər
mvn test

# Tək qovluq / tək fayl
mvn test -Dgauge.specs.dir=specs/api-testing
mvn test -Dgauge.specs.dir=specs/ui-testing/autoLabTest.spec

# Tag ilə filtr
mvn test -Dtags="smoke"
mvn test -Dtags="api & !slow"

# CI mühiti (headless brauzer): env/default + env/ci
mvn test -Denv=ci

# Parallel (hər spec ayrı prosesdə)
mvn test -Pparallel
```

> ⚠️ Testləri **yalnız `mvn test`** ilə işlədin. Birbaşa `gauge run` Maven asılılıqlarını görmür və kompilyasiya xətası verir.

Hesabat: `reports/html-report/index.html`. Hər API sorğusu/cavabı və uğursuz UI step-in brauzer screenshot-u orada görünür.

Framework-ün öz testləri (hər step-in işlək nümunəsi):

```bash
./framework-tests/run-selftest.sh        # hamısı
./framework-tests/run-selftest.sh ui     # yalnız UI (lokal playground səhifəsi)
./framework-tests/run-selftest.sh api    # yalnız API (dummyjson.com, postman-echo.com)
```

---

## 2. Öz layihənizə uyğunlaşdırmaq (addım-addım)

1. **`env/default/app.properties`**: `ui_base_url` və `api_base_url` dəyərlərini öz layihənizin ünvanı ilə əvəz edin.
2. **Locator-lar**: `src/test/resources/locator/` qovluğunda hər səhifə üçün bir JSON faylı yaradın (məs. `loginPage.json`).
3. **Request body-lər**: `src/test/resources/body/` qovluğuna JSON faylları qoyun.
4. **Login**: `specs/.../*.cpt` concept faylında login-i bir dəfə təyin edin (bax: [Autentifikasiya](#autentifikasiya)).
5. **Spec yazın**: `specs/` altında `.spec` faylları. Nümunələr: `framework-tests/*.spec`.

---

## 3. Qovluq strukturu

```
env/
  default/app.properties        ← layihə konfiqurasiyası (URL-lər, brauzer, timeout, retry)
  ci/app.properties             ← CI üçün override (headless)
specs/                          ← SİZİN testləriniz (.spec, .cpt)
framework-tests/                ← framework self-test-ləri + UI playground (nümunə kimi oxuyun)
src/test/java/
  imp/        ← @Step sinifləri (spec cümləsi → Java metodu). Yalnız helper-ləri çağırır.
  helper/     ← bütün məntiq: BaseHelper, Click/Type/Scroll/Verify/Browser, Api/ApiAssert/Auth
  utils/      ← Config, DriverManager, WebDriverFactory, LocatorReader, ScenarioContext
  hooks/      ← Hooks (ssenari təmizliyi), DriverScreenshotWriter
src/test/resources/
  locator/    ← UI locator JSON faylları (hamısı avtomatik yüklənir)
  body/       ← API request body-ləri (${dəyişən} dəstəkləyir)
  expected/   ← gözlənilən cavab JSON-ları (matcher-lərlə)
  schema/     ← JSON Schema faylları
  files/      ← yüklənəcək fayllar (UI upload, API multipart)
```

### Arxitektura

```
 .spec  ──►  imp/*Imp (@Step)  ──►  helper/*Helper  ──►  Selenium / RestAssured
                                        │
                     utils: Config · DriverManager (ThreadLocal) · LocatorReader · ScenarioContext (${var})
                     hooks: @BeforeScenario/@AfterScenario təmizlik · screenshot
```

- **Hər ssenari təmizdir**: API sorğusu, cavab və dəyişənlər ssenari bitəndə sıfırlanır. Brauzer avtomatik bağlanır (test ortada düşsə belə).
- **Thread-safe**: driver və API state `ThreadLocal`-dadır.
- **Flaky-ə qarşı**: bütün UI yoxlamaları `explicit_wait_seconds` müddətində təkrar cəhd edir. API 429/503 cavablarında avtomatik retry edir.
- **Aydın xətalar**: `"PG Title" mətni gözlənilən deyil. Gözlənilən: "X", faktiki: "Y"`.

---

## 4. Konfiqurasiya (`env/default/app.properties`)

| Açar | Default | İzah |
|---|---|---|
| `ui_base_url` | — | Nisbi ünvanlar (`"/login"`) buna birləşir |
| `browser` | `chrome` | `chrome`, `firefox`, `edge`, `safari`, `chrome-headless`... |
| `headless` | `false` | `true` → brauzer pəncərəsiz |
| `explicit_wait_seconds` | `10` | Element gözləmələrinin default müddəti |
| `keep_browser_open` | `false` | `true` → ssenari bitəndə brauzer bağlanmır (debug) |
| `api_base_url` | — | Nisbi endpoint-lər (`"/users"`) buna birləşir |
| `api_timeout_seconds` | `30` | Server cavab verməsə sorğu bu müddətdən sonra xəta verir |
| `api_max_retries` | `2` | 429/503 cavabında təkrar cəhd sayı |
| `api_retry_max_wait_seconds` | `10` | Bir retry üçün maksimum gözləmə |
| `api_log_all` | `true` | Sorğu/cavabı konsola tam yaz |
| `api_relaxed_https` | `false` | Self-signed sertifikatlı serverlər üçün |

Spec daxilində oxumaq: `${env.api_base_url}`.
Bir dəfəlik override (fayl dəyişmədən): `headless=true browser=firefox mvn test`.

---

## 5. Dəyişənlər: `${ad}`

İstənilən step parametrində, body faylında, expected JSON-da və locator adında işləyir.

| İfadə | Nəticə |
|---|---|
| `${token}`, `${userId}` | Əvvəl saxlanılmış dəyər |
| `${random.email}` | `test_1a2b3c4d@test.com` (hər dəfə yeni) |
| `${random.uuid}`, `${random.number}`, `${random.name}`, `${random.phone}` | Təsadüfi dəyərlər |
| `${timestamp}`, `${today}` | `1790622519782`, `2026-09-29` |
| `${env.açar}` | `app.properties`-dən dəyər |
| `${projectDir}` | Layihə qovluğunun tam yolu |

Dəyər saxlamaq: `Json cavabında "id" deyerini "userId" olaraq yadda saxla` → sonra `"/users/${userId}"`.
Ssenari dəyişənləri ssenari bitəndə silinir. "global" / "bütün testler üçün" variantları bütün suite boyu qalır.

---

## 6. Locator-lar

`src/test/resources/locator/*.json`: qovluqdakı bütün fayllar bir dəfə yüklənir. Eyni ad iki faylda olsa xəta verir.

```json
{
  "Login Email Input":  { "locatorType": "ID",          "locatorValue": "email" },
  "Login Button":       { "locatorType": "CSS",         "locatorValue": "button[type='submit']" },
  "Error Message":      { "locatorType": "XPATH",       "locatorValue": "//div[contains(@class,'error')]" },
  "Product Cards":      { "locatorType": "CLASS_NAME",  "locatorValue": "product-card" }
}
```

Tiplər: `ID`, `NAME`, `CSS` (`CSS_SELECTOR`), `XPATH`, `CLASS_NAME`, `TAG_NAME`, `LINK_TEXT`, `PARTIAL_LINK_TEXT`.

JSON yazmadan **inline locator** də işlətmək olar: `"css=#login"`, `"id=email"`, `"xpath=//button[text()='Giriş']"`, `"name=q"`.

---

## 7. Web UI step-ləri

### Brauzer və naviqasiya
| Step | Qeyd |
|---|---|
| `Brauzeri aç ve keçid et "/login"` | Brauzer `app.properties`-dən |
| `"chrome" brauzeri aç ve keçid et "https://site.com"` | Brauzeri açıq seçmək |
| `"/products" adresine keçid et` | Açıq brauzerdə keçid |
| `Sehifeni yenile` · `Evvelki sehifeye qayıt` · `Növbeti sehifeye keç` | |
| `Pencere ölçüsünü "375" x "812" et` | Mobil görünüş testi |
| `Brauzeri bağla` | Məcburi deyil, hook avtomatik bağlayır |

### Klik və mouse
| Step |
|---|
| `"Login Button" elementine klik et` |
| `"Giriş" metnli elemente klik et` (locator-suz, görünən mətnə görə) |
| `"Menu Items" siyahısında "Profil" metnli elemente klik et` |
| `"Product Cards" siyahısında "2" nömreli elemente klik et` |
| `"Row" elementine iki defe klik et` · `"Row" elementine sağ klik et` |
| `"Menu" elementinin üzerine gel` (hover) |
| `"Card" elementini "Basket" elementinin üzerine sürükle` |
| `"Hidden Button" elementine JavaScript ile klik et` |
| `"Cookie Accept" elementi "3" saniye içinde görünerse klik et` (popup/banner üçün) |

### Form
| Step |
|---|
| `"Email Input" elementine "user@test.com" yaz` (əvvəlcə təmizləyir) |
| `"Search Input" elementine "iphone" yaz ve Enter düymesine bas` · `... Tab düymesine bas` · `... Shift düymesine bas` |
| `"Email Input" elementini temizle` |
| `"Search Input" elementinde "ARROW_DOWN" düymesine bas` · `Sehifede "ESCAPE" düymesine bas` |
| `"Country" dropdown-undan "Azərbaycan" metnini seç` · `... "az" deyerini seç` · `... "2" indeksli seçimi seç` |
| `"Terms" checkbox-unu işaretle` · `"Terms" checkbox-unun işaretini kaldır` |
| `"Avatar Input" elementine "photo.png" faylını yükle` (`resources/files/`-dan) |

### Gözləmə
| Step |
|---|
| `"Dashboard" görsensin deye maksimum "10" saniye gözle` |
| `"Loader" yox olana qeder maksimum "15" saniye gözle` |
| `"Submit" kliklene bilene qeder gözle` · `Sehifenin tam yüklenmesini gözle` |
| `"2" saniye gözle` (son çarə, mümkün qədər işlətməyin) |

### Yoxlamalar
| Step |
|---|
| `"Title" elementinin metni "Xoş gəldiniz" olmalıdır` · `"Title" elementin içinde "Xoş" yazısı var` |
| `Sehifede "Sifariş qəbul edildi" yazısı olmalıdır` |
| `"Modal" görünür olmalıdır` · `"Modal" görünmemelidir` · `"Item" sehifede mövcud olmamalıdır` |
| `"Submit" aktiv olmalıdır` · `"Submit" deaktiv olmalıdır` |
| `"Terms" seçilmiş olmalıdır` · `"Terms" seçilmemiş olmalıdır` |
| `"Email Input" input deyeri "a@b.com" olmalıdır` |
| `"Link" elementinin "href" atributu "/about" olmalıdır` · `... "class" atributunda "active" olmalıdır` |
| `"Product Cards" elementlerinin sayı "12" olmalıdır` · `... sayı en az "1" olmalıdır` |
| `Sehife başlığı "Home" olmalıdır` · `Sehife başlığında "Home" olmalıdır` |
| `URL "/dashboard" içermelidir` · `URL "/dashboard" olmalıdır` |

### Dəyər saxlamaq
| Step |
|---|
| `"Order Number" elementinin metnini "orderNo" olaraq yadda saxla` |
| `"Link" elementinin "href" atributunu "link" olaraq yadda saxla` |

### Scroll
| Step |
|---|
| `"Footer" elementine scroll et` · `"Footer" elementine scroll et ve klik et` |
| `Sehifenin aşağısına scroll et` · `Sehifenin yuxarısına scroll et` |
| `"500" piksel vertical scroll et` · `"300" piksel horizontal scroll et` |

### Tab, iframe, alert, cookie, storage, JS
| Step |
|---|
| `Yeni açılan taba keç` · `"2" nömreli taba keç` · `Cari tabı bağla ve esas taba qayıt` · `Yeni tabda "/help" aç` |
| `"Payment Frame" iframe-ine keç` · `Iframe-den esas sehifeye qayıt` |
| `Alert-i qebul et` · `Alert-i legv et` · `Alert metninde "Əminsiniz" olmalıdır` · `Alert-e "Anar" yaz ve qebul et` |
| `Cookie elave et "session" = "abc"` · `"session" cookie-si mövcud olmalıdır` · `Bütün cookie-leri sil` |
| `LocalStorage-e yaz "lang" = "az"` · `LocalStorage ve SessionStorage-i temizle` |
| `JavaScript icra et "window.scrollTo(0, 0)"` · `Ekran görüntüsü çek` |

---

## 8. API step-ləri

### Sorğunun qurulması
| Step | Qeyd |
|---|---|
| `Set base Url to "https://api.site.com"` · `API base URL "..." olsun` | Default: `api_base_url` |
| `Initalize request specification` · `Yeni API sorğusu hazırla` | Təmiz sorğu |
| `Add Endpoint "/users/${userId}"` · `Endpoint "/users/{id}" olsun` | |
| `Path parametri elave et "id" = "5"` | `{id}` üçün |
| `Query parametri elave et "page" = "2"` | `?page=2` |
| `Header elave et "X-Lang" = "az"` · `Add as a header "Content-Type" = "application/json"` | |
| `Headerleri elave et <cədvəl>` | `\|key\|value\|` cədvəli |
| `Form parametri elave et "username" = "anar"` | `x-www-form-urlencoded` |
| `Multipart fayl elave et "file" = "photo.png"` | `resources/files/`-dan |

### Body
| Step | Qeyd |
|---|---|
| `Body olaraq "user.json" faylını elave et` · `Add body as file resource "user.json"` | `resources/body/`, `${var}` işləyir |
| `Body olaraq "{\"name\":\"Anar\"}" metnini elave et` · `Add body as text "..."` | |
| `Body-ni cedvelden qur <cədvəl>` | `address.city` → iç-içə obyekt; `12`→rəqəm, `true`→boolean |

Body şablonu nümunəsi (`body/new-user.json`):
```json
{ "email": "${random.email}", "name": "${random.name}", "role": "user" }
```

### Göndərmə
| Step |
|---|
| `"POST" sorğusu gönder` · `"GET" sorğusu gönder "/users/1"` (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS) |
| `Get request and display respons` · `Post ...` · `Put ...` · `Patch ...` · `Delete request and display response` |
| `API e GET request gönder "/users"` (header/body-siz tez GET) |
| `Cavabı çap et` |

### Autentifikasiya
| Step | Qeyd |
|---|---|
| `"/auth/login" ünvanına "login.json" ile login ol ve "token" tokenini yadda saxla` | Token **bütün suite üçün keşlənir** (1 login sorğusu). `${token}` = `Bearer ...`, `${rawToken}` = token |
| `"/auth/login" ünvanına "login.json" ile yeni sessiya açaraq login ol ve "data.accessToken" tokenini yadda saxla` | Keşsiz |
| `Authorization header-ine tokeni elave et` · `Add as a header "Authorization" = "token"` | |
| `Bearer token elave et "${rawToken}"` · `Basic auth elave et istifadeci "u" şifre "p"` · `API key header elave et "x-api-key" = "..."` | |
| `Token keşini temizle` | Logout testlərindən sonra |

Tövsiyə olunan concept (`specs/login.cpt`):
```markdown
# Admin kimi daxil ol
* "/auth/login" ünvanına "login.json" ile login ol ve "token" tokenini yadda saxla
```
> Hər ssenaridə real login sorğusu göndərmək API-nin rate limit-inə (429) düşməyə səbəb olur. Keşli step-i işlədin.

### Cavab yoxlamaları
JSON path sintaksisi (RestAssured GPath): `id`, `user.email`, `data[0].name`, `items.size()`, `data.findAll { it.price > 100 }.size()`, `items.sum { it.qty * it.price }`.

| Step |
|---|
| `Status kodunun "200" olmalıdır` · `Status kodu "200" ile "299" arasında olmalıdır` |
| `Json cavabında "email" deyeri "a@b.com" beraberdir` (rəqəm/boolean da: `"5"`, `"true"`) |
| `Json cavabında "status" deyeri "deleted" olmamalıdır` |
| `Json cavabında "name" deyerinde "Anar" olmalıdır` (mətn daxilində və ya massivdə element) |
| `Json cavabında "email" deyeri ".+@.+\..+" regex-ine uyğun olmalıdır` |
| `Json cavabında "price" deyeri ">" "0" olmalıdır` (`>` `>=` `<` `<=` `==` `!=`) |
| `Json cavabında "id" deyeri boş olmamalıdır` · `Json cavabında "deletedAt" deyeri null olmalıdır` |
| `Json cavabında "password" açarı olmamalıdır` · `Json cavabında "id" açarı mövcud olmalıdır` |
| `Json cavabında verilen "total" deyeri ededdir` · `Json cavabında "tags" deyerinin tipi "array" olmalıdır` (string, number, boolean, array, object, null) |
| `Json cavabında "data" massivinin ölçüsü "10" olmalıdır` · `... ölçüsü en az "1" olmalıdır` |
| `Json cavabında "data.status" siyahısındakı bütün deyerler "active" olmalıdır` (filter testi) |
| `Json cavabında "data.price" siyahısı artan sırada olmalıdır` · `... azalan sırada olmalıdır` (sort testi) |
| `Json cavabında "data.id" siyahısındakı deyerler unikal olmalıdır` |
| `Cavab body-sinde "success" olmalıdır` |
| `Header "Content-Type" movcud olmalıdır` · `Header "Content-Type" deyerinde "json" olmalıdır` |
| `Respons cavab müddeti "1500" milliSaniyeden az olmalıdır` |

### Bütün body-ni bir dəfəyə yoxlamaq
**1) Cədvəl:** bütün uyğunsuzluqlar birlikdə göstərilir.
```markdown
* Json cavabını cedvel ile yoxla
   |path            |value            |
   |----------------|-----------------|
   |id              |${userId}        |
   |email           |@regex:.+@.+     |
   |address.city    |Bakı             |
   |createdAt       |@notNull         |
```

**2) Gözlənilən JSON faylı** (`resources/expected/user.json`): faylda olan hər sahə cavabda olmalıdır, cavabdakı əlavə sahələr nəzərə alınmır.
```json
{
  "id": "@number",
  "email": "@regex:^[^@]+@[^@]+$",
  "role": "user",
  "tags": ["@string"],
  "address": { "city": "Bakı", "zip": "@notEmpty" },
  "createdAt": "@ignore"
}
```
`* Json cavabı "user.json" faylındakı gözlenilen JSON-a uyğun olmalıdır`

Matcher-lər: `@ignore` `@notNull` `@notEmpty` `@string` `@number` `@boolean` `@array` `@object` `@regex:...` `@contains:...`

**3) JSON Schema** (`resources/schema/user.schema.json`): `* Cavab "user.schema.json" JSON schema-sına uyğun olmalıdır`

**4) Request → response:** göndərilən dəyər geri qayıtdımı?
`* Json cavabında "name" deyeri "new-user.json" request body-sindeki "name" ile eyni olmalıdır`

### Dəyər saxlamaq və müqayisə
| Step |
|---|
| `Json cavabında "id" deyerini "userId" olaraq yadda saxla` · `Save value of "id" as "userId"` |
| `Json cavabında "id" deyerini "userId" olaraq bütün testler üçün yadda saxla` |
| `Header "Location" deyerini "location" olaraq yadda saxla` |
| `Json cavabında "id" deyeri "userId" ile eynidir` · `... "userId" ile ferqlidir` |

### Dəyişən step-ləri
| Step |
|---|
| `"email" deyişenine "${random.email}" deyerini ver` · `"env" global deyişenine "test" deyerini ver` |
| `"email" deyişeni "a@b.com" olmalıdır` · `"email" deyişeninin deyerini çap et` |

---

## 9. Nümunə: tam CRUD ssenarisi

```markdown
# İstifadəçi API

* Admin kimi daxil ol

## Yeni istifadəçi yaradılır, oxunur, yenilənir və silinir
tags: api, crud

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "new-user.json" faylını elave et
* "POST" sorğusu gönder "/users"
* Status kodunun "201" olmalıdır
* Json cavabı "user.json" faylındakı gözlenilen JSON-a uyğun olmalıdır
* Json cavabında "email" deyeri "new-user.json" request body-sindeki "email" ile eyni olmalıdır
* Json cavabında "id" deyerini "userId" olaraq yadda saxla

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/users/${userId}"
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "${userId}" beraberdir

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "DELETE" sorğusu gönder "/users/${userId}"
* Status kodu "200" ile "204" arasında olmalıdır
```

---

## 10. Yeni step əlavə etmək

1. Məntiqi uyğun `helper/*Helper` sinfinə metod kimi yazın (driver: `driver()`, element: `visible(name)`, `clickable(name)`, API: `ApiHelper.getInstance()`).
2. `imp/*Imp` sinfində `@Step("...")` ilə həmin metodu çağırın.
3. Step mətni bütün layihədə **unikal** olmalıdır.

```java
// helper/ClickHelper.java
public void clickTwiceWithPause(String elementName) { clickElement(elementName); clickElement(elementName); }

// imp/ClickElementImp.java
@Step("<element> elementine iki defe ardıcıl klik et")
public void clickTwice(String element) { clickTwiceWithPause(element); }
```

---

## 11. Tez-tez rast gəlinən xətalar

| Xəta | Həll |
|---|---|
| `package io.restassured does not exist` | `gauge run` yox, `mvn test` işlədin |
| `Locator tapılmadı: "X"` | Ad `locator/*.json`-dakı açarla hərfbəhərf eyni olmalıdır |
| `Aktiv brauzer/cihaz yoxdur` | Ssenarinin əvvəlində `Brauzeri aç ve keçid et ...` |
| `Hələ heç bir API sorğusu göndərilməyib` | Yoxlamadan əvvəl sorğu göndərin |
| `Dəyişən tapılmadı: ${x}` | Dəyişəni əvvəlcə saxlayın; ssenari dəyişənləri növbəti ssenariyə keçmir |
| `429 Too Many Requests` | Keşli login step-ini işlədin, `api_max_retries` artırın |
| `Nisbi ünvan üçün base URL təyin edilməyib` | `app.properties`-də `ui_base_url` / `api_base_url` |
