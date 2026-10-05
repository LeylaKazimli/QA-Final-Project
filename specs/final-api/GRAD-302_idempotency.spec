# GRAD-302 — Kommunal ödəniş: idempotency (ikiqat ödənişdən qorunma)

Bu spec öz sandbox-ında işləyir (login-user1-payidem.json), login keşlidir (spec üçün 1 dəfə).
Idempotency açarları hər run-da təsadüfi yaradılır və "acar" dəyişənində saxlanılır:
eyni açar ssenari daxilində təkrar istifadə olunur, run-lar arasında isə toqquşmur.

Manual qalan TC-lər (Excel-ə uyğun): TC-PAY-031, TC-PAY-033.

* "/auth/login" ünvanına "login-user1-payidem.json" ile login ol ve "token" tokenini yadda saxla

## TC-PAY-026 Eyni ödənişin təkrar göndərilməsində pulun ikinci dəfə çıxmaması (replay)
tags: api, regression, GRAD-302, idempotency, smoke

* "acar" deyişenine "idem-${random.uuid}" deyerini ver
* "Replay" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "50" AZN ödənişi "${acar}" açarı ilə göndər
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "payId" olaraq yadda saxla
* Json cavabında "receiptNo" deyerini "qebzNo" olaraq yadda saxla
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "50" AZN ödənişi "${acar}" açarı ilə göndər
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "payId" ile eynidir
* Json cavabında "receiptNo" deyeri "qebzNo" ile eynidir
* Header "Idempotent-Replay" deyerinde "true" olmalıdır
* Kartın balansı "49.5" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-027 Eyni açarla fərqli məbləğ göndəriləndə ödənişin rədd edilməsi
tags: api, regression, GRAD-302, idempotency, negative

* "acar" deyişenine "idem-${random.uuid}" deyerini ver
* "Konflikt" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "50" AZN ödənişi "${acar}" açarı ilə göndər
* Status kodunun "201" olmalıdır
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "60" AZN ödənişi "${acar}" açarı ilə göndər
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "IDEMPOTENCY_CONFLICT" beraberdir
* Kartın balansı "49.5" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-028 Idempotency-Key header-i olmadan ödənişin rədd edilməsi
tags: api, regression, GRAD-302, idempotency, negative

* "Acarsiz" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "pBiller" deyişenine "citynet" deyerini ver
* "pSub" deyişenine "CN123456" deyerini ver
* "pAmount" deyişenine "50" deyerini ver
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "payment.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "IDEMPOTENCY_KEY_REQUIRED" beraberdir
* Kartın balansı "100" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-029 7 simvolluq Idempotency-Key ilə ödənişin rədd edilməsi (BVA: min-1)
tags: api, regression, GRAD-302, idempotency, negative, bva

Açar: "a" + 6 rəqəm = 7 simvol.

* "Qisa Acar" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "50" AZN ödənişi "a${random.number}" açarı ilə göndər
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "IDEMPOTENCY_KEY_INVALID" beraberdir
* Kartın balansı "100" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-030 8 simvolluq Idempotency-Key ilə ödənişin keçməsi (BVA: min)
tags: api, regression, GRAD-302, idempotency, positive, bva

Açar: "ab" + 6 rəqəm = 8 simvol.

* "Min Acar" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "10" AZN ödənişi "ab${random.number}" açarı ilə göndər
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-032 Uğursuz ödənişdən sonra eyni açarla düzəldilmiş ödənişin keçməsi
tags: api, regression, GRAD-302, idempotency, positive

* "acar" deyişenine "idem-${random.uuid}" deyerini ver
* "Duzelis" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "citynet" təchizatçısına "CN12345" nömrəsi ilə "50" AZN ödənişi "${acar}" açarı ilə göndər
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INVALID_SUBSCRIBER" beraberdir
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "50" AZN ödənişi "${acar}" açarı ilə göndər
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Kartın balansı "949.5" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla
