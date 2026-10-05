# GRAD-102 — Alıcılar siyahısı: axtarış, filtr, sıralama (GET /beneficiaries)

Bu spec öz sandbox-ında işləyir (login-user1-benl.json), login keşlidir (spec üçün 1 dəfə).

D1 dataseti (Test Scope sheet-i) aşağıdakı kontekst addımlarında hazırlanır.
Kontekst addımları hər ssenaridən əvvəl işləyir: birinci ssenaridə 5 alıcı yaradılır (201),
sonrakılarda server "artıq var" deyir (409) və data dəyişmir. Beləliklə hər ssenari
D1-in mövcudluğuna zəmanətlə başlayır, ssenarilərin icra sırasından asılılıq yoxdur.

Manual qalan TC-lər (Excel-ə uyğun): TC-BENL-003, TC-BENL-015, TC-BENL-016, TC-BENL-018.

* "/auth/login" ünvanına "login-user1-benl.json" ile login ol ve "token" tokenini yadda saxla
* D1 alıcısı mövcud olsun: "Nigar Əliyeva" "AZ77AIIB40060019440123456789" "AZN" ləqəb "Anam"
* D1 alıcısı mövcud olsun: "Cavid Həsənov" "AZ12AIIB40060019440100000101" "USD" ləqəb "Dayı"
* D1 alıcısı mövcud olsun: "Çingiz Quliyev" "AZ12AIIB40060019440100000102" "EUR" ləqəbsiz
* D1 alıcısı mövcud olsun: "Elvin Məmmədov" "AZ12AIIB40060019440100000103" "USD" ləqəb "Qardaş"
* D1 alıcısı mövcud olsun: "Əli Rzayev" "AZ12AIIB40060019440100000104" "AZN" ləqəbsiz

## TC-BENL-001 Parametrsiz sorğuda bütün alıcıların ən yenidən köhnəyə qaytarılması
tags: api, regression, GRAD-102, positive

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "5" beraberdir
* Json cavabında "items" massivinin ölçüsü "5" olmalıdır
* Json cavabını cedvel ile yoxla
   |path             |value         |
   |-----------------|--------------|
   |items[0].fullName|Əli Rzayev    |
   |items[1].fullName|Elvin Məmmədov|
   |items[2].fullName|Çingiz Quliyev|
   |items[3].fullName|Cavid Həsənov |
   |items[4].fullName|Nigar Əliyeva |

## TC-BENL-002 Alıcıların adına görə Azərbaycan əlifbası ilə artan sıralanması
tags: api, regression, GRAD-102, positive

Sıra hərf-hərf yoxlanılır: C → Ç → E → Ə → N (Azərbaycan əlifbası).

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "sort" = "fullName"
* Query parametri elave et "order" = "asc"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü "5" olmalıdır
* Json cavabını cedvel ile yoxla
   |path             |value         |
   |-----------------|--------------|
   |items[0].fullName|Cavid Həsənov |
   |items[1].fullName|Çingiz Quliyev|
   |items[2].fullName|Elvin Məmmədov|
   |items[3].fullName|Əli Rzayev    |
   |items[4].fullName|Nigar Əliyeva |

## TC-BENL-004 Alıcıların valyutaya (USD) görə filtrlənməsi
tags: api, regression, GRAD-102, positive

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "currency" = "USD"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "items" massivinin ölçüsü "2" olmalıdır
* Json cavabında "items.currency" siyahısındakı bütün deyerler "USD" olmalıdır
* Json cavabında "items.fullName" deyerinde "Cavid Həsənov" olmalıdır
* Json cavabında "items.fullName" deyerinde "Elvin Məmmədov" olmalıdır

## TC-BENL-005 Böyük nöqtəli İ ilə (NİGAR) axtarışda alıcının tapılması
tags: api, regression, GRAD-102, positive

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "NİGAR"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items[0].fullName" deyeri "Nigar Əliyeva" beraberdir

## TC-BENL-006 Nöqtəsiz I ilə (NIGAR) axtarışda alıcının tapılması
tags: api, regression, GRAD-102, positive

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "NIGAR"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items[0].fullName" deyeri "Nigar Əliyeva" beraberdir

## TC-BENL-007 Adın bir hissəsi ilə kiçik hərflə (nig) axtarışda alıcının tapılması
tags: api, regression, GRAD-102, positive

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "nig"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items[0].fullName" deyeri "Nigar Əliyeva" beraberdir

## TC-BENL-008 Ləqəbin bir hissəsi ilə (qard) axtarışda alıcının tapılması
tags: api, regression, GRAD-102, positive

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "qard"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items[0].fullName" deyeri "Elvin Məmmədov" beraberdir
* Json cavabında "items[0].nickname" deyeri "Qardaş" beraberdir

## TC-BENL-009 Axtarış sözü 1 simvol olduqda sorğunun rədd edilməsi (BVA: min-1)
tags: api, regression, GRAD-102, negative, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "a"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "1" olmalıdır
* Json cavabında "details[0].field" deyeri "q" beraberdir

## TC-BENL-010 Axtarış sözü 2 simvol olduqda axtarışın işləməsi (BVA: min)
tags: api, regression, GRAD-102, positive, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "ni"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items[0].fullName" deyeri "Nigar Əliyeva" beraberdir

## TC-BENL-011 Heç nə tapılmadıqda xəta yox, boş siyahının qaytarılması
tags: api, regression, GRAD-102, positive

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "zzzz"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır

## TC-BENL-012 Valyuta və axtarış birlikdə: hər iki şərtə uyğun alıcının qaytarılması
tags: api, regression, GRAD-102, positive

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "currency" = "USD"
* Query parametri elave et "q" = "elv"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items[0].fullName" deyeri "Elvin Məmmədov" beraberdir
* Json cavabında "items[0].currency" deyeri "USD" beraberdir

## TC-BENL-013 Valyuta və axtarış birlikdə: AND məntiqi (uyğun olmayan alıcı qaytarılmır)
tags: api, regression, GRAD-102, negative

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "currency" = "AZN"
* Query parametri elave et "q" = "elv"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır

## TC-BENL-014 Dəstəklənməyən valyuta (GBP) filtri ilə sorğunun rədd edilməsi
tags: api, regression, GRAD-102, negative

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "currency" = "GBP"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "1" olmalıdır
* Json cavabında "details[0].field" deyeri "currency" beraberdir

## TC-BENL-017 Token olmadan alıcılar siyahısına baxmaq cəhdinin rədd edilməsi
tags: api, regression, GRAD-102, negative, auth

* Yeni API sorğusu hazırla
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "401" olmalıdır
* Json cavabında "error" açarı mövcud olmalıdır
* Json cavabında "items" açarı olmamalıdır
