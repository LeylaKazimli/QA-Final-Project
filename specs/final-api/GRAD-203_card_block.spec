# GRAD-203 — Kartı bloklamaq / dondurmaq (POST /cards/{id}/block)

State transition (vəziyyət keçidləri):
  ACTIVE  + TEMPORARY      → FROZEN
  ACTIVE  + LOST / STOLEN  → BLOCKED
  FROZEN  + TEMPORARY      → 409 ALREADY_FROZEN
  FROZEN  + LOST / STOLEN  → BLOCKED
  BLOCKED + istənilən səbəb → 409 CARD_BLOCKED (son vəziyyət)

Bu spec öz sandbox-ında işləyir (login-user1-cardb.json), login keşlidir (spec üçün 1 dəfə).
Hər ssenari öz kartını açır. ACTIVE və ya FROZEN qalan kartlar sonda LOST ilə bloklanır,
çünki FROZEN kart da 3 kart limitinə sayılır.

Manual qalan TC-lər (Excel-ə uyğun): TC-CARDB-013, TC-CARDB-015.

* "/auth/login" ünvanına "login-user1-cardb.json" ile login ol ve "token" tokenini yadda saxla

## TC-CARDB-001 Aktiv kartın müvəqqəti dondurulması (ACTIVE + TEMPORARY → FROZEN)
tags: api, regression, GRAD-203, positive, state-transition

* "Dondurma" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key   |value    |
   |------|---------|
   |reason|TEMPORARY|
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "FROZEN" beraberdir
* Json cavabında "blockReason" deyeri "TEMPORARY" beraberdir
* Json cavabında "blockedAt" deyeri "^[0-9]{4}-[0-9]{2}-[0-9]{2}T.+" regex-ine uyğun olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARDB-002 Aktiv kartın itirildiyi üçün bloklanması (ACTIVE + LOST → BLOCKED)
tags: api, regression, GRAD-203, positive, state-transition

* "Itirilmis" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key   |value|
   |------|-----|
   |reason|LOST |
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir
* Json cavabında "blockReason" deyeri "LOST" beraberdir
* Json cavabında "blockedAt" deyeri boş olmamalıdır

## TC-CARDB-003 Aktiv kartın oğurlandığı üçün bloklanması (ACTIVE + STOLEN → BLOCKED)
tags: api, regression, GRAD-203, positive, state-transition

* "Ogurlanmis" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key   |value |
   |------|------|
   |reason|STOLEN|
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir
* Json cavabında "blockReason" deyeri "STOLEN" beraberdir
* Json cavabında "blockedAt" deyeri boş olmamalıdır

## TC-CARDB-004 Artıq dondurulmuş kartın təkrar dondurula bilməməsi (FROZEN + TEMPORARY → 409)
tags: api, regression, GRAD-203, negative, state-transition

* "Tekrar Dondurma" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "${cardId}" kartını TEMPORARY səbəbi ilə dondur
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key   |value    |
   |------|---------|
   |reason|TEMPORARY|
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "ALREADY_FROZEN" beraberdir
* "${cardId}" kartının statusu "FROZEN" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARDB-005 Dondurulmuş kartın itirildiyi üçün həmişəlik bloklanması (FROZEN + LOST → BLOCKED)
tags: api, regression, GRAD-203, positive, state-transition

* "Donmus Itirilmis" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "${cardId}" kartını TEMPORARY səbəbi ilə dondur
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key   |value|
   |------|-----|
   |reason|LOST |
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir
* Json cavabında "blockReason" deyeri "LOST" beraberdir

## TC-CARDB-006 Dondurulmuş kartın oğurlandığı üçün həmişəlik bloklanması (FROZEN + STOLEN → BLOCKED)
tags: api, regression, GRAD-203, positive, state-transition

* "Donmus Ogurlanmis" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "${cardId}" kartını TEMPORARY səbəbi ilə dondur
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key   |value |
   |------|------|
   |reason|STOLEN|
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir
* Json cavabında "blockReason" deyeri "STOLEN" beraberdir

## TC-CARDB-007 Bloklanmış kartın dondurula bilməməsi (BLOCKED + TEMPORARY → 409)
tags: api, regression, GRAD-203, negative, state-transition

* "Blok Dondurma" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key   |value    |
   |------|---------|
   |reason|TEMPORARY|
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "CARD_BLOCKED" beraberdir
* "${cardId}" kartının statusu "BLOCKED" olmalıdır

## TC-CARDB-008 Bloklanmış kartın təkrar bloklana bilməməsi (BLOCKED + LOST → 409)
tags: api, regression, GRAD-203, negative, state-transition

* "Blok Lost" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key   |value|
   |------|-----|
   |reason|LOST |
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "CARD_BLOCKED" beraberdir

## TC-CARDB-009 Bloklanmış kartın təkrar bloklana bilməməsi (BLOCKED + STOLEN → 409)
tags: api, regression, GRAD-203, negative, state-transition

* "Blok Stolen" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key   |value |
   |------|------|
   |reason|STOLEN|
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "CARD_BLOCKED" beraberdir

## TC-CARDB-010 Dondurmadan sonra kartın yeni statusunun yadda saxlanması (GET ilə)
tags: api, regression, GRAD-203, positive, state-transition

* "Status Yaddasi" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "${cardId}" kartını TEMPORARY səbəbi ilə dondur
* Json cavabında "blockedAt" deyerini "blokVaxti" olaraq yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/cards/${cardId}"
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "FROZEN" beraberdir
* Json cavabında "blockReason" deyeri "TEMPORARY" beraberdir
* Json cavabında "blockedAt" deyeri "blokVaxti" ile eynidir
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARDB-011 İcazəsiz səbəblə (BROKEN) kartı bloklamaq cəhdinin rədd edilməsi
tags: api, regression, GRAD-203, negative

* "Sehv Sebeb" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key   |value |
   |------|------|
   |reason|BROKEN|
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "1" olmalıdır
* Json cavabında "details[0].field" deyeri "reason" beraberdir
* "${cardId}" kartının statusu "ACTIVE" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARDB-012 Səbəb (reason) göndərilmədən kartı bloklamaq cəhdinin rədd edilməsi
tags: api, regression, GRAD-203, negative

* "Sebebsiz" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "{}" metnini elave et
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "1" olmalıdır
* Json cavabında "details[0].field" deyeri "reason" beraberdir
* "${cardId}" kartının statusu "ACTIVE" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARDB-014 Body göndərilmədən kartı bloklamaq cəhdinin rədd edilməsi
tags: api, regression, GRAD-203, negative

* "Bodysiz" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "INVALID_JSON" beraberdir
* "${cardId}" kartının statusu "ACTIVE" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARDB-016 Mövcud olmayan kartı bloklamaq cəhdinin rədd edilməsi
tags: api, regression, GRAD-203, negative

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key   |value    |
   |------|---------|
   |reason|TEMPORARY|
* "POST" sorğusu gönder "/cards/vcd_00000000/block"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## TC-CARDB-017 Başqa istifadəçinin kartını bloklamaq cəhdinin rədd edilməsi (404, 403 yox)
tags: api, regression, GRAD-203, negative, security

* "Basqasinin Karti" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "/auth/login" ünvanına "login-user2-cardb.json" ile login ol ve "token" tokenini yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key   |value|
   |------|-----|
   |reason|LOST |
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir
* "/auth/login" ünvanına "login-user1-cardb.json" ile login ol ve "token" tokenini yadda saxla
* "${cardId}" kartının statusu "ACTIVE" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARDB-018 Token olmadan kartı bloklamaq cəhdinin rədd edilməsi
tags: api, regression, GRAD-203, negative, auth

* "Tokensiz Blok" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* Body-ni cedvelden qur
   |key   |value    |
   |------|---------|
   |reason|TEMPORARY|
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "401" olmalıdır
* Json cavabında "error" açarı mövcud olmalıdır
* "${cardId}" kartının statusu "ACTIVE" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARDB-019 Dondurulmuş kartla ödəniş edilə bilməməsi
tags: api, regression, GRAD-203, negative, state-transition

* "Donmus Odenis" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "${cardId}" kartını TEMPORARY səbəbi ilə dondur
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/cards/${cardId}"
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyerini "balansEvvel" olaraq yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "cardb19-${random.uuid}"
* Body olaraq "payment-azerisiq-10.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CARD_NOT_ACTIVE" beraberdir
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/cards/${cardId}"
* Json cavabında "availableBalance" deyeri "balansEvvel" ile eynidir
* Json cavabında "spentToday" deyeri "==" "0" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARDB-020 Bloklanmış kartla ödəniş edilə bilməməsi
tags: api, regression, GRAD-203, negative, state-transition

* "Bloklu Odenis" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/cards/${cardId}"
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyerini "balansEvvel" olaraq yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "cardb20-${random.uuid}"
* Body olaraq "payment-azerisiq-10.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CARD_NOT_ACTIVE" beraberdir
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/cards/${cardId}"
* Json cavabında "availableBalance" deyeri "balansEvvel" ile eynidir
