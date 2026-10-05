# GRAD-302 — Kommunal ödəniş: limitlər, balans və kart statusu

Bu spec öz sandbox-ında işləyir (login-user1-paylim.json), login keşlidir (spec üçün 1 dəfə).
Limitlər: bir əməliyyat 300 AZN, günlük 500 AZN (kart üzrə). Limit və balans
komissiya daxil cəm (total) üzrə yoxlanılır. Hər ssenari öz kartını açır və sonda bloklayır.

* "/auth/login" ünvanına "login-user1-paylim.json" ile login ol ve "token" tokenini yadda saxla

## TC-PAY-034 Bir ödənişdə 300 AZN-in keçməsi (bir əməliyyat limiti, BVA: max)
tags: api, regression, GRAD-302, limits, positive, bva

* "Limit 300" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "azerisiq" təchizatçısına "1234567890" nömrəsi ilə "300" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* Json cavabında "total" deyeri "==" "300" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-035 Bir ödənişdə 300.01 AZN-in rədd edilməsi (BVA: max+0.01)
tags: api, regression, GRAD-302, limits, negative, bva

* "Limit 30001" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "azerisiq" təchizatçısına "1234567890" nömrəsi ilə "300.01" AZN ödəniş göndər
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "PER_TRANSACTION_LIMIT" beraberdir
* Kartın balansı "1000" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-036 Limit və balansın məbləğ yox, komissiya daxil cəm (total) üzrə yoxlanması
tags: api, regression, GRAD-302, limits, negative

A) Günlük xərc 479.93 (limitə 20.07 qalır): CityNet 19.90 → total 20.10 > 20.07 → DAILY_LIMIT_EXCEEDED
B) Balans 50: CityNet 49.60 → total 50.10 > 50 → INSUFFICIENT_FUNDS

* "Total Limit" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "azerisiq" təchizatçısına "1234567890" nömrəsi ilə "300" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "azerisiq" təchizatçısına "1234567890" nömrəsi ilə "179.93" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "19.9" AZN ödəniş göndər
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "DAILY_LIMIT_EXCEEDED" beraberdir
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla
* "Total Balans" adlı "50" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "49.6" AZN ödəniş göndər
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INSUFFICIENT_FUNDS" beraberdir
* Kartın balansı "50" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-037 Günlük limit (500 AZN) dolduqda növbəti ödənişin rədd edilməsi
tags: api, regression, GRAD-302, limits, negative, bva

* "Gunluk Limit" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "azercell" təchizatçısına "501234567" nömrəsi ilə "200" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "azerisiq" təchizatçısına "1234567890" nömrəsi ilə "300" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "azerisiq" təchizatçısına "1234567890" nömrəsi ilə "1" AZN ödəniş göndər
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "DAILY_LIMIT_EXCEEDED" beraberdir
* Json cavabında "remaining" deyeri "==" "0" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-038 Balansdan 1 qəpik çox ödənişin rədd edilməsi (49.50 balans, 49.51 ödəniş)
tags: api, regression, GRAD-302, limits, negative, bva

* "Balans Asimi" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "50" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "azerisiq" təchizatçısına "1234567890" nömrəsi ilə "49.51" AZN ödəniş göndər
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INSUFFICIENT_FUNDS" beraberdir
* Kartın balansı "49.5" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-039 Balansın tamamı qədər ödənişin keçməsi (49.50 balans, 49.50 ödəniş)
tags: api, regression, GRAD-302, limits, positive, bva

* "Balans Tam" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "50" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* "azerisiq" təchizatçısına "1234567890" nömrəsi ilə "49.5" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* Json cavabında "balanceAfter" deyeri "==" "0" olmalıdır
* Kartın balansı "0" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-040 Dondurulmuş kartla ödənişin rədd edilməsi
tags: api, regression, GRAD-302, limits, negative

* "Donmus Kart" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "${cardId}" kartını TEMPORARY səbəbi ilə dondur
* "azerisiq" təchizatçısına "1234567890" nömrəsi ilə "10" AZN ödəniş göndər
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CARD_NOT_ACTIVE" beraberdir
* Kartın balansı "100" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-041 USD kartla AZN təchizatçısına ödənişin rədd edilməsi
tags: api, regression, GRAD-302, limits, negative

user2 (USD hesabı acc_003) öz sandbox-ında işləyir.

* "/auth/login" ünvanına "login-user2-pay.json" ile login ol ve "token" tokenini yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body-ni cedvelden qur
   |key          |value  |
   |-------------|-------|
   |accountId    |acc_003|
   |initialAmount|100    |
* "POST" sorğusu gönder "/cards"
* Status kodunun "201" olmalıdır
* Json cavabında "currency" deyeri "USD" beraberdir
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "azerisiq" təchizatçısına "1234567890" nömrəsi ilə "10" AZN ödəniş göndər
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CURRENCY_NOT_SUPPORTED" beraberdir
* Kartın balansı "100" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-042 Başqa istifadəçinin kartı ilə ödəniş cəhdinin rədd edilməsi (404)
tags: api, regression, GRAD-302, limits, negative, security

* "Basqasinin Karti" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "/auth/login" ünvanına "login-user2-pay.json" ile login ol ve "token" tokenini yadda saxla
* "azerisiq" təchizatçısına "1234567890" nömrəsi ilə "10" AZN ödəniş göndər
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "CARD_NOT_FOUND" beraberdir
* "/auth/login" ünvanına "login-user1-paylim.json" ile login ol ve "token" tokenini yadda saxla
* Kartın balansı "100" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla
