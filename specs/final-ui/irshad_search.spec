# irshad.az — Axtarış

Test mühiti: https://irshad.az
Excel: "UI Test Cases" vərəqi (TS-UI-04 Axtarış)
Nəticə səhifəsinin başlığı sorğunu yazıldığı kimi göstərir: "<sorğu> üzrə axtarış N nəticə verdi".
Başlıqların müqayisəsi böyük-kiçik hərf nəzərə alınmadan aparılır (eyni nəticə sayı).
Hər ssenari yeni brauzer sessiyası ilə başlayır. Real sifariş verilmir.

tags: ui, irshad, search

## TC-UI-SRCH-001 Tam məhsul adı ilə axtarış

tags: smoke

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Axtaris Input" elementine "iPhone Air" yaz ve Enter düymesine bas
* URL "/az/mehsullar?q=" içermelidir
* "Axtaris Basligi" elementin içinde "iPhone Air üzrə axtarış" yazısı var
* "iPhone Air Mehsul Adlari" elementlerinin sayı en az "1" olmalıdır

## TC-UI-SRCH-002 Brend adı ilə axtarışda nəticələrin uyğunluğu

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Axtaris Input" elementine "Samsung" yaz ve Enter düymesine bas
* "Axtaris Basligi" elementin içinde "Samsung üzrə axtarış" yazısı var
* "Samsung Mehsul Adlari" elementlerinin sayı en az "1" olmalıdır
* "Samsung Olmayan Mehsul Adlari" elementlerinin sayı "0" olmalıdır

## TC-UI-SRCH-003 Böyük-kiçik hərfin axtarış nəticəsinə təsir etməməsi (EP)

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Axtaris Input" elementine "iphone" yaz ve Enter düymesine bas
* "Axtaris Basligi" elementin içinde "üzrə axtarış" yazısı var
* "Axtaris Basligi" elementinin metnini "basliq" olaraq yadda saxla
* "Siyahi Mehsul Adi 1" elementinin metnini "ad1" olaraq yadda saxla
* "Siyahi Mehsul Adi 2" elementinin metnini "ad2" olaraq yadda saxla
* "Siyahi Mehsul Adi 3" elementinin metnini "ad3" olaraq yadda saxla
* "Siyahi Mehsul Adi 4" elementinin metnini "ad4" olaraq yadda saxla
* "Siyahi Mehsul Adi 5" elementinin metnini "ad5" olaraq yadda saxla
* "https://irshad.az/az" adresine keçid et
* "Axtaris Input" elementine "IPHONE" yaz ve Enter düymesine bas
* "xpath=//h1[@id='search-title'][translate(normalize-space(.),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')='${basliq}']" elementlerinin sayı "1" olmalıdır
* "Siyahi Mehsul Adi 1" elementinin metni "${ad1}" olmalıdır
* "Siyahi Mehsul Adi 2" elementinin metni "${ad2}" olmalıdır
* "Siyahi Mehsul Adi 3" elementinin metni "${ad3}" olmalıdır
* "Siyahi Mehsul Adi 4" elementinin metni "${ad4}" olmalıdır
* "Siyahi Mehsul Adi 5" elementinin metni "${ad5}" olmalıdır
* "https://irshad.az/az" adresine keçid et
* "Axtaris Input" elementine "iPhone" yaz ve Enter düymesine bas
* "xpath=//h1[@id='search-title'][translate(normalize-space(.),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')='${basliq}']" elementlerinin sayı "1" olmalıdır
* "Siyahi Mehsul Adi 1" elementinin metni "${ad1}" olmalıdır
* "Siyahi Mehsul Adi 2" elementinin metni "${ad2}" olmalıdır
* "Siyahi Mehsul Adi 3" elementinin metni "${ad3}" olmalıdır
* "Siyahi Mehsul Adi 4" elementinin metni "${ad4}" olmalıdır
* "Siyahi Mehsul Adi 5" elementinin metni "${ad5}" olmalıdır

## TC-UI-SRCH-004 Əvvəl və sonda boşluq olan sorğunun düzgün axtarılması

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Axtaris Input" elementine "iphone" yaz ve Enter düymesine bas
* "Axtaris Basligi" elementin içinde "üzrə axtarış" yazısı var
* "Axtaris Basligi" elementinin metnini "basliq" olaraq yadda saxla
* "Siyahi Mehsul Adi 1" elementinin metnini "ad1" olaraq yadda saxla
* "https://irshad.az/az" adresine keçid et
* "Axtaris Input" elementine "   iphone   " yaz ve Enter düymesine bas
* "xpath=//h1[@id='search-title'][translate(normalize-space(.),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')='${basliq}']" elementlerinin sayı "1" olmalıdır
* "Siyahi Mehsul Adi 1" elementinin metni "${ad1}" olmalıdır

## TC-UI-SRCH-005 Enter düyməsi və axtarış ikonu ilə axtarışın eyni nəticəni verməsi

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Axtaris Input" elementine "Samsung" yaz ve Enter düymesine bas
* "Axtaris Basligi" elementin içinde "Samsung üzrə axtarış" yazısı var
* "Axtaris Basligi" elementinin metnini "basliq" olaraq yadda saxla
* "Siyahi Mehsul Adi 1" elementinin metnini "ad1" olaraq yadda saxla
* "https://irshad.az/az" adresine keçid et
* "Axtaris Input" elementine "Samsung" yaz
* "Axtaris Lupa" elementine klik et
* "Axtaris Basligi" elementinin metni "${basliq}" olmalıdır
* "Siyahi Mehsul Adi 1" elementinin metni "${ad1}" olmalıdır

## TC-UI-SRCH-006 Axtarış nəticəsindən məhsul səhifəsinə keçid

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Axtaris Input" elementine "iPhone Air" yaz ve Enter düymesine bas
* "Axtaris Basligi" elementin içinde "iPhone Air üzrə axtarış" yazısı var
* "Siyahi Mehsul Adi 1" elementinin metnini "neticeAdi" olaraq yadda saxla
* "Siyahi Mehsul Adi 1" elementine klik et
* URL "/az/mehsullar/" içermelidir
* "PDP Basliq" elementinin metni "${neticeAdi}" olmalıdır

## TC-UI-SRCH-008 Azərbaycan hərfləri ilə axtarış

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Axtaris Input" elementine "ütü" yaz ve Enter düymesine bas
* "Axtaris Basligi" elementin içinde "ütü üzrə axtarış" yazısı var
* "Utu Mehsul Kartlari" elementlerinin sayı en az "1" olmalıdır

## TC-UI-SRCH-010 Model nömrəsi ilə axtarış

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Axtaris Input" elementine "17 Pro" yaz ve Enter düymesine bas
* "Axtaris Basligi" elementin içinde "17 Pro üzrə axtarış" yazısı var
* "iPhone 17 Pro Mehsul Adlari" elementlerinin sayı en az "1" olmalıdır

## TC-UI-SRCH-012 Axtarış sorğusunun nəticə səhifəsində axtarış sahəsində qalması

tags: search, usability, known-bug

BUG-UI-033: nəticə səhifəsində axtarış sahəsi təmizlənir — istifadəçi sorğunu düzəltmək üçün yenidən yazmalı olur.
Bug düzələndə known-bug teqi götürülür və ssenari regression-a qayıdır.

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Axtaris Input" elementine "Samsung" yaz ve Enter düymesine bas
* "Axtaris Basligi" elementin içinde "Samsung üzrə axtarış" yazısı var
* "Axtaris Input" elementinin "value" atributu "Samsung" olmalıdır

## TC-UI-SRCH-013 Mövcud olmayan sözlə axtarışda "nəticə yoxdur" vəziyyəti

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Axtaris Input" elementine "qwxzqwxz" yaz ve Enter düymesine bas
* "Axtaris Basligi" elementinin metni "qwxzqwxz üzrə axtarış heç bir nəticə vermədi" olmalıdır
* "Siyahi Mehsul Kartlari" elementlerinin sayı "0" olmalıdır

## TC-UI-CART-020 Uçdan-uca axın: axtarış → məhsul → səbət → say → silmə

tags: cart, e2e

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Axtaris Input" elementine "iPhone Air" yaz ve Enter düymesine bas
* "Axtaris Basligi" elementin içinde "iPhone Air üzrə axtarış" yazısı var
* Sehifenin tam yüklenmesini gözle
* "500" piksel vertical scroll et
* "A Karti Sekil Linki" elementine klik et
* URL "/az/mehsullar/iphone-air-256-gb-cloud-white" içermelidir
* "PDP Sebete Elave Button" elementine klik et
* "Header Sebet Sayi" elementinin metni "1" olmalıdır
* "https://irshad.az/az/sebet" adresine keçid et
* "Sebet Ilk Mehsul Adi" elementinin metni "iPhone Air 256 GB Cloud White" olmalıdır
* "Sebet Ilk Mehsul Plus" elementine klik et
* "Sebet Ilk Mehsul Sayi" input deyeri "2" olmalıdır
* "Sebet Cemi 2 Ededin Qiymetine Beraber" elementlerinin sayı "1" olmalıdır
* "Sebet Ilk Mehsul Sil" elementine klik et
* "Sebet Mehsul Setirleri" elementlerinin sayı "0" olmalıdır
* "Header Sebet Sayi" görünmemelidir

## TC-UI-SRCH-014 Boş axtarış sahəsi ilə axtarış (EP: boş dəyər)

tags: search, negative

Ana səhifədən boş sorğu göndəriləndə sayt xəta vermir: boş q ilə ümumi "Məhsullar" səhifəsini açır (15.10.2026 müşahidəsi).

* Brauzeri aç ve keçid et "https://irshad.az/az"
* Sehifenin tam yüklenmesini gözle
* "Axtaris Input" elementine "" yaz ve Enter düymesine bas
* URL "/az/mehsullar?q=" içermelidir
* Sehifenin tam yüklenmesini gözle
* "Breadcrumb Elementleri" elementlerinin sayı "2" olmalıdır
* Sehifede "Məhsullar" yazısı olmalıdır
* "Siyahi Gorunen Qiymetler" elementlerinin sayı en az "1" olmalıdır

## TC-UI-SRCH-015 Yalnız boşluqlardan ibarət axtarış (EP: boşluq)

tags: search, negative

Yalnız boşluqdan ibarət sorğu boş sorğu kimi işlənməlidir (TC-UI-SRCH-014 ilə eyni davranış): ümumi "Məhsullar" səhifəsi, xəta yoxdur.

* Brauzeri aç ve keçid et "https://irshad.az/az"
* Sehifenin tam yüklenmesini gözle
* "Axtaris Input" elementine "     " yaz ve Enter düymesine bas
* URL "/az/mehsullar?q=" içermelidir
* Sehifenin tam yüklenmesini gözle
* "Breadcrumb Elementleri" elementlerinin sayı "2" olmalıdır
* Sehifede "Məhsullar" yazısı olmalıdır
* "Siyahi Gorunen Qiymetler" elementlerinin sayı en az "1" olmalıdır

## TC-UI-SRCH-019 Xüsusi simvollar və SQL tipli sorğu ilə axtarış

tags: search, negative, security, known-bug

BUG-UI-011: "%" joker (wildcard) kimi işlənir və bütün kataloqu qaytarır. SQL tipli sorğu xətasız işlənir (keçir), "%" yoxlaması bug-ı tutur.
Bug düzələndə known-bug teqi götürülür və ssenari regression-a qayıdır.

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Axtaris Input" elementine "' OR 1=1 --" yaz ve Enter düymesine bas
* "Axtaris Basligi" elementin içinde "üzrə axtarış" yazısı var
* "xpath=//*[contains(normalize-space(.),'SQLSTATE') or contains(normalize-space(.),'syntax error') or contains(normalize-space(.),'Stack trace')]" elementlerinin sayı "0" olmalıdır
* "https://irshad.az/az" adresine keçid et
* "Axtaris Input" elementine "%" yaz ve Enter düymesine bas
* "Axtaris Basligi" elementin içinde "% üzrə axtarış" yazısı var
* "xpath=//div[@id='productGridItems']//a[contains(@class,'product__name')][not(contains(normalize-space(.),'%'))]" elementlerinin sayı "0" olmalıdır

