# irshad.az — Bəyəndiklərim və Müqayisə

Test mühiti: https://irshad.az
Excel: "UI Test Cases" vərəqi (TS-UI-13 Bəyəndiklərim, TS-UI-14 Müqayisə)
İstinad məhsullar: A = iPhone Air 256 GB Cloud White (kod RF1R0JV); B = iPhone 17 Pro 1 TB Cosmic Orange (kod LZ5AGZT).
Hər ssenari yeni brauzer sessiyası ilə başlayır — qonaq istifadəçinin bəyəndiklər və müqayisə siyahıları boşdur.
Ön şərt (siyahıda A/B olması) məhsul səhifəsindəki ❤ / ⚖ ikonları ilə hazırlanır.

tags: ui, irshad, favorites, compare

## TC-UI-FAV-001 Kateqoriya kartından məhsulun bəyəndiklərimə əlavə edilməsi

tags: favorites, smoke

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar?price_from=2509&price_to=2510"
* Sehifenin tam yüklenmesini gözle
* "300" piksel vertical scroll et
* "A Karti Cloud White Reng" elementine klik et
* "Kart A Beyen Ikonu" elementine klik et
* "Header Beyendim Sayi" elementinin metni "1" olmalıdır
* "https://irshad.az/az/beyendiklerim" adresine keçid et
* "Beyendiklerim Kartlari" elementlerinin sayı "1" olmalıdır
* "Beyendiklerim A Karti" görünür olmalıdır

## TC-UI-FAV-002 Məhsul səhifəsindən bəyəndiklərimə əlavə

tags: favorites

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white"
* "PDP Beyen Ikonu" elementine klik et
* "Header Beyendim Sayi" elementinin metni "1" olmalıdır
* "PDP Beyen Ikonu Aktiv" elementlerinin sayı "1" olmalıdır
* "https://irshad.az/az/beyendiklerim" adresine keçid et
* "Beyendiklerim A Karti" görünür olmalıdır

## TC-UI-FAV-003 Bəyən ikonuna təkrar klikləməklə məhsulun çıxarılması (toggle)

tags: favorites

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar?price_from=2509&price_to=2510"
* Sehifenin tam yüklenmesini gözle
* "300" piksel vertical scroll et
* "A Karti Cloud White Reng" elementine klik et
* "Kart A Beyen Ikonu" elementine klik et
* "Header Beyendim Sayi" elementinin metni "1" olmalıdır
* "Kart A Beyen Ikonu Aktiv" elementlerinin sayı "1" olmalıdır
* "Kart A Beyen Ikonu" elementine klik et
* "Kart A Beyen Ikonu Aktiv" sehifede mövcud olmamalıdır
* "Header Beyendim Sayi" görünmemelidir
* "https://irshad.az/az/beyendiklerim" adresine keçid et
* "Beyendiklerim A Karti" sehifede mövcud olmamalıdır

## TC-UI-FAV-004 Bəyəndiklərim səhifəsindən məhsulun silinməsi

tags: favorites

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white"
* "PDP Beyen Ikonu" elementine klik et
* "Header Beyendim Sayi" elementinin metni "1" olmalıdır
* "https://irshad.az/az/mehsullar/iphone-17-pro-1-tb-cosmic-orange-2" adresine keçid et
* "PDP Beyen Ikonu" elementine klik et
* "Header Beyendim Sayi" elementinin metni "2" olmalıdır
* "https://irshad.az/az/beyendiklerim" adresine keçid et
* "Beyendiklerim Kartlari" elementlerinin sayı "2" olmalıdır
* "Beyendiklerim A Beyen Ikonu" elementine klik et
* "Header Beyendim Sayi" elementinin metni "1" olmalıdır
* Sehifeni yenile
* "Beyendiklerim A Karti" sehifede mövcud olmamalıdır
* "Beyendiklerim B Karti" görünür olmalıdır
* "Beyendiklerim Kartlari" elementlerinin sayı "1" olmalıdır

## TC-UI-FAV-005 Boş Bəyəndiklərim vəziyyəti

tags: favorites, known-bug

* Brauzeri aç ve keçid et "https://irshad.az/az/beyendiklerim"
* Sehifede "Bəyəndiklərim" yazısı olmalıdır
* "Beyendiklerim Kartlari" elementlerinin sayı "0" olmalıdır
* "Beyendiklerim Bos Mesaji" elementlerinin sayı en az "1" olmalıdır

## TC-UI-FAV-007 Səhifə yenilənəndə bəyəndiklərimin saxlanması

tags: favorites

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white"
* "PDP Beyen Ikonu" elementine klik et
* "Header Beyendim Sayi" elementinin metni "1" olmalıdır
* "https://irshad.az/az/beyendiklerim" adresine keçid et
* "Beyendiklerim A Karti" görünür olmalıdır
* Sehifeni yenile
* "Beyendiklerim A Karti" görünür olmalıdır
* "Beyendiklerim Kartlari" elementlerinin sayı "1" olmalıdır
* "Header Beyendim Sayi" elementinin metni "1" olmalıdır

## TC-UI-FAV-008 Bir neçə məhsulun bəyəndiklərimə əlavə edilməsi

tags: favorites

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* "Siyahi Mehsul Adi 1" elementinin metnini "ad1" olaraq yadda saxla
* "Siyahi Mehsul Adi 2" elementinin metnini "ad2" olaraq yadda saxla
* "Siyahi Mehsul Adi 3" elementinin metnini "ad3" olaraq yadda saxla
* "Siyahi 1-ci Kart Beyen Ikonu" elementine klik et
* "Header Beyendim Sayi" elementinin metni "1" olmalıdır
* "Siyahi 2-ci Kart Beyen Ikonu" elementine klik et
* "Header Beyendim Sayi" elementinin metni "2" olmalıdır
* "Siyahi 3-cu Kart Beyen Ikonu" elementine klik et
* "Header Beyendim Sayi" elementinin metni "3" olmalıdır
* "https://irshad.az/az/beyendiklerim" adresine keçid et
* "Beyendiklerim Kartlari" elementlerinin sayı "3" olmalıdır
* "xpath=//section[@id='AccountWishlist']//a[contains(@class,'product__name') and normalize-space()='${ad1}']" elementlerinin sayı "1" olmalıdır
* "xpath=//section[@id='AccountWishlist']//a[contains(@class,'product__name') and normalize-space()='${ad2}']" elementlerinin sayı "1" olmalıdır
* "xpath=//section[@id='AccountWishlist']//a[contains(@class,'product__name') and normalize-space()='${ad3}']" elementlerinin sayı "1" olmalıdır

## TC-UI-CMP-001 Boş müqayisə səhifəsinin göstərilməsi

tags: compare, smoke, backlog

* Brauzeri aç ve keçid et "https://irshad.az/az/muqayise"
* Sehifede "Müqayisə" yazısı olmalıdır
* Sehifede "Müqayisə etmək üçün məhsul əlavə olunmayıb" yazısı olmalıdır
* Sehifede "Alışverişə davam et" yazısı olmalıdır
* Sehifede "Səbətə keç" yazısı olmalıdır

## TC-UI-CMP-002 "Alışverişə davam et" düyməsinin işləməsi

tags: compare, backlog

* Brauzeri aç ve keçid et "https://irshad.az/az/muqayise"
* "Alışverişə davam et" metnli elemente klik et
* Sehifenin tam yüklenmesini gözle
* "Bos Muqayise Mesaji" görünmemelidir
* "Header Logo" görünür olmalıdır
* "Kataloq Button" görünür olmalıdır

## TC-UI-CART-019 Müqayisə səhifəsindəki "Səbətə keç" düyməsi

tags: compare, cart, backlog

* Brauzeri aç ve keçid et "https://irshad.az/az/muqayise"
* "Səbətə keç" metnli elemente klik et
* URL "https://irshad.az/az/sebet" olmalıdır

## TC-UI-CMP-003 Eyni kateqoriyadan 2 məhsulun müqayisəyə əlavə edilməsi

tags: compare, smoke

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar?price_from=2509&price_to=2510"
* Sehifenin tam yüklenmesini gözle
* "300" piksel vertical scroll et
* "A Karti Cloud White Reng" elementine klik et
* "Kart A Muqayise Ikonu" elementine klik et
* "Header Muqayise Sayi" elementinin metni "1" olmalıdır
* "https://irshad.az/az/mehsullar?q=iPhone 17 Pro 1 TB Cosmic Orange" adresine keçid et
* Sehifenin tam yüklenmesini gözle
* "300" piksel vertical scroll et
* "Kart B Muqayise Ikonu" elementine klik et
* "Header Muqayise Sayi" elementinin metni "2" olmalıdır
* "https://irshad.az/az/muqayise" adresine keçid et
* "Muqayise Mehsul Basliqlari" elementlerinin sayı "2" olmalıdır
* "Muqayise A Basligi" görünür olmalıdır
* "Muqayise B Basligi" görünür olmalıdır
* "Muqayise Xususiyyet Setirleri" elementlerinin sayı en az "3" olmalıdır
* "Bos Muqayise Mesaji" sehifede mövcud olmamalıdır

## TC-UI-CMP-004 Müqayisədən bir məhsulun silinməsi

tags: compare

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white"
* "PDP Muqayise Ikonu" elementine klik et
* "Header Muqayise Sayi" elementinin metni "1" olmalıdır
* "https://irshad.az/az/mehsullar/iphone-17-pro-1-tb-cosmic-orange-2" adresine keçid et
* "PDP Muqayise Ikonu" elementine klik et
* "Header Muqayise Sayi" elementinin metni "2" olmalıdır
* "https://irshad.az/az/muqayise" adresine keçid et
* "Muqayise Mehsul Basliqlari" elementlerinin sayı "2" olmalıdır
* "Muqayise A Sil" elementine klik et
* "Muqayise A Basligi" sehifede mövcud olmamalıdır
* "Muqayise B Basligi" görünür olmalıdır
* "Muqayise Mehsul Basliqlari" elementlerinin sayı "1" olmalıdır

## TC-UI-CMP-005 Bütün məhsullar silinəndə boş vəziyyətə qayıtma (dolu → boş)

tags: compare

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/iphone-17-pro-1-tb-cosmic-orange-2"
* "PDP Muqayise Ikonu" elementine klik et
* "Header Muqayise Sayi" elementinin metni "1" olmalıdır
* "https://irshad.az/az/muqayise" adresine keçid et
* "Muqayise B Basligi" görünür olmalıdır
* "Muqayise B Sil" elementine klik et
* Sehifede "Müqayisə etmək üçün məhsul əlavə olunmayıb" yazısı olmalıdır
* "Muqayise Mehsul Basliqlari" elementlerinin sayı "0" olmalıdır

## TC-UI-CMP-006 Eyni məhsulun müqayisəyə iki dəfə əlavə edilməməsi

Gözlənilən: A müqayisədə ən çox bir dəfə göstərilir (ikinci klik ya çıxarır, ya da heç nə etmir).

tags: compare

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white"
* "PDP Muqayise Ikonu" elementine klik et
* "Header Muqayise Sayi" elementinin metni "1" olmalıdır
* "PDP Muqayise Ikonu" elementine klik et
* Sehifenin tam yüklenmesini gözle
* "https://irshad.az/az/muqayise" adresine keçid et
* "Muqayise A Dublikat Basligi" sehifede mövcud olmamalıdır

## TC-UI-CMP-009 Müqayisədəki qiymətin məhsul səhifəsindəki qiymətlə eyni olması

tags: compare

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white"
* "PDP Muqayise Ikonu" elementine klik et
* "Header Muqayise Sayi" elementinin metni "1" olmalıdır
* "https://irshad.az/az/muqayise" adresine keçid et
* "Muqayise A Qiymeti" elementinin metnini "muqayiseQiymeti" olaraq yadda saxla
* "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white" adresine keçid et
* "PDP Cari Qiymet" elementinin metni "${muqayiseQiymeti}" olmalıdır

## TC-UI-CMP-010 Səhifə yenilənəndə müqayisə siyahısının saxlanması

tags: compare

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white"
* "PDP Muqayise Ikonu" elementine klik et
* "Header Muqayise Sayi" elementinin metni "1" olmalıdır
* "https://irshad.az/az/mehsullar/iphone-17-pro-1-tb-cosmic-orange-2" adresine keçid et
* "PDP Muqayise Ikonu" elementine klik et
* "Header Muqayise Sayi" elementinin metni "2" olmalıdır
* "https://irshad.az/az/muqayise" adresine keçid et
* "Muqayise Mehsul Basliqlari" elementlerinin sayı "2" olmalıdır
* Sehifeni yenile
* "Muqayise A Basligi" görünür olmalıdır
* "Muqayise B Basligi" görünür olmalıdır
* "Muqayise Mehsul Basliqlari" elementlerinin sayı "2" olmalıdır
