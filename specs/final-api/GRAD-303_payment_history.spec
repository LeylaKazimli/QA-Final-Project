# GRAD-303 — Ödəniş tarixçəsi (GET /bill-payments)

Bu spec öz təmiz sandbox-ında işləyir (login-user1-hist.json), login keşlidir (spec üçün 1 dəfə).

D2 dataseti (Test Scope sheet-indəki paylanma ilə eyni): cəmi 21 ödəniş
  Kart A (1000 AZN): citynet 9 · azerisiq 4 · azercell 4  → 17 ödəniş
  Kart B (100 AZN):  azerisiq 1 · azercell 1 · aztelekom 2 → 4 ödəniş
  Təchizatçı üzrə: citynet 9 · azerisiq 5 · azercell 5 · aztelekom 2
Sandbox təmiz olduğu üçün qəbz nömrələri RCP-<tarix>-000001 … 000021 olur.

D2 birinci ssenaridə ("Hazırlıq") BİR DƏFƏ yaradılır, kart id-ləri bütün run üçün
yadda saxlanılır (d2KartA, d2KartB). Kartları hər ssenaridə yenidən yaratmaq olmaz:
3 kart limiti dolar və ödəniş sayı dəyişər. Gauge spec daxilində ssenariləri yuxarıdan
aşağı ardıcıl icra edir, ona görə hazırlıq ssenarisi həmişə birinci işləyir.

Manual qalan TC-lər (Excel-ə uyğun): TC-HIST-010, 012, 017, 018, 020.

* "/auth/login" ünvanına "login-user1-hist.json" ile login ol ve "token" tokenini yadda saxla

## Hazırlıq: D2 datasetinin (21 ödəniş) yaradılması
tags: api, regression, GRAD-303, setup

* "Tarixce A" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "d2KartA" global deyişenine "${cardId}" deyerini ver
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "5" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "azerisiq" təchizatçısına "1234567890" nömrəsi ilə "1" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "5" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "azercell" təchizatçısına "501234567" nömrəsi ilə "1" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "5" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "azerisiq" təchizatçısına "1234567890" nömrəsi ilə "1" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "5" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "azercell" təchizatçısına "501234567" nömrəsi ilə "1" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "5" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "azerisiq" təchizatçısına "1234567890" nömrəsi ilə "1" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "5" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "azercell" təchizatçısına "501234567" nömrəsi ilə "1" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "5" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "azerisiq" təchizatçısına "1234567890" nömrəsi ilə "1" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "5" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "azercell" təchizatçısına "501234567" nömrəsi ilə "1" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "5" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "Tarixce B" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "d2KartB" global deyişenine "${cardId}" deyerini ver
* "azerisiq" təchizatçısına "1234567890" nömrəsi ilə "1" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "azercell" təchizatçısına "501234567" nömrəsi ilə "1" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "aztelekom" təchizatçısına "1234567" nömrəsi ilə "2" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "aztelekom" təchizatçısına "1234567" nömrəsi ilə "2" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* Json cavabında "receiptNo" deyeri "^RCP-[0-9]{8}-000021$" regex-ine uyğun olmalıdır

## TC-HIST-001 Parametrsiz sorğuda ilk 10 ödənişin ən yenidən köhnəyə qaytarılması
tags: api, regression, GRAD-303, positive

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabını cedvel ile yoxla
   |path      |value|
   |----------|-----|
   |page      |1    |
   |limit     |10   |
   |total     |21   |
   |totalPages|3    |
* Json cavabında "items" massivinin ölçüsü "10" olmalıdır
* Json cavabında "items[0].receiptNo" deyeri "^RCP-[0-9]{8}-000021$" regex-ine uyğun olmalıdır
* Json cavabında "items[9].receiptNo" deyeri "^RCP-[0-9]{8}-000012$" regex-ine uyğun olmalıdır
* Json cavabında "items.createdAt" siyahısı azalan sırada olmalıdır

## TC-HIST-002 İkinci səhifədə növbəti 10 ödənişin təkrarsız qaytarılması
tags: api, regression, GRAD-303, positive

Səhifə 1: 000021 … 000012, səhifə 2: 000011 … 000002 → kəsişmə yoxdur.

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "page" = "2"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "page" deyeri "2" beraberdir
* Json cavabında "totalPages" deyeri "3" beraberdir
* Json cavabında "items" massivinin ölçüsü "10" olmalıdır
* Json cavabında "items[0].receiptNo" deyeri "^RCP-[0-9]{8}-000011$" regex-ine uyğun olmalıdır
* Json cavabında "items[9].receiptNo" deyeri "^RCP-[0-9]{8}-000002$" regex-ine uyğun olmalıdır

## TC-HIST-003 Mövcud olmayan səhifə (page=4) üçün xəta yox, boş siyahının qaytarılması
tags: api, regression, GRAD-303, positive

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "page" = "4"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "21" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır

## TC-HIST-004 Bütün səhifələr birləşdikdə ödənişlərin təkrarsız və ardıcıl olması (limit=5)
tags: api, regression, GRAD-303, positive

Hər səhifənin ilk və son qəbz nömrəsi yoxlanılır: 21→17, 16→12, 11→7, 6→2, 1.
Bir səhifənin sonu ilə növbətinin əvvəli arasında boşluq və təkrar olmadığı belə sübut olunur.

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "limit" = "5"
* Query parametri elave et "page" = "1"
* "GET" sorğusu gönder "/bill-payments"
* Json cavabında "items" massivinin ölçüsü "5" olmalıdır
* Json cavabında "items[0].receiptNo" deyeri "^RCP-[0-9]{8}-000021$" regex-ine uyğun olmalıdır
* Json cavabında "items[4].receiptNo" deyeri "^RCP-[0-9]{8}-000017$" regex-ine uyğun olmalıdır
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "limit" = "5"
* Query parametri elave et "page" = "2"
* "GET" sorğusu gönder "/bill-payments"
* Json cavabında "items" massivinin ölçüsü "5" olmalıdır
* Json cavabında "items[0].receiptNo" deyeri "^RCP-[0-9]{8}-000016$" regex-ine uyğun olmalıdır
* Json cavabında "items[4].receiptNo" deyeri "^RCP-[0-9]{8}-000012$" regex-ine uyğun olmalıdır
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "limit" = "5"
* Query parametri elave et "page" = "3"
* "GET" sorğusu gönder "/bill-payments"
* Json cavabında "items" massivinin ölçüsü "5" olmalıdır
* Json cavabında "items[0].receiptNo" deyeri "^RCP-[0-9]{8}-000011$" regex-ine uyğun olmalıdır
* Json cavabında "items[4].receiptNo" deyeri "^RCP-[0-9]{8}-000007$" regex-ine uyğun olmalıdır
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "limit" = "5"
* Query parametri elave et "page" = "4"
* "GET" sorğusu gönder "/bill-payments"
* Json cavabında "items" massivinin ölçüsü "5" olmalıdır
* Json cavabında "items[0].receiptNo" deyeri "^RCP-[0-9]{8}-000006$" regex-ine uyğun olmalıdır
* Json cavabında "items[4].receiptNo" deyeri "^RCP-[0-9]{8}-000002$" regex-ine uyğun olmalıdır
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "limit" = "5"
* Query parametri elave et "page" = "5"
* "GET" sorğusu gönder "/bill-payments"
* Json cavabında "items" massivinin ölçüsü "1" olmalıdır
* Json cavabında "items[0].receiptNo" deyeri "^RCP-[0-9]{8}-000001$" regex-ine uyğun olmalıdır

## TC-HIST-005 Səhifədə 1 element (limit=1, BVA: min) ilə tarixçənin qaytarılması
tags: api, regression, GRAD-303, positive, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "limit" = "1"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü "1" olmalıdır
* Json cavabında "totalPages" deyeri "21" beraberdir

## TC-HIST-006 Səhifədə 50 element (limit=50, BVA: max) ilə tarixçənin qaytarılması
tags: api, regression, GRAD-303, positive, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "limit" = "50"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü "21" olmalıdır
* Json cavabında "totalPages" deyeri "1" beraberdir
* Json cavabında "items.id" siyahısındakı deyerler unikal olmalıdır
* Json cavabında "items.receiptNo" siyahısı azalan sırada olmalıdır

## TC-HIST-007 limit=0 ilə sorğunun rədd edilməsi (BVA: min-1)
tags: api, regression, GRAD-303, negative, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "limit" = "0"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "limit" olmalıdır

## TC-HIST-008 limit=51 ilə sorğunun rədd edilməsi (BVA: max+1)
tags: api, regression, GRAD-303, negative, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "limit" = "51"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "limit" olmalıdır

## TC-HIST-009 page=0 ilə sorğunun rədd edilməsi (BVA: min-1)
tags: api, regression, GRAD-303, negative, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "page" = "0"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "page" olmalıdır

## TC-HIST-011 Səhifə nömrəsi rəqəm olmadıqda (page=abc) sorğunun rədd edilməsi
tags: api, regression, GRAD-303, negative

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "page" = "abc"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir

## TC-HIST-013 Tarixçənin təchizatçıya (citynet) görə filtrlənməsi
tags: api, regression, GRAD-303, positive

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "billerId" = "citynet"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "9" beraberdir
* Json cavabında "items" massivinin ölçüsü "9" olmalıdır
* Json cavabında "items.billerId" siyahısındakı bütün deyerler "citynet" olmalıdır

## TC-HIST-014 Filtr və səhifələmə birlikdə: total-un ümumi sayı göstərməsi (səhifədəki sayı yox)
tags: api, regression, GRAD-303, positive

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "billerId" = "citynet"
* Query parametri elave et "limit" = "5"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü "5" olmalıdır
* Json cavabında "total" deyeri "9" beraberdir
* Json cavabında "totalPages" deyeri "2" beraberdir
* Json cavabında "items.billerId" siyahısındakı bütün deyerler "citynet" olmalıdır

## TC-HIST-015 Tarixçənin karta (cardId) görə filtrlənməsi
tags: api, regression, GRAD-303, positive

Kart A-nın ödənişləri: citynet 9 · azerisiq 4 · azercell 4, aztelekom YOXDUR (aztelekom yalnız kart B-dədir).
Nəticədə bu paylanma görünməli və bir dənə də aztelekom ödənişi olmamalıdır.

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "cardId" = "${d2KartA}"
* Query parametri elave et "limit" = "50"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "17" beraberdir
* Json cavabında "items" massivinin ölçüsü "17" olmalıdır
* Json cavabında "items.findAll { it.billerId == 'citynet' }.size()" deyeri "9" beraberdir
* Json cavabında "items.findAll { it.billerId == 'azerisiq' }.size()" deyeri "4" beraberdir
* Json cavabında "items.findAll { it.billerId == 'azercell' }.size()" deyeri "4" beraberdir
* Json cavabında "items.findAll { it.billerId == 'aztelekom' }.size()" deyeri "0" beraberdir

## TC-HIST-016 Eyni başlanğıc və son tarixlə (from = to = bu gün) günün bütün ödənişlərinin qaytarılması
tags: api, regression, GRAD-303, positive, bva

D2 bu gün yaradıldığı üçün from = to = ${today} hamısını qaytarmalıdır (sərhəd tarix daxildir).

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "from" = "${today}"
* Query parametri elave et "to" = "${today}"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "21" beraberdir

## TC-HIST-019 Mövcud olmayan ay (2026-13-01) ilə sorğunun rədd edilməsi
tags: api, regression, GRAD-303, negative

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "from" = "2026-13-01"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "from" olmalıdır

## TC-HIST-021 Səhv tarix formatı (01-10-2026) ilə sorğunun rədd edilməsi
tags: api, regression, GRAD-303, negative

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "from" = "01-10-2026"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir

## TC-HIST-022 Başlanğıc tarixi son tarixdən böyük olduqda sorğunun rədd edilməsi
tags: api, regression, GRAD-303, negative

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "from" = "2026-10-02"
* Query parametri elave et "to" = "2026-10-01"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir

## TC-HIST-023 Başqa istifadəçinin ödəniş tarixçəsinin görünməməsi
tags: api, regression, GRAD-303, negative, security

* "/auth/login" ünvanına "login-user2-hist.json" ile login ol ve "token" tokenini yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır

## TC-HIST-024 Token olmadan ödəniş tarixçəsinə baxmaq cəhdinin rədd edilməsi
tags: api, regression, GRAD-303, negative, auth

* Yeni API sorğusu hazırla
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "401" olmalıdır
* Json cavabında "error" açarı mövcud olmalıdır
* Json cavabında "items" açarı olmamalıdır
