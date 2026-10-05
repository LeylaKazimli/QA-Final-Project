# GRAD-201 — Virtual kart buraxmaq (POST /cards)

Bu spec öz sandbox-ında işləyir (login-user1-card.json), login keşlidir (spec üçün 1 dəfə).

Kart limiti (3 ACTIVE/FROZEN) testlərə qarışmasın deyə kart açan hər ssenari sonda
öz kartını LOST ilə bloklayır (BLOCKED kart limitə sayılmır — TC-CARD-020).
Beləliklə sandbox-da eyni anda ən çox 1 aktiv kart olur və ssenarilərin sırası önəmli deyil.
Limit testləri (TC-CARD-019, TC-CARD-020) ayrıca spec-dədir: GRAD-201_card_limit.spec.

Manual qalan TC-lər (Excel-ə uyğun): TC-CARD-005, TC-CARD-012, TC-CARD-013.

* "/auth/login" ünvanına "login-user1-card.json" ile login ol ve "token" tokenini yadda saxla

## TC-CARD-001 Düzgün məlumatla virtual kartın buraxılması
tags: api, regression, GRAD-201, positive

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key          |value   |
   |-------------|--------|
   |accountId    |acc_002 |
   |initialAmount|100     |
   |label        |Kommunal|
* "POST" sorğusu gönder "/cards"
* Status kodunun "201" olmalıdır
* Json cavabını cedvel ile yoxla
   |path       |value                   |
   |-----------|------------------------|
   |id         |@regex:^vcd_[a-z0-9]{8}$|
   |status     |ACTIVE                  |
   |currency   |AZN                     |
   |label      |Kommunal                |
   |blockReason|null                    |
   |blockedAt  |null                    |
* Json cavabında "availableBalance" deyeri "==" "100" olmalıdır
* Json cavabında "limits.dailyOnline" deyeri "==" "500" olmalıdır
* Json cavabında "limits.perTransaction" deyeri "==" "300" olmalıdır
* Json cavabında "spentToday" deyeri "==" "0" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Header "Location" deyerinde "/cards/${cardId}" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARD-002 Yeni kartın nömrəsinin (maskedPan) və bitmə tarixinin (expiry) formatı
tags: api, regression, GRAD-201, positive

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key          |value   |
   |-------------|--------|
   |accountId    |acc_002 |
   |initialAmount|100     |
   |label        |Kommunal|
* "POST" sorğusu gönder "/cards"
* Status kodunun "201" olmalıdır
* Json cavabında "maskedPan" deyeri "^4169 73[*][*] [*]{4} [0-9]{4}$" regex-ine uyğun olmalıdır
* Json cavabında "expiry" deyeri "^(0[1-9]|1[0-2])/[0-9]{2}$" regex-ine uyğun olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARD-003 Ad (label) göndərilmədikdə kartın adsız (null) yaradılması
tags: api, regression, GRAD-201, positive

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key          |value  |
   |-------------|-------|
   |accountId    |acc_002|
   |initialAmount|50     |
* "POST" sorğusu gönder "/cards"
* Status kodunun "201" olmalıdır
* Json cavabında "label" deyeri null olmalıdır
* Json cavabında "availableBalance" deyeri "==" "50" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARD-004 USD hesabından kart açıldıqda kartın valyutasının USD olması (balansın tamamı)
tags: api, regression, GRAD-201, positive, bva

user2 öz sandbox-ında işləyir (login-user2-card.json).

* "/auth/login" ünvanına "login-user2-card.json" ile login ol ve "token" tokenini yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key          |value  |
   |-------------|-------|
   |accountId    |acc_003|
   |initialAmount|890.5  |
* "POST" sorğusu gönder "/cards"
* Status kodunun "201" olmalıdır
* Json cavabında "currency" deyeri "USD" beraberdir
* Json cavabında "status" deyeri "ACTIVE" beraberdir
* Json cavabında "availableBalance" deyeri "==" "890.5" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARD-006 Karta 0.99 yükləmək cəhdinin rədd edilməsi (BVA: min-0.01)
tags: api, regression, GRAD-201, negative, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key          |value  |
   |-------------|-------|
   |accountId    |acc_002|
   |initialAmount|0.99   |
   |label        |Test   |
* "POST" sorğusu gönder "/cards"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "1" olmalıdır
* Json cavabında "details[0].field" deyeri "initialAmount" beraberdir

## TC-CARD-007 Karta 1.00 yükləməklə kartın açılması (BVA: min)
tags: api, regression, GRAD-201, positive, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key          |value  |
   |-------------|-------|
   |accountId    |acc_002|
   |initialAmount|1.00   |
   |label        |Minimum|
* "POST" sorğusu gönder "/cards"
* Status kodunun "201" olmalıdır
* Json cavabında "availableBalance" deyeri "==" "1" olmalıdır
* Json cavabında "status" deyeri "ACTIVE" beraberdir
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARD-008 Karta 1000.00 yükləməklə kartın açılması (BVA: max)
tags: api, regression, GRAD-201, positive, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key          |value   |
   |-------------|--------|
   |accountId    |acc_002 |
   |initialAmount|1000.00 |
   |label        |Maksimum|
* "POST" sorğusu gönder "/cards"
* Status kodunun "201" olmalıdır
* Json cavabında "availableBalance" deyeri "==" "1000" olmalıdır
* Json cavabında "status" deyeri "ACTIVE" beraberdir
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARD-009 Karta 1000.01 yükləmək cəhdinin rədd edilməsi (BVA: max+0.01)
tags: api, regression, GRAD-201, negative, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key          |value  |
   |-------------|-------|
   |accountId    |acc_002|
   |initialAmount|1000.01|
   |label        |Test   |
* "POST" sorğusu gönder "/cards"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "1" olmalıdır
* Json cavabında "details[0].field" deyeri "initialAmount" beraberdir

## TC-CARD-010 Məbləğ mətn kimi ("50") göndəriləndə kartın açılmaması
tags: api, regression, GRAD-201, negative

Body fayldan göndərilir, çünki cədvəldə "50" avtomatik rəqəmə çevrilir — bizə isə məhz mətn lazımdır.

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "card-amount-as-string.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "1" olmalıdır
* Json cavabında "details[0].field" deyeri "initialAmount" beraberdir

## TC-CARD-011 Məbləğdə 3 onluq rəqəm (10.555) olduqda kartın açılmaması
tags: api, regression, GRAD-201, negative

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key          |value  |
   |-------------|-------|
   |accountId    |acc_002|
   |initialAmount|10.555 |
   |label        |Test   |
* "POST" sorğusu gönder "/cards"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "1" olmalıdır
* Json cavabında "details[0].field" deyeri "initialAmount" beraberdir

## TC-CARD-014 Hesab (accountId) göndərilmədikdə kartın açılmaması
tags: api, regression, GRAD-201, negative

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key          |value|
   |-------------|-----|
   |initialAmount|100  |
   |label        |Test |
* "POST" sorğusu gönder "/cards"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "1" olmalıdır
* Json cavabında "details[0].field" deyeri "accountId" beraberdir

## TC-CARD-015 Başqa istifadəçinin hesabından kart açmaq cəhdinin rədd edilməsi
tags: api, regression, GRAD-201, negative, security

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key          |value  |
   |-------------|-------|
   |accountId    |acc_003|
   |initialAmount|100    |
   |label        |Test   |
* "POST" sorğusu gönder "/cards"
* Status kodunun "403" olmalıdır
* Json cavabında "code" deyeri "FORBIDDEN" beraberdir
* Json cavabında "id" açarı olmamalıdır

## TC-CARD-016 Mövcud olmayan hesabdan kart açmaq cəhdinin rədd edilməsi
tags: api, regression, GRAD-201, negative

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key          |value  |
   |-------------|-------|
   |accountId    |acc_999|
   |initialAmount|100    |
   |label        |Test   |
* "POST" sorğusu gönder "/cards"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "ACCOUNT_NOT_FOUND" beraberdir

## TC-CARD-017 Hesab balansından çox məbləğlə kart açmaq cəhdinin rədd edilməsi
tags: api, regression, GRAD-201, negative, bva

user2 (acc_003, balans 890.50) öz sandbox-ında işləyir.

* "/auth/login" ünvanına "login-user2-card.json" ile login ol ve "token" tokenini yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key          |value  |
   |-------------|-------|
   |accountId    |acc_003|
   |initialAmount|891    |
* "POST" sorğusu gönder "/cards"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INSUFFICIENT_FUNDS" beraberdir

## TC-CARD-018 Token olmadan kart açmaq cəhdinin rədd edilməsi
tags: api, regression, GRAD-201, negative, auth

* Yeni API sorğusu hazırla
* Body-ni cedvelden qur
   |key          |value  |
   |-------------|-------|
   |accountId    |acc_002|
   |initialAmount|100    |
   |label        |Test   |
* "POST" sorğusu gönder "/cards"
* Status kodunun "401" olmalıdır
* Json cavabında "error" açarı mövcud olmalıdır
* Json cavabında "id" açarı olmamalıdır
