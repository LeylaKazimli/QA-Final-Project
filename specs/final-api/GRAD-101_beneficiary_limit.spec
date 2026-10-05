# GRAD-101 — Alıcı limiti (maksimum 10)

Limit testi digər testlərin datasına qarışmasın deyə AYRICA, təmiz sandbox-da işləyir
(login-user1-ben-limit.json). Ssenari 10 alıcını özü əlavə edir, sonra 11-cini yoxlayır.

* "/auth/login" ünvanına "login-user1-ben-limit.json" ile login ol ve "token" tokenini yadda saxla

## TC-BEN-017 Siyahıda 10 alıcı olduqda 11-cinin əlavə edilməməsi (BVA: max+1)
tags: api, regression, GRAD-101, negative, bva

* "Alıcı Bir" adlı və "AZ12AIIB40060019440100000101" IBAN-lı AZN alıcısını əlavə et
* "Alıcı İki" adlı və "AZ12AIIB40060019440100000102" IBAN-lı AZN alıcısını əlavə et
* "Alıcı Üç" adlı və "AZ12AIIB40060019440100000103" IBAN-lı AZN alıcısını əlavə et
* "Alıcı Dörd" adlı və "AZ12AIIB40060019440100000104" IBAN-lı AZN alıcısını əlavə et
* "Alıcı Beş" adlı və "AZ12AIIB40060019440100000105" IBAN-lı AZN alıcısını əlavə et
* "Alıcı Altı" adlı və "AZ12AIIB40060019440100000106" IBAN-lı AZN alıcısını əlavə et
* "Alıcı Yeddi" adlı və "AZ12AIIB40060019440100000107" IBAN-lı AZN alıcısını əlavə et
* "Alıcı Səkkiz" adlı və "AZ12AIIB40060019440100000108" IBAN-lı AZN alıcısını əlavə et
* "Alıcı Doqquz" adlı və "AZ12AIIB40060019440100000109" IBAN-lı AZN alıcısını əlavə et
* "Alıcı On" adlı və "AZ12AIIB40060019440100000110" IBAN-lı AZN alıcısını əlavə et
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key     |value                       |
   |--------|----------------------------|
   |fullName|Onbirinci Alıcı             |
   |iban    |AZ12AIIB40060019440100000111|
   |currency|AZN                         |
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "LIMIT_REACHED" beraberdir
* Json cavabında "limit" deyeri "10" beraberdir
