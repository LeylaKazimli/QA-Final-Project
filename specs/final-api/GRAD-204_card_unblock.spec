# GRAD-204 — Dondurulmuş kartı açmaq (POST /cards/{id}/unblock)

State transition (vəziyyət keçidləri):
  FROZEN  + unblock → ACTIVE (blockReason və blockedAt sıfırlanır)
  ACTIVE  + unblock → 409 NOT_FROZEN
  BLOCKED + unblock → 409 PERMANENTLY_BLOCKED (LOST/STOLEN geri qaytarılmır)

Bu spec öz sandbox-ında işləyir (login-user1-cardu.json), login keşlidir (spec üçün 1 dəfə).
Hər ssenari öz kartını açır; ACTIVE və ya FROZEN qalan kartlar sonda LOST ilə bloklanır (3 kart limiti).

Manual qalan TC-lər (Excel-ə uyğun): TC-CARDU-004, TC-CARDU-006, TC-CARDU-009.

* "/auth/login" ünvanına "login-user1-cardu.json" ile login ol ve "token" tokenini yadda saxla

## TC-CARDU-001 Dondurulmuş kartın yenidən aktivləşdirilməsi (FROZEN → ACTIVE)
tags: api, regression, GRAD-204, positive, state-transition

* "Acilan Kart" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "${cardId}" kartını TEMPORARY səbəbi ilə dondur
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "POST" sorğusu gönder "/cards/${cardId}/unblock"
* Status kodunun "200" olmalıdır
* Json cavabını cedvel ile yoxla
   |path       |value |
   |-----------|------|
   |status     |ACTIVE|
   |blockReason|null  |
   |blockedAt  |null  |
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARDU-002 Aktiv kartı "açmaq" cəhdinin rədd edilməsi (ACTIVE → 409)
tags: api, regression, GRAD-204, negative, state-transition

* "Aktiv Kart" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "POST" sorğusu gönder "/cards/${cardId}/unblock"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "NOT_FROZEN" beraberdir
* "${cardId}" kartının statusu "ACTIVE" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARDU-003 İtirildiyi üçün bloklanmış kartın açıla bilməməsi (BLOCKED → 409)
tags: api, regression, GRAD-204, negative, state-transition

* "Itirilmis Kart" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "POST" sorğusu gönder "/cards/${cardId}/unblock"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "PERMANENTLY_BLOCKED" beraberdir
* "${cardId}" kartının statusu "BLOCKED" olmalıdır

## TC-CARDU-005 Açılmış kartın yenidən dondurula bilməsi (FROZEN → ACTIVE → FROZEN)
tags: api, regression, GRAD-204, positive, state-transition

* "Tekrar Donan" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "${cardId}" kartını TEMPORARY səbəbi ilə dondur
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "POST" sorğusu gönder "/cards/${cardId}/unblock"
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "ACTIVE" beraberdir
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
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARDU-007 Kart açıldıqdan sonra yeni statusun yadda saxlanması (GET ilə)
tags: api, regression, GRAD-204, positive, state-transition

* "Status Yaddasi" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "${cardId}" kartını TEMPORARY səbəbi ilə dondur
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "POST" sorğusu gönder "/cards/${cardId}/unblock"
* Status kodunun "200" olmalıdır
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/cards/${cardId}"
* Status kodunun "200" olmalıdır
* Json cavabını cedvel ile yoxla
   |path       |value |
   |-----------|------|
   |status     |ACTIVE|
   |blockReason|null  |
   |blockedAt  |null  |
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARDU-008 Açılmış kartla ödənişin uğurla keçməsi
tags: api, regression, GRAD-204, positive, state-transition

Azərişıq komissiyasızdır: 10 AZN ödənişdən sonra balans 100 → 90.

* "Odenis Karti" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "${cardId}" kartını TEMPORARY səbəbi ilə dondur
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "POST" sorğusu gönder "/cards/${cardId}/unblock"
* Status kodunun "200" olmalıdır
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "cardu8-${random.uuid}"
* Body olaraq "payment-azerisiq-10.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/cards/${cardId}"
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyeri "==" "90" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARDU-010 Mövcud olmayan kartı açmaq cəhdinin rədd edilməsi
tags: api, regression, GRAD-204, negative

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "POST" sorğusu gönder "/cards/vcd_00000000/unblock"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## TC-CARDU-011 Başqa istifadəçinin kartını açmaq cəhdinin rədd edilməsi (404, 403 yox)
tags: api, regression, GRAD-204, negative, security

* "Basqasinin Karti" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "${cardId}" kartını TEMPORARY səbəbi ilə dondur
* "/auth/login" ünvanına "login-user2-cardu.json" ile login ol ve "token" tokenini yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "POST" sorğusu gönder "/cards/${cardId}/unblock"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir
* "/auth/login" ünvanına "login-user1-cardu.json" ile login ol ve "token" tokenini yadda saxla
* "${cardId}" kartının statusu "FROZEN" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-CARDU-012 Token olmadan kartı açmaq cəhdinin rədd edilməsi
tags: api, regression, GRAD-204, negative, auth

* "Tokensiz Acma" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "${cardId}" kartını TEMPORARY səbəbi ilə dondur
* Yeni API sorğusu hazırla
* "POST" sorğusu gönder "/cards/${cardId}/unblock"
* Status kodunun "401" olmalıdır
* Json cavabında "error" açarı mövcud olmalıdır
* "${cardId}" kartının statusu "FROZEN" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla
