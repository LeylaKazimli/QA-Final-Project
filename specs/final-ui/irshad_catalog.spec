# irshad.az — Kateqoriya, filtrlər, sıralama, məhsul kartı və məhsul səhifəsi

Test mühiti: https://irshad.az
Excel: "UI Test Cases" vərəqi (TS-UI-01, TS-UI-03, TS-UI-05 … TS-UI-10)
Kateqoriya: Mobil telefonlar — https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar
İstinad məhsul A: iPhone Air 256 GB Cloud White. Qiymət yoxlamaları nisbidir (kart = məhsul səhifəsi, köhnə > cari, dil dəyişəndə eyni qiymət).
Yalnız BVA testləri (FLTP-002/003/004) və A kartını tapmaq üçün qiymət aralığı (2509–2510) P = 2509.99-a (11–13.10.2026) bağlıdır — TC-də olduğu kimi "P test zamanı qeyd edilir"; qiymət dəyişərsə bu rəqəmlər yenilənməlidir.
Qiymət sahələri onluq qəbul etmir (BUG-UI-015) — BVA testlərində TC-dəki qayda ilə tam ədəd sərhədlər işlədilir (P+1 / P−1 əvəzinə 2510 / 2509).
"... Kenar Qiymetler", "... Pozuntulari" lokatorları qaydanı pozan elementləri tapır — onların sayı 0 olmalıdır.
Yoxlamalar siyahının birinci hissəsinə (ilk yüklənən kartlara) aiddir. Hər ssenari yeni brauzer sessiyası ilə başlayır.
Qiymət sahəsi təmizlənəndə (clear) sayt dərhal ayrıca filtr sorğusu göndərir; növbəti dəyər yalnız URL-də boş parametr görünəndən sonra yazılır.
Filtr Tab (blur) ilə tətbiq olunur. Sayt köhnə filtr sorğusunu ləğv etmir: gec gələn köhnə cavab yeni nəticənin üstünə yazıla bilir
(URL düzgün, siyahı köhnə — BUG-UI-028). Ona görə filtr URL-də tam tətbiq olunandan sonra səhifə yenilənir və siyahı həmin URL üzrə
serverdən yüklənmiş vəziyyətdə yoxlanılır — nəticə sorğuların cavab ardıcıllığından asılı olmur (flaky deyil).

tags: ui, irshad, catalog

## TC-UI-HOME-010 Ana səhifədəki məhsul kartından məhsul səhifəsinə keçid

tags: home

* Brauzeri aç ve keçid et "https://irshad.az/az"
* Sehifenin tam yüklenmesini gözle
* "600" piksel vertical scroll et
* "Ana Sehife Ilk Mehsul Adi" elementinin metnini "kartAdi" olaraq yadda saxla
* "Ana Sehife Ilk Mehsul Adi" elementine klik et
* URL "/az/mehsullar/" içermelidir
* "PDP Basliq" elementinin metni "${kartAdi}" olmalıdır

## TC-UI-HOME-013 "Həftənin təklifi" blokunda endirim məbləğinin qiymətlərlə uyğunluğu

tags: home

* Brauzeri aç ve keçid et "https://irshad.az/az"
* Sehifede "Həftənin təklifi" yazısı olmalıdır
* "Heftenin Teklifi Bloklari" elementlerinin sayı en az "1" olmalıdır
* "Heftenin Teklifi Endirim Uygunsuzluqlari" elementlerinin sayı "0" olmalıdır
* "Heftenin Teklifi Kohne Qiymeti Boyuk Olmayan" elementlerinin sayı "0" olmalıdır
* "Heftenin Teklifi Natamam Bloklar" elementlerinin sayı "0" olmalıdır

## TC-UI-LANG-004 Məhsul səhifəsində dil dəyişəndə məhsulun və qiymətin eyni qalması

tags: language

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white"
* "PDP Cari Qiymet" elementinin metnini "pdpQiymeti" olaraq yadda saxla
* "Dil Secici" elementinin üzerine gel
* "Rus Dili Link" kliklene bilene qeder gözle
* "Rus Dili Link" elementine klik et
* URL "/ru/tovary/iphone-air-256-gb-cloud-white" içermelidir
* "PDP Basliq" elementinin metni "iPhone Air 256 GB Cloud White" olmalıdır
* "xpath=(//section[contains(@class,'product-view') and not(contains(@class,'d-none'))]//div[contains(@class,'price-info__buy-now') and not(ancestor::div[contains(@class,'product-view__fixed-bar__info')])]//p[contains(@class,'new-price')])[1][round(100*number(normalize-space(translate(.,'AZN','')))) = round(100*number(normalize-space(translate('${pdpQiymeti}','AZN',''))))]" elementlerinin sayı "1" olmalıdır

## TC-UI-LANG-005 Seçilmiş dilin başqa səhifəyə keçəndə saxlanması

tags: language

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Dil Secici" elementinin üzerine gel
* "Rus Dili Link" kliklene bilene qeder gözle
* "Rus Dili Link" elementine klik et
* URL "https://irshad.az/ru" içermelidir
* "Kataloq Button" elementine klik et
* "RU Menyu Telefon Kateqoriyasi" görsensin deye maksimum "5" saniye gözle
* "RU Menyu Telefon Kateqoriyasi" elementinin üzerine gel
* "RU Menyu Mobil telefonlar" kliklene bilene qeder gözle
* "RU Menyu Mobil telefonlar" elementine klik et
* URL "https://irshad.az/ru/" içermelidir
* "Siyahi Mehsul Kartlari" elementlerinin sayı en az "1" olmalıdır
* Sehifede "Русский язык" yazısı olmalıdır
* "RU Ust Xett Magazalar" elementine klik et
* URL "https://irshad.az/ru/" içermelidir
* "Baki Magaza Kartlari" elementlerinin sayı en az "1" olmalıdır
* Sehifede "Русский язык" yazısı olmalıdır

## TC-UI-FLTB-001 Tək brend (Samsung) filtri

tags: filter, smoke

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* Sehifenin tam yüklenmesini gözle
* "400" piksel vertical scroll et
* "Brend Samsung" elementine klik et
* "Brend Samsung Checkbox" seçilmiş olmalıdır
* "Grid Yalniz Samsung" elementlerinin sayı "1" olmalıdır
* "Samsung Olmayan Mehsul Adlari" elementlerinin sayı "0" olmalıdır
* "Samsung Mehsul Adlari" elementlerinin sayı en az "1" olmalıdır

## TC-UI-FLTB-002 Tək brend (Apple) filtri

tags: filter

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* Sehifenin tam yüklenmesini gözle
* "400" piksel vertical scroll et
* "Brend Apple" elementine klik et
* "Brend Apple Checkbox" seçilmiş olmalıdır
* "Grid Yalniz Apple" elementlerinin sayı "1" olmalıdır
* "Apple Olmayan Mehsul Adlari" elementlerinin sayı "0" olmalıdır
* "Apple Mehsul Adlari" elementlerinin sayı en az "1" olmalıdır

## TC-UI-FLTB-003 İki brendin eyni anda seçilməsi (qrup daxilində VƏ YA məntiqi)

tags: filter

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* Sehifenin tam yüklenmesini gözle
* "400" piksel vertical scroll et
* "Brend Apple" elementine klik et
* "Apple Olmayan Mehsul Adlari" elementlerinin sayı "0" olmalıdır
* "Brend Samsung" elementine klik et
* "Brend Apple Checkbox" seçilmiş olmalıdır
* "Brend Samsung Checkbox" seçilmiş olmalıdır
* "Samsung Mehsul Adlari" elementlerinin sayı en az "1" olmalıdır
* "Apple Mehsul Adlari" elementlerinin sayı en az "1" olmalıdır
* "Grid Yalniz Apple ve Samsung" elementlerinin sayı "1" olmalıdır
* "Apple ve Samsung Olmayan Mehsul Adlari" elementlerinin sayı "0" olmalıdır

## TC-UI-FLTB-004 Brend seçimini ləğv edəndə siyahının ilkin vəziyyətə qayıtması

tags: filter, known-bug

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* Sehifenin tam yüklenmesini gözle
* "400" piksel vertical scroll et
* "Siyahi Mehsul Adi 1" elementinin metnini "ad1" olaraq yadda saxla
* "Siyahi Mehsul Adi 2" elementinin metnini "ad2" olaraq yadda saxla
* "Siyahi Mehsul Adi 3" elementinin metnini "ad3" olaraq yadda saxla
* "Siyahi Mehsul Adi 4" elementinin metnini "ad4" olaraq yadda saxla
* "Siyahi Mehsul Adi 5" elementinin metnini "ad5" olaraq yadda saxla
* "Brend Samsung" elementine klik et
* "Samsung Olmayan Mehsul Adlari" elementlerinin sayı "0" olmalıdır
* "Brend Samsung" elementine klik et
* "Brend Samsung Checkbox" seçilmemiş olmalıdır
* "Samsung Olmayan Mehsul Adlari" elementlerinin sayı en az "1" olmalıdır
* "Siyahi Mehsul Adi 1" elementinin metni "${ad1}" olmalıdır
* "Siyahi Mehsul Adi 2" elementinin metni "${ad2}" olmalıdır
* "Siyahi Mehsul Adi 3" elementinin metni "${ad3}" olmalıdır
* "Siyahi Mehsul Adi 4" elementinin metni "${ad4}" olmalıdır
* "Siyahi Mehsul Adi 5" elementinin metni "${ad5}" olmalıdır

## TC-UI-FLTB-006 Filtrli səhifə linkinin yeni sessiyada eyni nəticəni açması

tags: filter

Hər ssenari yeni brauzer sessiyası ilə başlayır (cookie və kəş yoxdur) — paylaşılan linkin başqa istifadəçidə açılması kimidir.

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar?brands[]=7"
* Sehifenin tam yüklenmesini gözle
* "Brend Samsung Checkbox" seçilmiş olmalıdır
* "Grid Yalniz Samsung" elementlerinin sayı "1" olmalıdır
* "Samsung Olmayan Mehsul Adlari" elementlerinin sayı "0" olmalıdır

## TC-UI-FLTB-010 Az məhsullu brendin (HMD) filtrlənməsi

tags: filter

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* Sehifenin tam yüklenmesini gözle
* "400" piksel vertical scroll et
* "Brend HMD" elementine klik et
* "Grid Yalniz HMD" elementlerinin sayı "1" olmalıdır
* "HMD Olmayan Mehsul Adlari" elementlerinin sayı "0" olmalıdır
* "HMD Mehsul Adlari" elementlerinin sayı en az "1" olmalıdır

## TC-UI-FLTP-001 Etibarlı qiymət aralığı ilə filtrləmə

tags: filter, smoke

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* "Qiymet Min Input" elementini temizle
* URL "price_from=&" içermelidir
* "Qiymet Min Input" elementine "500" yaz ve Tab düymesine bas
* "Qiymet Min Input" input deyeri "500" olmalıdır
* URL "price_from=500" içermelidir
* "Qiymet Max Input" elementini temizle
* URL "price_to=&" içermelidir
* "Qiymet Max Input" elementine "1000" yaz ve Tab düymesine bas
* "Qiymet Max Input" input deyeri "1000" olmalıdır
* URL "price_to=1000" içermelidir
* Sehifeni yenile
* "500-1000 Araligindan Kenar Qiymetler" elementlerinin sayı "0" olmalıdır
* "Siyahi Gorunen Qiymetler" elementlerinin sayı en az "1" olmalıdır

## TC-UI-FLTP-002 Min = Max = P (BVA: dəqiq sərhəd daxildir)

Sahə onluq qəbul etmədiyi üçün P = 2509.99 tam ədəd sərhədləri ilə əhatə olunur: min 2509, max 2510.

tags: filter, bva

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* "Qiymet Min Input" elementini temizle
* URL "price_from=&" içermelidir
* "Qiymet Min Input" elementine "2509" yaz ve Tab düymesine bas
* "Qiymet Min Input" input deyeri "2509" olmalıdır
* URL "price_from=2509" içermelidir
* "Qiymet Max Input" elementini temizle
* URL "price_to=&" içermelidir
* "Qiymet Max Input" elementine "2510" yaz ve Tab düymesine bas
* "Qiymet Max Input" input deyeri "2510" olmalıdır
* URL "price_to=2510" içermelidir
* Sehifeni yenile
* "2509-2510 Araligindan Kenar Qiymetler" elementlerinin sayı "0" olmalıdır
* "A Mehsulu Siyahida" elementlerinin sayı en az "1" olmalıdır

## TC-UI-FLTP-003 Min = P + 0.01 (BVA: aşağı sərhəddən bir addım yuxarı)

Sahə onluq qəbul etmir (BUG-UI-015) — TC qaydası ilə tam ədəd: min = 2510 (> P = 2509.99).

tags: filter, bva

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* "Qiymet Max Input" elementini temizle
* URL "price_to=&" içermelidir
* "Qiymet Min Input" elementini temizle
* URL "price_from=&" içermelidir
* "Qiymet Min Input" elementine "2510" yaz ve Tab düymesine bas
* "Qiymet Min Input" input deyeri "2510" olmalıdır
* URL "price_from=2510" içermelidir
* Sehifeni yenile
* "2510-dan Asagi Qiymetler" elementlerinin sayı "0" olmalıdır
* "Siyahi Gorunen Qiymetler" elementlerinin sayı en az "1" olmalıdır
* "A Mehsulu Siyahida" sehifede mövcud olmamalıdır

## TC-UI-FLTP-004 Max = P − 0.01 (BVA: yuxarı sərhəddən bir addım aşağı)

Sahə onluq qəbul etmir (BUG-UI-015) — TC qaydası ilə tam ədəd: max = 2509 (< P = 2509.99).

tags: filter, bva

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* "Qiymet Min Input" elementini temizle
* URL "price_from=&" içermelidir
* "Qiymet Max Input" elementini temizle
* URL "price_to=&" içermelidir
* "Qiymet Max Input" elementine "2509" yaz ve Tab düymesine bas
* "Qiymet Max Input" input deyeri "2509" olmalıdır
* URL "price_to=2509" içermelidir
* Sehifeni yenile
* "2509-dan Yuxari Qiymetler" elementlerinin sayı "0" olmalıdır
* "Siyahi Gorunen Qiymetler" elementlerinin sayı en az "1" olmalıdır
* "A Mehsulu Siyahida" sehifede mövcud olmamalıdır

## TC-UI-FLTP-005 Yalnız minimum qiymətin daxil edilməsi

tags: filter

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* "Qiymet Max Input" elementini temizle
* URL "price_to=&" içermelidir
* "Qiymet Min Input" elementini temizle
* URL "price_from=&" içermelidir
* "Qiymet Min Input" elementine "2000" yaz ve Tab düymesine bas
* "Qiymet Min Input" input deyeri "2000" olmalıdır
* URL "price_from=2000" içermelidir
* Sehifeni yenile
* "2000-den Asagi Qiymetler" elementlerinin sayı "0" olmalıdır
* "Siyahi Gorunen Qiymetler" elementlerinin sayı en az "1" olmalıdır

## TC-UI-FLTP-006 Yalnız maksimum qiymətin daxil edilməsi

tags: filter

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* "Qiymet Min Input" elementini temizle
* URL "price_from=&" içermelidir
* "Qiymet Max Input" elementini temizle
* URL "price_to=&" içermelidir
* "Qiymet Max Input" elementine "300" yaz ve Tab düymesine bas
* "Qiymet Max Input" input deyeri "300" olmalıdır
* URL "price_to=300" içermelidir
* Sehifeni yenile
* "300-den Yuxari Qiymetler" elementlerinin sayı "0" olmalıdır
* "Siyahi Gorunen Qiymetler" elementlerinin sayı en az "1" olmalıdır

## TC-UI-FLTP-013 Qiymət aralığı ilə brend filtrinin birlikdə işləməsi (VƏ məntiqi)

tags: filter

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* Sehifenin tam yüklenmesini gözle
* "400" piksel vertical scroll et
* "Brend Samsung" elementine klik et
* "Samsung Olmayan Mehsul Adlari" elementlerinin sayı "0" olmalıdır
* "Qiymet Min Input" elementini temizle
* URL "price_from=&" içermelidir
* "Qiymet Min Input" elementine "500" yaz ve Tab düymesine bas
* "Qiymet Min Input" input deyeri "500" olmalıdır
* URL "price_from=500" içermelidir
* "Qiymet Max Input" elementini temizle
* URL "price_to=&" içermelidir
* "Qiymet Max Input" elementine "1500" yaz ve Tab düymesine bas
* "Qiymet Max Input" input deyeri "1500" olmalıdır
* URL "price_to=1500" içermelidir
* Sehifeni yenile
* "500-1500 Araligindan Kenar Qiymetler" elementlerinin sayı "0" olmalıdır
* "Samsung Olmayan Mehsul Adlari" elementlerinin sayı "0" olmalıdır
* "Samsung Mehsul Adlari" elementlerinin sayı en az "1" olmalıdır

## TC-UI-SORT-001 Sıralama siyahısında 6 variantın olması

tags: sort

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* "Siralama Select" görünür olmalıdır
* "Siralama Variantlari" elementlerinin sayı "6" olmalıdır
* "Siralama Evvelce baha" elementlerinin sayı "1" olmalıdır
* "Siralama Ada gore" elementlerinin sayı "1" olmalıdır
* "Siralama Yeniler evvelce" elementlerinin sayı "1" olmalıdır
* "Siralama Populyar evvelce" elementlerinin sayı "1" olmalıdır
* "Siralama Populyar sonda" elementlerinin sayı "1" olmalıdır
* "Siralama Evvelce ucuz" elementlerinin sayı "1" olmalıdır
* "Siralama Bos Variant" elementlerinin sayı "0" olmalıdır

## TC-UI-SORT-002 "Əvvəlcə ucuz" sıralaması

tags: sort, smoke

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* "Siralama Select" dropdown-undan "Əvvəlcə ucuz" metnini seç
* URL "direction=asc&sort=price" içermelidir
* "Siyahi Mehsul Kartlari" elementlerinin sayı en az "5" olmalıdır
* "Artan Sira Pozuntulari" elementlerinin sayı "0" olmalıdır

## TC-UI-SORT-003 "Əvvəlcə baha" sıralaması

tags: sort

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* "Siralama Select" dropdown-undan "Əvvəlcə baha" metnini seç
* URL "direction=desc&sort=price" içermelidir
* "Siyahi Mehsul Kartlari" elementlerinin sayı en az "5" olmalıdır
* "Azalan Sira Pozuntulari" elementlerinin sayı "0" olmalıdır

## TC-UI-SORT-004 "Ada görə" sıralaması

Avtomat yoxlama adların birinci simvolunun (0–9, A–Z, böyük-kiçik hərf nəzərə alınmadan) azalmayan sırada olmasını yoxlayır.

tags: sort

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* "Siralama Select" dropdown-undan "Ada görə" metnini seç
* URL "sort=title" içermelidir
* "Siyahi Mehsul Kartlari" elementlerinin sayı en az "5" olmalıdır
* "Ad Sirasi Pozuntulari" elementlerinin sayı "0" olmalıdır

## TC-UI-SORT-007 Sıralamanın brend filtri ilə birlikdə işləməsi

tags: sort, filter

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* Sehifenin tam yüklenmesini gözle
* "400" piksel vertical scroll et
* "Brend Samsung" elementine klik et
* "Samsung Olmayan Mehsul Adlari" elementlerinin sayı "0" olmalıdır
* "Siralama Select" dropdown-undan "Əvvəlcə ucuz" metnini seç
* URL "direction=asc&sort=price" içermelidir
* "Brend Samsung Checkbox" seçilmiş olmalıdır
* "Grid Yalniz Samsung" elementlerinin sayı "1" olmalıdır
* "Artan Sira Pozuntulari" elementlerinin sayı "0" olmalıdır
* "Samsung Olmayan Mehsul Adlari" elementlerinin sayı "0" olmalıdır
* "Samsung Mehsul Adlari" elementlerinin sayı en az "2" olmalıdır

## TC-UI-CRD-001 Kateqoriya kartında aylıq ödəniş məlumatının göstərilməsi

11.10.2026 formatı: kartda müddət seçimi (6 / 12 / 18 ay) və aylıq məbləğ "X AZN".

tags: card

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* "Siyahi Ayliq Odenisler" elementlerinin sayı en az "1" olmalıdır
* "Siyahi Yanlis Ayliq Odenisler" elementlerinin sayı "0" olmalıdır
* Sehifede "18 ay" yazısı olmalıdır

## TC-UI-PDP-001 Məhsul səhifəsinin əsas elementlərlə açılması

tags: pdp, smoke

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white"
* "PDP Basliq" elementinin metni "iPhone Air 256 GB Cloud White" olmalıdır
* "PDP Cari Qiymet" elementin içinde "AZN" yazısı var
* "PDP Sekil" görünür olmalıdır
* "PDP Sebete Elave Button" görünür olmalıdır
* "PDP Sebete Elave Button" elementinin "class" atributunda "btn-green" olmalıdır
* "PDP Bir Klikle Al Button" görünür olmalıdır
* "PDP Bir Klikle Al Button" elementin içinde "Bir kliklə al" yazısı var

## TC-UI-PDP-002 Kateqoriya kartındakı qiymətlə məhsul səhifəsindəki qiymətin eyni olması

Hazırlıq: A-nın kartını birinci hissəyə gətirmək üçün kateqoriya qiymət aralığı (2509–2510) ilə açılır.

tags: pdp

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar?price_from=2509&price_to=2510"
* Sehifenin tam yüklenmesini gözle
* "300" piksel vertical scroll et
* "A Karti Cloud White Reng" elementine klik et
* "A Karti Ad Linki" görünür olmalıdır
* "A Karti Cari Qiymet" elementinin metnini "kartQiymeti" olaraq yadda saxla
* "A Karti Ad Linki" elementine klik et
* URL "/az/mehsullar/iphone-air-256-gb-cloud-white" içermelidir
* "PDP Cari Qiymet" elementinin metni "${kartQiymeti}" olmalıdır

## TC-UI-PDP-003 Endirimli məhsulda köhnə qiymətin cari qiymətdən böyük göstərilməsi

Üstündən xətt (vizual) avtomat yoxlanılmır — köhnə qiymət ayrıca "old-price" elementi kimi göstərilir.

tags: pdp

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar?price_from=2509&price_to=2510"
* Sehifenin tam yüklenmesini gözle
* "300" piksel vertical scroll et
* "A Karti Cloud White Reng" elementine klik et
* "A Karti Kohne Qiymet" görünür olmalıdır
* "A Karti Cari Qiymet" görünür olmalıdır
* "A Karti Endirimi Duzgun" elementlerinin sayı "1" olmalıdır

## TC-UI-CART-002 Kateqoriya kartından birbaşa səbətə əlavə

tags: cart

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar?price_from=2509&price_to=2510"
* Sehifenin tam yüklenmesini gözle
* "300" piksel vertical scroll et
* "A Karti Cloud White Reng" elementine klik et
* "A Karti Ad Linki" görünür olmalıdır
* "200" piksel vertical scroll et
* "A Karti Sebete Elave Button" elementine klik et
* "Header Sebet Sayi" elementinin metni "1" olmalıdır
* "https://irshad.az/az/sebet" adresine keçid et
* "Sebet Mehsul Setirleri" elementlerinin sayı "1" olmalıdır
* "Sebet Ilk Mehsul Adi" elementinin metni "iPhone Air 256 GB Cloud White" olmalıdır
* "Sebet Ilk Mehsul Sayi" input deyeri "1" olmalıdır

## TC-UI-FLTB-007 Səhifə yenilənəndə (F5) brend filtrinin saxlanması

tags: filter

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* Sehifenin tam yüklenmesini gözle
* "400" piksel vertical scroll et
* "Brend Samsung" elementine klik et
* "Brend Samsung Checkbox" seçilmiş olmalıdır
* URL "brands" içermelidir
* Sehifeni yenile
* Sehifenin tam yüklenmesini gözle
* URL "brands" içermelidir
* "Brend Samsung Checkbox" seçilmiş olmalıdır
* "Samsung Olmayan Mehsul Adlari" elementlerinin sayı "0" olmalıdır
* "Samsung Mehsul Adlari" elementlerinin sayı en az "1" olmalıdır

## TC-UI-FLTP-009 Mənfi qiymətin daxil edilməsi

tags: filter, negative

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* "Qiymet Min Input" elementini temizle
* URL "price_from=&" içermelidir
* "Qiymet Min Input" elementine "-100" yaz ve Tab düymesine bas
* "Qiymet Min Input" input deyeri "100" olmalıdır
* URL "price_from=100" içermelidir
* Sehifeni yenile
* "Siyahi Gorunen Qiymetler" elementlerinin sayı en az "1" olmalıdır

## TC-UI-FLTP-010 Qiymət sahəsinə hərf daxil edilməsi

tags: filter, negative

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* "Qiymet Min Input" elementini temizle
* URL "price_from=&" içermelidir
* "Qiymet Min Input" elementine "abc" yaz ve Tab düymesine bas
* "Qiymet Min Input" input deyeri "" olmalıdır
* URL "price_from=&" içermelidir
* "Siyahi Gorunen Qiymetler" elementlerinin sayı en az "1" olmalıdır

## TC-UI-FLTP-008 Min-in max-dan böyük daxil edilməsi

tags: filter, negative, known-bug

BUG-UI-014: min > max aralığı xəbərdarlıqsız qəbul olunur, siyahı mesajsız boş qalır.
Gözlənilən: sistem məntiqsiz aralığı qəbul etmir (dəyərləri yerini dəyişir və ya filtri tətbiq etmir) — hər iki halda siyahıda məhsul qalır.

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* "Qiymet Min Input" elementini temizle
* URL "price_from=&" içermelidir
* "Qiymet Min Input" elementine "2000" yaz ve Tab düymesine bas
* URL "price_from=2000" içermelidir
* "Qiymet Max Input" elementini temizle
* URL "price_to=&" içermelidir
* "Qiymet Max Input" elementine "1000" yaz ve Tab düymesine bas
* URL "price_to=1000" içermelidir
* Sehifeni yenile
* "Siyahi Gorunen Qiymetler" elementlerinin sayı en az "1" olmalıdır

