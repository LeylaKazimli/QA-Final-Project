# GRAD-201 — Kart sayı limiti (maksimum 3 ACTIVE/FROZEN)

Limit testləri digər testlərə qarışmasın deyə hər ssenari ÖZ təmiz sandbox-ında işləyir
(login addımı ssenarinin içindədir, hər ssenarinin öz login faylı var).
Ssenari lazım olan 3 kartı özü açır.

## TC-CARD-019 3 aktiv kart olduqda 4-cü kartın açılmaması (BVA: max+1)
tags: api, regression, GRAD-201, negative, bva

* "/auth/login" ünvanına "login-user1-card-limit.json" ile login ol ve "token" tokenini yadda saxla
* "Bir" adlı "10" AZN-lik kart aç və id-sini "kart1" olaraq yadda saxla
* "Iki" adlı "10" AZN-lik kart aç və id-sini "kart2" olaraq yadda saxla
* "Uc" adlı "10" AZN-lik kart aç və id-sini "kart3" olaraq yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key          |value    |
   |-------------|---------|
   |accountId    |acc_002  |
   |initialAmount|10       |
   |label        |Dorduncu |
* "POST" sorğusu gönder "/cards"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CARD_LIMIT_REACHED" beraberdir

## TC-CARD-020 Bloklanmış kartın limitə sayılmaması: yeni kart açıla bilir
tags: api, regression, GRAD-201, positive

* "/auth/login" ünvanına "login-user1-card-limit2.json" ile login ol ve "token" tokenini yadda saxla
* "Bir" adlı "10" AZN-lik kart aç və id-sini "kart1" olaraq yadda saxla
* "Iki" adlı "10" AZN-lik kart aç və id-sini "kart2" olaraq yadda saxla
* "Uc" adlı "10" AZN-lik kart aç və id-sini "kart3" olaraq yadda saxla
* "${kart2}" kartını təmizlik üçün LOST səbəbi ilə blokla
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
* Json cavabında "status" deyeri "ACTIVE" beraberdir
* Json cavabında "id" deyeri "kart2" ile ferqlidir
