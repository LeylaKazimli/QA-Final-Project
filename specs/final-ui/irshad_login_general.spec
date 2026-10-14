# irshad.az — Giriş səhifəsi və ümumi yoxlamalar

Test mühiti: https://irshad.az
Excel: "UI Test Cases" vərəqi (TS-UI-01 Ümumi, TS-UI-07 Giriş)
Qeyd: tam 9 rəqəmli nömrə ilə "Daxil ol" BASILMIR — həmin nömrəyə real SMS gedir.

tags: ui, irshad, login

## TC-UI-GEN-001 HTTP ünvanının HTTPS-ə yönləndirilməsi

tags: general

* Brauzeri aç ve keçid et "http://irshad.az"
* Sehifenin tam yüklenmesini gözle
* URL "https://" içermelidir
* URL "irshad.az" içermelidir
* Sehifede "Kataloq" yazısı olmalıdır

## TC-UI-GEN-002 Dil hissəsi olmayan ünvanda ana səhifənin açılması

tags: general

* Brauzeri aç ve keçid et "https://irshad.az"
* Sehifenin tam yüklenmesini gözle
* URL "https://irshad.az/" olmalıdır
* Sehifede "Kataloq" yazısı olmalıdır
* Sehifede "Azərbaycan dili" yazısı olmalıdır

## TC-UI-GEN-003 www prefiksli ünvanın açılması

tags: general

* Brauzeri aç ve keçid et "https://www.irshad.az"
* Sehifenin tam yüklenmesini gözle
* URL "irshad.az" içermelidir
* Sehifede "Kataloq" yazısı olmalıdır

## TC-UI-HOME-006 "Şəxsi kabinet"ə klikləyəndə giriş səhifəsinin açılması

tags: home, login

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Şəxsi kabinet" metnli elemente klik et
* URL "/az/giris" içermelidir
* "Giris Basligi" görünür olmalıdır
* "Telefon Input" görünür olmalıdır

## TC-UI-LOGIN-001 Giriş səhifəsinin elementlərlə düzgün açılması

* Brauzeri aç ve keçid et "https://irshad.az/az/giris"
* "Telefon Input" görsensin deye maksimum "10" saniye gözle
* Sehife başlığında "Giriş" olmalıdır
* "Giris Basligi" görünür olmalıdır
* Sehifede "Telefon" yazısı olmalıdır
* "Telefon Input" elementinin "placeholder" atributu "+(994) (00) 000-00-00" olmalıdır
* "Daxil ol Button" görünür olmalıdır

## TC-UI-LOGIN-002 Boş telefon sahəsi ilə girişin qarşısının alınması

* Brauzeri aç ve keçid et "https://irshad.az/az/giris"
* "Telefon Input" görsensin deye maksimum "10" saniye gözle
* "Telefon Input" elementinin "required" atributu "true" olmalıdır
* "Daxil ol Button" elementine klik et
* URL "/az/giris" içermelidir

## TC-UI-LOGIN-003 8 rəqəmli nömrə ilə girişin qarşısının alınması

* Brauzeri aç ve keçid et "https://irshad.az/az/giris"
* "Telefon Input" görsensin deye maksimum "10" saniye gözle
* "Telefon Input" elementine "50123456" yaz
* "Daxil ol Button" elementine klik et
* "Telefon Xeta Mesaji" görsensin deye maksimum "5" saniye gözle
* URL "/az/giris" içermelidir

## TC-UI-LOGIN-004 10-cu rəqəmin sahəyə yazılmaması

* Brauzeri aç ve keçid et "https://irshad.az/az/giris"
* "Telefon Input" görsensin deye maksimum "10" saniye gözle
* "Telefon Input" elementine "5012345678" yaz
* "Telefon Input" input deyeri "+994 (50) 123-45-67" olmalıdır
* "Telefon Input" elementini temizle

## TC-UI-LOGIN-005 Telefon sahəsinə hərf daxil edilməsi

* Brauzeri aç ve keçid et "https://irshad.az/az/giris"
* "Telefon Input" görsensin deye maksimum "10" saniye gözle
* "Telefon Input" elementine "abcdef" yaz
* "Telefon Input" input deyeri "+994 (" olmalıdır

## TC-UI-LOGIN-019 OTP səhifəsinin birbaşa URL ilə açılması

* Brauzeri aç ve keçid et "https://irshad.az/az/giris-otp-tesdiqle"
* Sehifenin tam yüklenmesini gözle
* Sehifede "Axtardığınız səhifə tapılmadı" yazısı olmalıdır
* Sehifede "404" yazısı olmalıdır

## TC-UI-LOGIN-012 Giriş səhifəsində loqo ilə ana səhifəyə qayıtmaq

tags: login, navigation

* Brauzeri aç ve keçid et "https://irshad.az/az/giris"
* "Giris Basligi" görünür olmalıdır
* "Giris Sehifesi Logo" elementine klik et
* URL "https://irshad.az/az" olmalıdır
* "Kataloq Button" görünür olmalıdır

