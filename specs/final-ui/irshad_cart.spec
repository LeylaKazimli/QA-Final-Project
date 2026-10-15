# irshad.az — Səbət

Test mühiti: https://irshad.az
Excel: "UI Test Cases" vərəqi (TS-UI-12 Səbət)
Test data: A = iPhone Air 256 GB Cloud White, B = iPhone 17 Pro 1 TB Cosmic Orange.
Qiymətlər spec-ə yazılmır: məhsul səhifəsindən oxunur, səbət cəmi nisbi yoxlanılır (cəm = say × qiymət; cəm = məhsulların qiyməti + endirim; cəm = sətirlərin cəmi).
Hər ssenari yeni brauzer sessiyası ilə başlayır — qonaq səbəti boşdur. Real sifariş verilmir.

tags: ui, irshad, cart

## TC-UI-HOME-007 Boş səbət ikonuna klikləyəndə boş səbət vəziyyətinin göstərilməsi

tags: home, known-bug

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Sebet Link" elementine klik et
* URL "https://irshad.az/az/sebet" olmalıdır
* "Sebet Mehsul Setirleri" elementlerinin sayı "0" olmalıdır
* "Header Sebet Sayi" görünmemelidir

## TC-UI-CART-001 Məhsul səhifəsindən səbətə məhsul əlavə edilməsi

tags: smoke

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white"
* "PDP Cari Qiymet" elementinin metnini "pdpQiymeti" olaraq yadda saxla
* "PDP Sebete Elave Button" kliklene bilene qeder gözle
* "PDP Sebete Elave Button" elementine klik et
* "Header Sebet Sayi" elementinin metni "1" olmalıdır
* "https://irshad.az/az/sebet" adresine keçid et
* "Sebet Mehsul Setirleri" elementlerinin sayı "1" olmalıdır
* "Sebet Ilk Mehsul Adi" elementinin metni "iPhone Air 256 GB Cloud White" olmalıdır
* "Sebet Ilk Mehsul Sayi" input deyeri "1" olmalıdır
* "xpath=(//section[contains(@class,'basket')]//div[contains(@class,'basket__content__item')]//p[contains(@class,'new-price')])[1][round(100*number(normalize-space(translate(.,'AZN','')))) = round(100*number(normalize-space(translate('${pdpQiymeti}','AZN',''))))]" elementlerinin sayı "1" olmalıdır

## TC-UI-CART-003 Səbətdə məhsul sayının artırılması (+)

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white"
* "PDP Sebete Elave Button" elementine klik et
* "Header Sebet Sayi" elementinin metni "1" olmalıdır
* "https://irshad.az/az/sebet" adresine keçid et
* "Sebet Ilk Mehsul Plus" elementine klik et
* "Sebet Ilk Mehsul Sayi" input deyeri "2" olmalıdır
* "Sebet Cemi 2 Ededin Qiymetine Beraber" elementlerinin sayı "1" olmalıdır
* "Sebet Cemi Endirimle Uygun" elementlerinin sayı "1" olmalıdır

## TC-UI-CART-004 Səbətdə məhsul sayının azaldılması (−)

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white"
* "PDP Sebete Elave Button" elementine klik et
* "Header Sebet Sayi" elementinin metni "1" olmalıdır
* "https://irshad.az/az/sebet" adresine keçid et
* "Sebet Ilk Mehsul Plus" elementine klik et
* "Sebet Ilk Mehsul Sayi" input deyeri "2" olmalıdır
* "Sebet Ilk Mehsul Minus" elementine klik et
* "Sebet Ilk Mehsul Sayi" input deyeri "1" olmalıdır
* "Sebet Cemi 1 Ededin Qiymetine Beraber" elementlerinin sayı "1" olmalıdır

## TC-UI-CART-008 Eyni məhsulun ikinci dəfə səbətə əlavə edilməsi

Saytın davranışı (11.10.2026 manual təsdiq): məhsul artıq səbətdədirsə düymə "Səbətə keç" vəziyyətinə keçir
və klik səbət səhifəsinə aparır — dublikat sətir yaranmır, say 1 qalır.

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white"
* "PDP Sebete Elave Button" elementine klik et
* "Header Sebet Sayi" elementinin metni "1" olmalıdır
* Sehifeni yenile
* "PDP Sebete Elave Button" kliklene bilene qeder gözle
* "PDP Sebete Elave Button" elementine klik et
* URL "https://irshad.az/az/sebet" olmalıdır
* "Sebet Mehsul Setirleri" elementlerinin sayı "1" olmalıdır
* "Sebet Ilk Mehsul Sayi" input deyeri "1" olmalıdır
* "Header Sebet Sayi" elementinin metni "1" olmalıdır

## TC-UI-CART-009 İki fərqli məhsulun səbətə əlavə edilməsi və ümumi cəm

tags: smoke

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white"
* "PDP Sebete Elave Button" elementine klik et
* "Header Sebet Sayi" elementinin metni "1" olmalıdır
* "https://irshad.az/az/mehsullar/iphone-17-pro-1-tb-cosmic-orange-2" adresine keçid et
* "PDP Sebete Elave Button" kliklene bilene qeder gözle
* "PDP Sebete Elave Button" elementine klik et
* "Header Sebet Sayi" elementinin metni "2" olmalıdır
* "https://irshad.az/az/sebet" adresine keçid et
* "Sebet Mehsul Setirleri" elementlerinin sayı "2" olmalıdır
* "Sebet iPhone Air Setri" görünür olmalıdır
* "Sebet iPhone 17 Pro Setri" görünür olmalıdır
* "Sebet Cemi Setirlerin Cemine Beraber" elementlerinin sayı "1" olmalıdır

## TC-UI-CART-010 Səbət sayğacının (header) yenilənməsi

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white"
* "Header Sebet Sayi" görünmemelidir
* "PDP Sebete Elave Button" elementine klik et
* "Header Sebet Sayi" elementinin metni "1" olmalıdır
* "https://irshad.az/az/mehsullar/iphone-17-pro-1-tb-cosmic-orange-2" adresine keçid et
* "PDP Sebete Elave Button" kliklene bilene qeder gözle
* "PDP Sebete Elave Button" elementine klik et
* "Header Sebet Sayi" elementinin metni "2" olmalıdır

## TC-UI-CART-011 Səbətdəki qiymətin məhsul səhifəsindəki qiymətlə eyni olması

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white"
* "PDP Cari Qiymet" elementinin metnini "pdpQiymeti" olaraq yadda saxla
* "PDP Sebete Elave Button" elementine klik et
* "Header Sebet Sayi" elementinin metni "1" olmalıdır
* "https://irshad.az/az/sebet" adresine keçid et
* "xpath=(//section[contains(@class,'basket')]//div[contains(@class,'basket__content__item')]//p[contains(@class,'new-price')])[1][round(100*number(normalize-space(translate(.,'AZN','')))) = round(100*number(normalize-space(translate('${pdpQiymeti}','AZN',''))))]" elementlerinin sayı "1" olmalıdır

## TC-UI-CART-012 Səbətdə məhsul adına klikləyəndə məhsul səhifəsinin açılması

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white"
* "PDP Sebete Elave Button" elementine klik et
* "Header Sebet Sayi" elementinin metni "1" olmalıdır
* "https://irshad.az/az/sebet" adresine keçid et
* "Sebet Ilk Mehsul Adi" elementine klik et
* URL "/az/mehsullar/iphone-air-256-gb-cloud-white" içermelidir
* "PDP Basliq" elementinin metni "iPhone Air 256 GB Cloud White" olmalıdır

## TC-UI-CART-013 Səbətdən məhsulun silinməsi

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white"
* "PDP Sebete Elave Button" elementine klik et
* "Header Sebet Sayi" elementinin metni "1" olmalıdır
* "https://irshad.az/az/mehsullar/iphone-17-pro-1-tb-cosmic-orange-2" adresine keçid et
* "PDP Sebete Elave Button" kliklene bilene qeder gözle
* "PDP Sebete Elave Button" elementine klik et
* "Header Sebet Sayi" elementinin metni "2" olmalıdır
* "https://irshad.az/az/sebet" adresine keçid et
* "Sebet iPhone Air Sil" elementine klik et
* "Sebet iPhone Air Setri" sehifede mövcud olmamalıdır
* "Sebet Mehsul Setirleri" elementlerinin sayı "1" olmalıdır
* "Sebet iPhone 17 Pro Setri" görünür olmalıdır
* "Sebet Cemi Setirlerin Cemine Beraber" elementlerinin sayı "1" olmalıdır

## TC-UI-CART-014 Son məhsul silinəndə boş səbət vəziyyəti (dolu → boş)

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white"
* "PDP Sebete Elave Button" elementine klik et
* "Header Sebet Sayi" elementinin metni "1" olmalıdır
* "https://irshad.az/az/sebet" adresine keçid et
* "Sebet Ilk Mehsul Sil" elementine klik et
* "Sebet Mehsul Setirleri" elementlerinin sayı "0" olmalıdır
* "Header Sebet Sayi" görünmemelidir

## TC-UI-CART-015 Səhifə yenilənəndə (F5) səbətin saxlanması

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white"
* "PDP Sebete Elave Button" elementine klik et
* "Header Sebet Sayi" elementinin metni "1" olmalıdır
* "https://irshad.az/az/sebet" adresine keçid et
* "Sebet Ilk Mehsul Plus" elementine klik et
* "Sebet Ilk Mehsul Sayi" input deyeri "2" olmalıdır
* Sehifeni yenile
* "Sebet Ilk Mehsul Adi" elementinin metni "iPhone Air 256 GB Cloud White" olmalıdır
* "Sebet Ilk Mehsul Sayi" input deyeri "2" olmalıdır
* "Sebet Cemi 2 Ededin Qiymetine Beraber" elementlerinin sayı "1" olmalıdır

## TC-UI-CART-005 Say = 1 olanda azaltma (BVA: minimum say)

tags: cart, negative, bva

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white"
* "PDP Sebete Elave Button" elementine klik et
* "Header Sebet Sayi" elementinin metni "1" olmalıdır
* "https://irshad.az/az/sebet" adresine keçid et
* "Sebet Ilk Mehsul Sayi" input deyeri "1" olmalıdır
* "Sebet Ilk Mehsul Minus" elementine klik et
* Sehifeni yenile
* "Sebet Ilk Mehsul Sayi" input deyeri "1" olmalıdır
* "Sebet Ilk Mehsul Adi" elementin içinde "iPhone Air 256 GB" yazısı var
* "Header Sebet Sayi" elementinin metni "1" olmalıdır
