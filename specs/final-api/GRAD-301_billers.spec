# GRAD-301 — Xidmət təchizatçıları kataloqu (GET /billers)

Kataloq statikdir (sandbox-dan asılı deyil), ona görə testlər data yaratmır.
Təchizatçılar massivdə sıra ilə yox, id-yə görə tapılır (GPath: items.find { it.id == '...' }),
beləliklə server sıranı dəyişsə də testlər sınmır.

Manual qalan TC-lər (Excel-ə uyğun): TC-BILL-007, TC-BILL-008, TC-BILL-010.

* "/auth/login" ünvanına "login-user1-bill.json" ile login ol ve "token" tokenini yadda saxla

## TC-BILL-001 Bütün təchizatçıların (6) tam məlumatla qaytarılması
tags: api, regression, GRAD-301, positive

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/billers"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "6" beraberdir
* Json cavabında "items" massivinin ölçüsü "6" olmalıdır
* Json cavabında "items.id" siyahısındakı deyerler unikal olmalıdır
* Json cavabında "items.findAll { it.id && it.name && it.category && it.subscriberFormat && it.subscriberPattern && it.minAmount != null && it.maxAmount != null && it.fee }.size()" deyeri "6" beraberdir

## TC-BILL-002 Təchizatçıların kateqoriya və məbləğ aralıqlarının spesifikasiyaya uyğunluğu
tags: api, regression, GRAD-301, positive

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/billers"
* Status kodunun "200" olmalıdır
* Json cavabını cedvel ile yoxla
   |path                                         |value   |
   |---------------------------------------------|--------|
   |items.find { it.id == 'azerisiq' }.category |UTILITY |
   |items.find { it.id == 'azersu' }.category   |UTILITY |
   |items.find { it.id == 'azercell' }.category |MOBILE  |
   |items.find { it.id == 'bakcell' }.category  |MOBILE  |
   |items.find { it.id == 'citynet' }.category  |INTERNET|
   |items.find { it.id == 'aztelekom' }.category|INTERNET|
* Json cavabında "items.find { it.id == 'azerisiq' }.minAmount" deyeri "==" "1" olmalıdır
* Json cavabında "items.find { it.id == 'azerisiq' }.maxAmount" deyeri "==" "500" olmalıdır
* Json cavabında "items.find { it.id == 'azersu' }.minAmount" deyeri "==" "1" olmalıdır
* Json cavabında "items.find { it.id == 'azersu' }.maxAmount" deyeri "==" "300" olmalıdır
* Json cavabında "items.find { it.id == 'azercell' }.minAmount" deyeri "==" "0.5" olmalıdır
* Json cavabında "items.find { it.id == 'azercell' }.maxAmount" deyeri "==" "200" olmalıdır
* Json cavabında "items.find { it.id == 'bakcell' }.minAmount" deyeri "==" "0.5" olmalıdır
* Json cavabında "items.find { it.id == 'bakcell' }.maxAmount" deyeri "==" "200" olmalıdır
* Json cavabında "items.find { it.id == 'citynet' }.minAmount" deyeri "==" "5" olmalıdır
* Json cavabında "items.find { it.id == 'citynet' }.maxAmount" deyeri "==" "150" olmalıdır
* Json cavabında "items.find { it.id == 'aztelekom' }.minAmount" deyeri "==" "2" olmalıdır
* Json cavabında "items.find { it.id == 'aztelekom' }.maxAmount" deyeri "==" "100" olmalıdır

## TC-BILL-003 Təchizatçıların komissiya qaydalarının spesifikasiyaya uyğunluğu
tags: api, regression, GRAD-301, positive

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/billers"
* Status kodunun "200" olmalıdır
* Json cavabını cedvel ile yoxla
   |path                                         |value  |
   |---------------------------------------------|-------|
   |items.find { it.id == 'citynet' }.fee.type  |PERCENT|
   |items.find { it.id == 'aztelekom' }.fee.type|FIXED  |
   |items.find { it.id == 'azerisiq' }.fee.type |NONE   |
   |items.find { it.id == 'azersu' }.fee.type   |NONE   |
   |items.find { it.id == 'azercell' }.fee.type |NONE   |
   |items.find { it.id == 'bakcell' }.fee.type  |NONE   |
* Json cavabında "items.find { it.id == 'citynet' }.fee.value" deyeri "==" "1" olmalıdır
* Json cavabında "items.find { it.id == 'citynet' }.fee.min" deyeri "0.2" beraberdir
* Json cavabında "items.find { it.id == 'citynet' }.fee.max" deyeri "==" "2" olmalıdır
* Json cavabında "items.find { it.id == 'aztelekom' }.fee.value" deyeri "==" "0.5" olmalıdır

## TC-BILL-004 Abunəçi nömrəsi şablonlarının (regex) düzgün işləməsi
tags: api, regression, GRAD-301, positive

Hər təchizatçının cavabdakı subscriberPattern-i düzgün nümunəni qəbul etməli (1), səhvini rədd etməlidir (0).

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/billers"
* Status kodunun "200" olmalıdır
* Json cavabında "items.findAll { it.id == 'citynet' && 'CN123456' ==~ it.subscriberPattern }.size()" deyeri "1" beraberdir
* Json cavabında "items.findAll { it.id == 'citynet' && 'CN12345' ==~ it.subscriberPattern }.size()" deyeri "0" beraberdir
* Json cavabında "items.findAll { it.id == 'citynet' && 'cn123456' ==~ it.subscriberPattern }.size()" deyeri "0" beraberdir
* Json cavabında "items.findAll { it.id == 'azercell' && '501234567' ==~ it.subscriberPattern }.size()" deyeri "1" beraberdir
* Json cavabında "items.findAll { it.id == 'azercell' && '511234567' ==~ it.subscriberPattern }.size()" deyeri "1" beraberdir
* Json cavabında "items.findAll { it.id == 'azercell' && '101234567' ==~ it.subscriberPattern }.size()" deyeri "1" beraberdir
* Json cavabında "items.findAll { it.id == 'azercell' && '551234567' ==~ it.subscriberPattern }.size()" deyeri "0" beraberdir
* Json cavabında "items.findAll { it.id == 'bakcell' && '551234567' ==~ it.subscriberPattern }.size()" deyeri "1" beraberdir
* Json cavabında "items.findAll { it.id == 'bakcell' && '991234567' ==~ it.subscriberPattern }.size()" deyeri "1" beraberdir
* Json cavabında "items.findAll { it.id == 'bakcell' && '501234567' ==~ it.subscriberPattern }.size()" deyeri "0" beraberdir
* Json cavabında "items.findAll { it.id == 'azerisiq' && '1234567890' ==~ it.subscriberPattern }.size()" deyeri "1" beraberdir
* Json cavabında "items.findAll { it.id == 'azerisiq' && '123456789' ==~ it.subscriberPattern }.size()" deyeri "0" beraberdir
* Json cavabında "items.findAll { it.id == 'azersu' && '12345678' ==~ it.subscriberPattern }.size()" deyeri "1" beraberdir
* Json cavabında "items.findAll { it.id == 'azersu' && '1234567' ==~ it.subscriberPattern }.size()" deyeri "0" beraberdir
* Json cavabında "items.findAll { it.id == 'aztelekom' && '1234567' ==~ it.subscriberPattern }.size()" deyeri "1" beraberdir
* Json cavabında "items.findAll { it.id == 'aztelekom' && '12345678' ==~ it.subscriberPattern }.size()" deyeri "0" beraberdir

## TC-BILL-005 Kataloqdakı məbləğ sahələrinin rəqəm (number) tipində qaytarılması
tags: api, regression, GRAD-301, positive

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/billers"
* Status kodunun "200" olmalıdır
* Json cavabında "items.findAll { it.minAmount instanceof Number && it.maxAmount instanceof Number }.size()" deyeri "6" beraberdir
* Json cavabında "items.find { it.id == 'citynet' }.fee.value" deyerinin tipi "number" olmalıdır
* Json cavabında "items.find { it.id == 'citynet' }.fee.min" deyerinin tipi "number" olmalıdır
* Json cavabında "items.find { it.id == 'citynet' }.fee.max" deyerinin tipi "number" olmalıdır
* Json cavabında "items.find { it.id == 'aztelekom' }.fee.value" deyerinin tipi "number" olmalıdır

## TC-BILL-006 Təchizatçıların MOBILE kateqoriyasına görə filtrlənməsi
tags: api, regression, GRAD-301, positive

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "category" = "MOBILE"
* "GET" sorğusu gönder "/billers"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "items" massivinin ölçüsü "2" olmalıdır
* Json cavabında "items.category" siyahısındakı bütün deyerler "MOBILE" olmalıdır
* Json cavabında "items.id" deyerinde "azercell" olmalıdır
* Json cavabında "items.id" deyerinde "bakcell" olmalıdır

## TC-BILL-009 Mövcud olmayan kateqoriya (GAS) ilə sorğunun rədd edilməsi
tags: api, regression, GRAD-301, negative

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "category" = "GAS"
* "GET" sorğusu gönder "/billers"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "1" olmalıdır
* Json cavabında "details[0].field" deyeri "category" beraberdir

## TC-BILL-011 Token olmadan kataloqa baxmaq cəhdinin rədd edilməsi
tags: api, regression, GRAD-301, negative, auth

* Yeni API sorğusu hazırla
* "GET" sorğusu gönder "/billers"
* Status kodunun "401" olmalıdır
* Json cavabında "error" açarı mövcud olmalıdır
* Json cavabında "items" açarı olmamalıdır
