# GRAD-302 — Kommunal ödəniş: uğurlu ödəniş, komissiya, abunəçi nömrəsi, validasiya

Bu spec öz sandbox-ında işləyir (login-user1-pay.json), login keşlidir (spec üçün 1 dəfə).
Hər ssenari öz kartını açır (günlük 500 AZN limiti ssenarilər arasında paylaşılmasın deyə)
və sonda LOST ilə bloklayır (3 kart limiti).

Komissiyalar: CityNet 1% (min 0.20, max 2.00) · Aztelekom sabit 0.50 · digərləri komissiyasız.
Pul dəyərləri mətn kimi müqayisə olunur ("0.21" beraberdir): onluq kəsrlər (0.2, 0.21, 0.33)
float tipində dəqiq saxlanılmadığı üçün ədədi "==" müqayisəsi yalançı xəta verir.

Manual qalan TC-lər (Excel-ə uyğun): TC-PAY-010, TC-PAY-024.

* "/auth/login" ünvanına "login-user1-pay.json" ile login ol ve "token" tokenini yadda saxla

## TC-PAY-001 Düzgün məlumatla kommunal ödənişin uğurla edilməsi (CityNet, 50 AZN)
tags: api, regression, GRAD-302, positive, smoke

* "Odenis" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "50" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* Json cavabını cedvel ile yoxla
   |path        |value                             |
   |------------|----------------------------------|
   |id          |@regex:^bpm_[a-z0-9]{8}$          |
   |status      |SUCCESS                           |
   |amount      |50                                |
   |fee         |0.5                               |
   |total       |50.5                              |
   |currency    |AZN                               |
   |balanceAfter|49.5                              |
   |receiptNo   |@regex:^RCP-[0-9]{8}-[0-9]{6}$    |
* Json cavabında "id" deyerini "payId" olaraq yadda saxla
* Header "Location" deyerinde "/bill-payments/${payId}" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-002 Ödənişdən sonra kartdan komissiya ilə birlikdə (total) pul çıxılması
tags: api, regression, GRAD-302, positive

* "Total Cixilmasi" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "50" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/cards/${cardId}"
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyeri "49.5" beraberdir
* Json cavabında "spentToday" deyeri "50.5" beraberdir
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-003 Hər uğurlu ödənişdə qəbz nömrəsinin 1 artması
tags: api, regression, GRAD-302, positive

Qəbz sayğacı sandbox üzrə işləyir, ona görə bu ssenari ÖZ təmiz sandbox-ında işləyir:
birinci ödəniş -000001, ikinci -000002 olmalıdır.

* "/auth/login" ünvanına "login-user1-pay-receipt.json" ile login ol ve "token" tokenini yadda saxla
* "Qebz" adlı "100" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "50" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* Json cavabında "receiptNo" deyeri "^RCP-[0-9]{8}-000001$" regex-ine uyğun olmalıdır
* "azerisiq" təchizatçısına "1234567890" nömrəsi ilə "10" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* Json cavabında "receiptNo" deyeri "^RCP-[0-9]{8}-000002$" regex-ine uyğun olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-004 Komissiyasız təchizatçıya (Azərişıq) ödənişdə komissiyanın 0 olması
tags: api, regression, GRAD-302, positive

* "Komissiyasiz" adlı "49.5" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "azerisiq" təchizatçısına "1234567890" nömrəsi ilə "49.5" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* Json cavabını cedvel ile yoxla
   |path        |value|
   |------------|-----|
   |fee         |0    |
   |total       |49.5 |
   |balanceAfter|0    |
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-005 CityNet-ə 5 AZN ödənişdə minimum komissiyanın (0.20) tətbiqi (BVA)
tags: api, regression, GRAD-302, positive, bva

* "Min Komissiya" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "5" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* Json cavabında "fee" deyeri "0.2" beraberdir
* Json cavabında "total" deyeri "5.2" beraberdir
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-006 CityNet-ə 20 AZN ödənişdə komissiyanın 0.20 olması (1% = minimum, BVA)
tags: api, regression, GRAD-302, positive, bva

* "Komissiya 20" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "20" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* Json cavabında "fee" deyeri "0.2" beraberdir
* Json cavabında "total" deyeri "20.2" beraberdir
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-007 CityNet-ə 21 AZN ödənişdə komissiyanın 1% (0.21) olması (BVA)
tags: api, regression, GRAD-302, positive, bva

* "Komissiya 21" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "21" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* Json cavabında "fee" deyeri "0.21" beraberdir
* Json cavabında "total" deyeri "21.21" beraberdir
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-008 CityNet-ə maksimum məbləğ (150 AZN) ödənişdə komissiyanın 1.50 olması (BVA)
tags: api, regression, GRAD-302, positive, bva

* "Komissiya 150" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "150" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* Json cavabında "fee" deyeri "1.5" beraberdir
* Json cavabında "total" deyeri "151.5" beraberdir
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-009 CityNet komissiyasının 2 onluğa yuvarlaqlaşdırılması (33.33 AZN → 0.33)
tags: api, regression, GRAD-302, positive

* "Yuvarlaq" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "33.33" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* Json cavabında "fee" deyeri "0.33" beraberdir
* Json cavabında "total" deyeri "33.66" beraberdir
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-011 Aztelekom-a minimum məbləğ (2 AZN) ödənişdə sabit komissiyanın (0.50) tətbiqi
tags: api, regression, GRAD-302, positive, bva

* "Aztelekom Min" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "aztelekom" təchizatçısına "1234567" nömrəsi ilə "2" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* Json cavabında "fee" deyeri "0.5" beraberdir
* Json cavabında "total" deyeri "2.5" beraberdir
* Json cavabında "balanceAfter" deyeri "997.5" beraberdir
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-012 Aztelekom-a maksimum məbləğ (100 AZN) ödənişdə komissiyanın yenə 0.50 olması
tags: api, regression, GRAD-302, positive, bva

* "Aztelekom Max" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "aztelekom" təchizatçısına "1234567" nömrəsi ilə "100" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* Json cavabında "fee" deyeri "0.5" beraberdir
* Json cavabında "total" deyeri "100.5" beraberdir
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-013 Azercell ödənişində Bakcell nömrəsinin (55 prefiksli) rədd edilməsi
tags: api, regression, GRAD-302, negative

* "Azercell 55" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "azercell" təchizatçısına "551234567" nömrəsi ilə "10" AZN ödəniş göndər
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INVALID_SUBSCRIBER" beraberdir
* Json cavabında "expected" deyeri boş olmamalıdır
* Kartın balansı "1000" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-014 Azercell-in bütün prefikslərinə (50, 51, 10) ödənişin keçməsi
tags: api, regression, GRAD-302, positive

* "Azercell Prefiks" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "azercell" təchizatçısına "501234567" nömrəsi ilə "1" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* "azercell" təchizatçısına "511234567" nömrəsi ilə "1" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* "azercell" təchizatçısına "101234567" nömrəsi ilə "1" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Kartın balansı "997" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-015 CityNet-ə natamam abunəçi nömrəsi (CN12345) ilə ödənişin rədd edilməsi
tags: api, regression, GRAD-302, negative

* "CityNet Natamam" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "citynet" təchizatçısına "CN12345" nömrəsi ilə "10" AZN ödəniş göndər
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INVALID_SUBSCRIBER" beraberdir
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-016 Azercell-ə 0.49 AZN ödənişin rədd edilməsi (BVA: min-0.01)
tags: api, regression, GRAD-302, negative, bva

* "Azercell 049" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "azercell" təchizatçısına "501234567" nömrəsi ilə "0.49" AZN ödəniş göndər
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "AMOUNT_OUT_OF_RANGE" beraberdir
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-017 Azercell-ə 0.50 AZN ödənişin keçməsi (BVA: min)
tags: api, regression, GRAD-302, positive, bva

* "Azercell 050" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "azercell" təchizatçısına "501234567" nömrəsi ilə "0.5" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* Json cavabında "total" deyeri "0.5" beraberdir
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-018 Azercell-ə 200.00 AZN ödənişin keçməsi (BVA: max)
tags: api, regression, GRAD-302, positive, bva

* "Azercell 200" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "azercell" təchizatçısına "501234567" nömrəsi ilə "200.00" AZN ödəniş göndər
* Status kodunun "201" olmalıdır
* Json cavabında "total" deyeri "==" "200" olmalıdır
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-019 Azercell-ə 200.01 AZN ödənişin rədd edilməsi (BVA: max+0.01)
tags: api, regression, GRAD-302, negative, bva

* "Azercell 20001" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "azercell" təchizatçısına "501234567" nömrəsi ilə "200.01" AZN ödəniş göndər
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "AMOUNT_OUT_OF_RANGE" beraberdir
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-020 Mövcud olmayan təchizatçıya ödənişin rədd edilməsi
tags: api, regression, GRAD-302, negative

* "Namelum Techizatci" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "gas" təchizatçısına "123" nömrəsi ilə "10" AZN ödəniş göndər
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "BILLER_NOT_FOUND" beraberdir
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-021 Məbləğ mətn kimi ("10") göndəriləndə ödənişin rədd edilməsi
tags: api, regression, GRAD-302, negative

* "Metn Mebleg" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "pay-${random.uuid}"
* Body olaraq "payment-amount-as-string.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "1" olmalıdır
* Json cavabında "details[0].field" deyeri "amount" beraberdir
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-022 Məbləğdə 3 onluq rəqəm (10.555) olduqda ödənişin rədd edilməsi
tags: api, regression, GRAD-302, negative

* "Uc Onluq" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "10.555" AZN ödəniş göndər
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "1" olmalıdır
* Json cavabında "details[0].field" deyeri "amount" beraberdir
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-023 Məbləğ 0 olduqda ödənişin rədd edilməsi
tags: api, regression, GRAD-302, negative, bva

* "Sifir Mebleg" adlı "1000" AZN-lik kart aç və id-sini "cardId" olaraq yadda saxla
* "citynet" təchizatçısına "CN123456" nömrəsi ilə "0" AZN ödəniş göndər
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "1" olmalıdır
* Json cavabında "details[0].field" deyeri "amount" beraberdir
* "${cardId}" kartını təmizlik üçün LOST səbəbi ilə blokla

## TC-PAY-025 Token olmadan ödəniş cəhdinin rədd edilməsi
tags: api, regression, GRAD-302, negative, auth

* "cardId" deyişenine "vcd_00000000" deyerini ver
* "pBiller" deyişenine "citynet" deyerini ver
* "pSub" deyişenine "CN123456" deyerini ver
* "pAmount" deyişenine "50" deyerini ver
* Yeni API sorğusu hazırla
* Header elave et "Idempotency-Key" = "pay-${random.uuid}"
* Body olaraq "payment.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "401" olmalıdır
* Json cavabında "error" açarı mövcud olmalıdır
* Json cavabında "receiptNo" açarı olmamalıdır
