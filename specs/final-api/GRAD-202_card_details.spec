# GRAD-202 — Kart məlumatına baxmaq (GET /cards/{id})

Bu spec öz sandbox-ında işləyir (login-user1-cardg.json), login keşlidir (spec üçün 1 dəfə).
Hər ssenari öz kartını özü açır və sonda LOST ilə bloklayır (3 kart limitinə qarışmamaq üçün).

Manual qalan TC-lər (Excel-ə uyğun): TC-CARDG-003, TC-CARDG-005, TC-CARDG-009.

* "/auth/login" ünvanına "login-user1-cardg.json" ile login ol ve "token" tokenini yadda saxla

## TC-CARDG-001 Yeni kartın məlumatlarının düzgün qaytarılması (POST cavabı ilə eyni)
tags: api, regression, GRAD-202, positive

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
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Json cavabında "maskedPan" deyerini "kartPan" olaraq yadda saxla
* Json cavabında "expiry" deyerini "kartExpiry" olaraq yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/cards/${cardId}"
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "cardId" ile eynidir
* Json cavabında "maskedPan" deyeri "kartPan" ile eynidir
* Json cavabında "expiry" deyeri "kartExpiry" ile eynidir
* Json cavabını cedvel ile yoxla
   |path    |value   |
   |--------|--------|
   |status  |ACTIVE  |
   |currency|AZN     |
   |label   |Kommunal|
* Json cavabında "availableBalance" deyeri "==" "100" olmalıdır
* Json cavabında "spentToday" deyeri "==" "0" olmalıdır
* Json cavabında "limits.dailyOnline" deyeri "==" "500" olmalıdır
* Json cavabında "limits.perTransaction" deyeri "==" "300" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARDG-002 Ödənişdən sonra kart balansının və bugünkü xərcin yenilənməsi
tags: api, regression, GRAD-202, positive

CityNet-ə 50 AZN ödəniş: komissiya 0.50, cəmi (total) 50.50 → balans 100 - 50.50 = 49.50.

* "Odenis Karti" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "cardg-${random.uuid}"
* Body-ni cedvelden qur
   |key         |value    |
   |------------|---------|
   |cardId      |${cardId}|
   |billerId    |citynet  |
   |subscriberNo|CN123456 |
   |amount      |50       |
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "total" deyeri "==" "50.5" olmalıdır
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/cards/${cardId}"
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyeri "==" "49.5" olmalıdır
* Json cavabında "spentToday" deyeri "==" "50.5" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARDG-004 Kartdakı pul sahələrinin rəqəm (number) tipində qaytarılması
tags: api, regression, GRAD-202, positive

* "Tip Yoxlamasi" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/cards/${cardId}"
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyerinin tipi "number" olmalıdır
* Json cavabında "spentToday" deyerinin tipi "number" olmalıdır
* Json cavabında "limits.dailyOnline" deyerinin tipi "number" olmalıdır
* Json cavabında "limits.perTransaction" deyerinin tipi "number" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARDG-006 Başqa istifadəçinin kartına baxmaq cəhdinin rədd edilməsi (404, 403 yox)
tags: api, regression, GRAD-202, negative, security

user1 kart açır, user2 ona baxmağa çalışır. Sonra user1-ə qayıdıb kart bloklanır (təmizlik).

* "Basqasinin Karti" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "/auth/login" ünvanına "login-user2-cardg.json" ile login ol ve "token" tokenini yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/cards/${cardId}"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir
* Json cavabında "maskedPan" açarı olmamalıdır
* Json cavabında "availableBalance" açarı olmamalıdır
* "/auth/login" ünvanına "login-user1-cardg.json" ile login ol ve "token" tokenini yadda saxla
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARDG-007 Mövcud olmayan karta baxmaq cəhdinin rədd edilməsi
tags: api, regression, GRAD-202, negative

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/cards/vcd_00000000"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## TC-CARDG-008 Token olmadan karta baxmaq cəhdinin rədd edilməsi
tags: api, regression, GRAD-202, negative, auth

* "Tokensiz Baxis" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* "GET" sorğusu gönder "/cards/${cardId}"
* Status kodunun "401" olmalıdır
* Json cavabında "error" açarı mövcud olmalıdır
* Json cavabında "maskedPan" açarı olmamalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla
