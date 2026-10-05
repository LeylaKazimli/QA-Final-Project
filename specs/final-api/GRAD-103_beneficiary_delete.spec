# GRAD-103 — Alıcını silmək (DELETE /beneficiaries/{id})

Bu spec öz sandbox-ında işləyir (login-user1-bend.json), login keşlidir (spec üçün 1 dəfə).
Hər ssenari silinəcək alıcını ÖZÜ yaradır və id-sini "benId" kimi yadda saxlayır,
ona görə ssenarilər bir-birindən və icra sırasından asılı deyil.

Manual qalan TC-lər (Excel-ə uyğun): TC-BEND-004, TC-BEND-008, TC-BEND-010.

* "/auth/login" ünvanına "login-user1-bend.json" ile login ol ve "token" tokenini yadda saxla

## TC-BEND-001 Mövcud alıcının uğurla silinməsi
tags: api, regression, GRAD-103, positive

* "Silinəcək Alıcı" adlı və "AZ12AIIB40060019440100000201" IBAN-lı AZN alıcısını əlavə et
* Json cavabında "id" deyerini "benId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "DELETE" sorğusu gönder "/beneficiaries/${benId}"
* Status kodunun "204" olmalıdır

## TC-BEND-002 Silinmiş alıcının siyahıdan həqiqətən yox olması
tags: api, regression, GRAD-103, positive

Əvvəl alıcının siyahıda olduğu təsdiqlənir (total = 1), silindikdən sonra yox olduğu (total = 0).

* "Yoxlanış Nümunəsi" adlı və "AZ12AIIB40060019440100000202" IBAN-lı AZN alıcısını əlavə et
* Json cavabında "id" deyerini "benId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "Yoxlanış"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items[0].id" deyeri "benId" ile eynidir
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "DELETE" sorğusu gönder "/beneficiaries/${benId}"
* Status kodunun "204" olmalıdır
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "Yoxlanış"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır

## TC-BEND-003 Silinmiş alıcının eyni IBAN ilə yenidən əlavə edilə bilməsi
tags: api, regression, GRAD-103, positive

* "Təkrar Alıcı" adlı və "AZ12AIIB40060019440100000203" IBAN-lı AZN alıcısını əlavə et
* Json cavabında "id" deyerini "benId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "DELETE" sorğusu gönder "/beneficiaries/${benId}"
* Status kodunun "204" olmalıdır
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key     |value                       |
   |--------|----------------------------|
   |fullName|Təkrar Alıcı                |
   |iban    |AZ12AIIB40060019440100000203|
   |currency|AZN                         |
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "201" olmalıdır
* Json cavabında "iban" deyeri "AZ12AIIB40060019440100000203" beraberdir
* Json cavabında "id" deyeri "^ben_[a-z0-9]{8}$" regex-ine uyğun olmalıdır
* Json cavabında "id" deyeri "benId" ile ferqlidir

## TC-BEND-005 Artıq silinmiş alıcının ikinci dəfə silinə bilməməsi
tags: api, regression, GRAD-103, negative

* "İkiqat Silmə" adlı və "AZ12AIIB40060019440100000205" IBAN-lı AZN alıcısını əlavə et
* Json cavabında "id" deyerini "benId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "DELETE" sorğusu gönder "/beneficiaries/${benId}"
* Status kodunun "204" olmalıdır
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "DELETE" sorğusu gönder "/beneficiaries/${benId}"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## TC-BEND-006 Başqa istifadəçinin alıcısını silmək cəhdinin rədd edilməsi (404, 403 yox)
tags: api, regression, GRAD-103, negative, security

user1 alıcı yaradır, user2 onu silməyə çalışır. Sonra user1 ilə alıcının yerində qaldığı yoxlanılır.

* "Başqasının Alıcısı" adlı və "AZ12AIIB40060019440100000206" IBAN-lı AZN alıcısını əlavə et
* Json cavabında "id" deyerini "benId" olaraq yadda saxla
* "/auth/login" ünvanına "login-user2-bend.json" ile login ol ve "token" tokenini yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "DELETE" sorğusu gönder "/beneficiaries/${benId}"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir
* "/auth/login" ünvanına "login-user1-bend.json" ile login ol ve "token" tokenini yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "Başqasının"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items[0].id" deyeri "benId" ile eynidir

## TC-BEND-007 Mövcud olmayan id ilə alıcı silmək cəhdinin rədd edilməsi
tags: api, regression, GRAD-103, negative

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "DELETE" sorğusu gönder "/beneficiaries/ben_00000000"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## TC-BEND-009 Token olmadan alıcı silmək cəhdinin rədd edilməsi
tags: api, regression, GRAD-103, negative, auth

Tokensiz silmə cəhdindən sonra user1 ilə alıcının silinmədiyi yoxlanılır.

* "Tokensiz Silmə" adlı və "AZ12AIIB40060019440100000209" IBAN-lı AZN alıcısını əlavə et
* Json cavabında "id" deyerini "benId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* "DELETE" sorğusu gönder "/beneficiaries/${benId}"
* Status kodunun "401" olmalıdır
* Json cavabında "error" açarı mövcud olmalıdır
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "Tokensiz"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items[0].id" deyeri "benId" ile eynidir
