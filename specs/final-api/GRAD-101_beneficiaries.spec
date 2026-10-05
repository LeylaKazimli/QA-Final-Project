# GRAD-101 — Yeni alıcı əlavə etmək (POST /beneficiaries)

Bu spec öz sandbox-ında işləyir (login-user1-ben.json).
Login keşlidir: bütün spec üçün real login cəmi 1 dəfə olur (@BeforeClass-ın Gauge qarşılığı),
ona görə ssenarilər eyni sandbox-u və bir-birinin datasını görür.
Manual qalan TC-lər (Excel-ə uyğun): TC-BEN-010, TC-BEN-012, TC-BEN-019, TC-BEN-020.

* "/auth/login" ünvanına "login-user1-ben.json" ile login ol ve "token" tokenini yadda saxla

## TC-BEN-001 Bütün sahələr düzgün olduqda yeni alıcının əlavə edilməsi
tags: api, regression, GRAD-101, positive

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key     |value                       |
   |--------|----------------------------|
   |fullName|Nigar Əliyeva               |
   |iban    |AZ77AIIB40060019440123456789|
   |currency|AZN                         |
   |nickname|Anam                        |
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "201" olmalıdır
* Json cavabını cedvel ile yoxla
   |path     |value                       |
   |---------|----------------------------|
   |id       |@regex:^ben_[a-z0-9]{8}$    |
   |fullName |Nigar Əliyeva               |
   |iban     |AZ77AIIB40060019440123456789|
   |currency |AZN                         |
   |nickname |Anam                        |
   |createdAt|@notEmpty                   |
* Json cavabında "ibanMasked" deyeri "AZ77 **** **** **** **** 6789" beraberdir
* Json cavabında "id" deyerini "benId" olaraq yadda saxla
* Header "Location" deyerinde "/beneficiaries/${benId}" olmalıdır

## TC-BEN-002 Boşluqlu və kiçik hərfli IBAN-ın avtomatik düzəldilib qəbul edilməsi
tags: api, regression, GRAD-101, positive

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key     |value                             |
   |--------|----------------------------------|
   |fullName|Leyla Həsənova                    |
   |iban    |az12 aiib 4006 0019 4401 0000 0002|
   |currency|AZN                               |
   |nickname|Bacım                             |
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "201" olmalıdır
* Json cavabında "iban" deyeri "AZ12AIIB40060019440100000002" beraberdir
* Json cavabında "ibanMasked" deyeri "AZ12 **** **** **** **** 0002" beraberdir

## TC-BEN-003 Ləqəb göndərilmədikdə alıcının ləqəbsiz (null) yaradılması
tags: api, regression, GRAD-101, positive

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key     |value                       |
   |--------|----------------------------|
   |fullName|Rauf Quliyev                |
   |iban    |AZ12AIIB40060019440100000003|
   |currency|USD                         |
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "201" olmalıdır
* Json cavabında "nickname" deyeri null olmalıdır
* Json cavabında "currency" deyeri "USD" beraberdir
* Json cavabında "fullName" deyeri "Rauf Quliyev" beraberdir

## TC-BEN-004 Bir neçə sahə səhv olduqda hər səhvin ayrıca göstərilməsi
tags: api, regression, GRAD-101, negative

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key     |value|
   |--------|-----|
   |fullName|A    |
   |iban    |123  |
   |currency|GBP  |
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "3" olmalıdır
* Json cavabında "details.field" deyerinde "fullName" olmalıdır
* Json cavabında "details.field" deyerinde "iban" olmalıdır
* Json cavabında "details.field" deyerinde "currency" olmalıdır
* Json cavabında "details.findAll { it.message }.size()" deyeri "3" beraberdir

## TC-BEN-005 Ad 1 simvol olduqda alıcının əlavə edilməməsi (BVA: min-1)
tags: api, regression, GRAD-101, negative, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key     |value                       |
   |--------|----------------------------|
   |fullName|A                           |
   |iban    |AZ12AIIB40060019440100000005|
   |currency|AZN                         |
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "1" olmalıdır
* Json cavabında "details[0].field" deyeri "fullName" beraberdir

## TC-BEN-006 Ad 2 simvol olduqda alıcının əlavə edilməsi (BVA: min)
tags: api, regression, GRAD-101, positive, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key     |value                       |
   |--------|----------------------------|
   |fullName|Al                          |
   |iban    |AZ12AIIB40060019440100000006|
   |currency|AZN                         |
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "201" olmalıdır
* Json cavabında "fullName" deyeri "Al" beraberdir
* Json cavabında "id" deyeri "^ben_[a-z0-9]{8}$" regex-ine uyğun olmalıdır

## TC-BEN-007 Ad 50 simvol olduqda alıcının əlavə edilməsi (BVA: max)
tags: api, regression, GRAD-101, positive, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key     |value                                             |
   |--------|--------------------------------------------------|
   |fullName|Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa|
   |iban    |AZ12AIIB40060019440100000007                      |
   |currency|AZN                                               |
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "201" olmalıdır
* Json cavabında "fullName" deyeri "Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" beraberdir

## TC-BEN-008 Ad 51 simvol olduqda alıcının əlavə edilməməsi (BVA: max+1)
tags: api, regression, GRAD-101, negative, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key     |value                                              |
   |--------|---------------------------------------------------|
   |fullName|Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa|
   |iban    |AZ12AIIB40060019440100000008                       |
   |currency|AZN                                                |
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "1" olmalıdır
* Json cavabında "details[0].field" deyeri "fullName" beraberdir

## TC-BEN-009 Ad hərflə başlamadıqda alıcının əlavə edilməməsi
tags: api, regression, GRAD-101, negative

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key     |value                       |
   |--------|----------------------------|
   |fullName|---                         |
   |iban    |AZ12AIIB40060019440100000009|
   |currency|AZN                         |
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "1" olmalıdır
* Json cavabında "details[0].field" deyeri "fullName" beraberdir

## TC-BEN-011 Dəstəklənməyən valyuta (GBP) ilə alıcının əlavə edilməməsi
tags: api, regression, GRAD-101, negative

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key     |value                       |
   |--------|----------------------------|
   |fullName|Nigar Əliyeva               |
   |iban    |AZ12AIIB40060019440100000011|
   |currency|GBP                         |
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "1" olmalıdır
* Json cavabında "details[0].field" deyeri "currency" beraberdir

## TC-BEN-013 IBAN 27 simvol olduqda alıcının əlavə edilməməsi (BVA)
tags: api, regression, GRAD-101, negative, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key     |value                      |
   |--------|---------------------------|
   |fullName|Nigar Əliyeva              |
   |iban    |AZ12AIIB4006001944010000001|
   |currency|AZN                        |
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "1" olmalıdır
* Json cavabında "details[0].field" deyeri "iban" beraberdir

## TC-BEN-014 Siyahıda olan IBAN-ın ikinci dəfə əlavə edilməməsi
tags: api, regression, GRAD-101, negative

Ssenari öz datasını özü yaradır: əvvəl alıcı əlavə olunur, sonra eyni IBAN təkrar göndərilir.

* "Tural Babayev" adlı və "AZ12AIIB40060019440100000014" IBAN-lı AZN alıcısını əlavə et
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key     |value                       |
   |--------|----------------------------|
   |fullName|Tural Babayev               |
   |iban    |AZ12AIIB40060019440100000014|
   |currency|AZN                         |
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "BENEFICIARY_EXISTS" beraberdir

## TC-BEN-015 Mövcud ləqəbin böyük hərflə təkrar istifadəsinin qadağan olunması
tags: api, regression, GRAD-101, negative

Ssenari öz datasını özü yaradır: əvvəl "Xala" ləqəbli alıcı əlavə olunur, sonra "XALA" göndərilir.

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key     |value                       |
   |--------|----------------------------|
   |fullName|Gülnarə Həsənova            |
   |iban    |AZ12AIIB40060019440100000150|
   |currency|AZN                         |
   |nickname|Xala                        |
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "201" olmalıdır
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key     |value                       |
   |--------|----------------------------|
   |fullName|Səbinə Məmmədova            |
   |iban    |AZ12AIIB40060019440100000015|
   |currency|AZN                         |
   |nickname|XALA                        |
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "NICKNAME_TAKEN" beraberdir

## TC-BEN-016 İstifadəçinin öz hesabının IBAN-ını alıcı kimi əlavə edə bilməməsi
tags: api, regression, GRAD-101, negative

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key     |value                       |
   |--------|----------------------------|
   |fullName|Test User                   |
   |iban    |AZ29NABZ00000000137010002855|
   |currency|AZN                         |
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "OWN_ACCOUNT" beraberdir

## TC-BEN-018 Token olmadan alıcı əlavə etmək cəhdinin rədd edilməsi
tags: api, regression, GRAD-101, negative, auth

* Yeni API sorğusu hazırla
* Body-ni cedvelden qur
   |key     |value                       |
   |--------|----------------------------|
   |fullName|Kamran Əliyev               |
   |iban    |AZ12AIIB40060019440100000028|
   |currency|AZN                         |
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "401" olmalıdır
* Json cavabında "error" açarı mövcud olmalıdır
* Json cavabında "id" açarı olmamalıdır
