# Framework self-test — API step-ləri

Bu spec framework-ün BÜTÜN API step-lərini açıq test API-lərində yoxlayır
(dummyjson.com, postman-echo.com) və hər step-in istifadə nümunəsidir.
İcra: `./framework-tests/run-selftest.sh api`

## GET: status, dəyər müqayisəsi, tip, regex, header, vaxt
tags: selftest, api, get

* Set base Url to "https://dummyjson.com"
* API e GET request gönder "/products/1"
* Status kodunun "200" olmalıdır
* Status kodu "200" ile "299" arasında olmalıdır
* Json cavabında "id" deyeri "1" beraberdir
* Json cavabında "id" deyeri integer "1" beraberdir
* Json cavabında "category" deyeri "groceries" olmamalıdır
* Json cavabında "title" deyerinde "Mascara" olmalıdır
* Json cavabında "tags" deyerinde "beauty" olmalıdır
* Json cavabında "sku" deyeri "^[A-Z]{3}-.+" regex-ine uyğun olmalıdır
* Json cavabında "price" deyeri ">" "0" olmalıdır
* Json cavabında "rating" deyeri "<=" "5" olmalıdır
* Json cavabında "title" deyeri boş olmamalıdır
* Json cavabında "dimensions" açarı mövcud olmalıdır
* Json cavabında "dimensions.width" açarı mövcud olmalıdır
* Json cavabında "password" açarı olmamalıdır
* Json cavabında verilen "stock" deyeri ededdir
* Json cavabında "title" deyerinin tipi "string" olmalıdır
* Json cavabında "price" deyerinin tipi "number" olmalıdır
* Json cavabında "tags" deyerinin tipi "array" olmalıdır
* Json cavabında "dimensions" deyerinin tipi "object" olmalıdır
* Json cavabında "reviews[0].rating" deyeri ">=" "1" olmalıdır
* Cavab body-sinde "Essence" olmalıdır
* Header "Content-Type" movcud olmalıdır
* Header "Content-Type" deyerinde "application/json" olmalıdır
* Respons cavab müddeti "5000" milliSaniyeden az olmalıdır

## Tam body yoxlaması: cədvəl, gözlənilən JSON faylı, JSON schema
tags: selftest, api, body

* Set base Url to "https://dummyjson.com"
* API e GET request gönder "/products/1"
* Json cavabını cedvel ile yoxla

   |path             |value         |
   |-----------------|--------------|
   |id               |1             |
   |category         |beauty        |
   |brand            |Essence       |
   |price            |@number       |
   |tags[0]          |beauty        |
   |dimensions.depth |@number       |
   |reviews[0].date  |@notNull      |
   |meta.qrCode      |@contains:http|
   |availabilityStatus|@regex:.+Stock|

* Json cavabı "selftest-product.json" faylındakı gözlenilen JSON-a uyğun olmalıdır
* Cavab "selftest-product.schema.json" JSON schema-sına uyğun olmalıdır

## Massivlər: ölçü, sıralama, unikallıq, filter
tags: selftest, api, array

* Set base Url to "https://dummyjson.com"
* Initalize request specification
* Add Endpoint "/products"
* Query parametri elave et "limit" = "10"
* Query parametri elave et "sortBy" = "price"
* Query parametri elave et "order" = "asc"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "products" massivinin ölçüsü "10" olmalıdır
* Json cavabında "products" massivinin ölçüsü en az "5" olmalıdır
* Json cavabında "products.price" siyahısı artan sırada olmalıdır
* Json cavabında "products.id" siyahısındakı deyerler unikal olmalıdır
* Json cavabında "products.findAll { it.price > 0 }.size()" deyeri "10" beraberdir
* Yeni API sorğusu hazırla
* Endpoint "/products/category/{category}" olsun
* Path parametri elave et "category" = "smartphones"
* Query parametri elave et "sortBy" = "price"
* Query parametri elave et "order" = "desc"
* "GET" sorğusu gönder
* Json cavabında "products.category" siyahısındakı bütün deyerler "smartphones" olmalıdır
* Json cavabında "products.price" siyahısı azalan sırada olmalıdır

## Auth: login, token keşi, Bearer, qorunan endpoint, 401
tags: selftest, api, auth

* Set base Url to "https://dummyjson.com"
* "/auth/login" ünvanına "selftest-dummyjson-login.json" ile login ol ve "accessToken" tokenini yadda saxla
* "/auth/login" ünvanına "selftest-dummyjson-login.json" ile login ol ve "accessToken" tokenini yadda saxla
* Initalize request specification
* Add Endpoint "/auth/me"
* Authorization header-ine tokeni elave et
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "username" deyeri "emilys" beraberdir
* Yeni API sorğusu hazırla
* Bearer token elave et "${rawToken}"
* "GET" sorğusu gönder "/auth/me"
* Status kodunun "200" olmalıdır
* Yeni API sorğusu hazırla
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder "/auth/me"
* Status kodunun "200" olmalıdır
* "/auth/login" ünvanına "selftest-dummyjson-login.json" ile yeni sessiya açaraq login ol ve "accessToken" tokenini yadda saxla
* Token keşini temizle
* Yeni API sorğusu hazırla
* Bearer token elave et "yanlis-token"
* "GET" sorğusu gönder "/auth/me"
* Status kodu "400" ile "499" arasında olmalıdır

## POST / PUT / PATCH / DELETE və body şablonları
tags: selftest, api, crud

* Set base Url to "https://dummyjson.com"
* Initalize request specification
* Add Endpoint "/products/add"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"title\": \"Gauge Test\", \"price\": 12.5}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "title" deyeri "Gauge Test" beraberdir
* Save value of "id" as "newId"
* Json cavabında "id" deyeri "newId" ile eynidir
* Json cavabında "price" deyeri "newId" ile ferqlidir
* Yeni API sorğusu hazırla
* Body-ni cedvelden qur

   |key     |value      |
   |--------|-----------|
   |title   |Cədvəldən  |
   |price   |42         |
   |stock   |7          |

* "PUT" sorğusu gönder "/products/1"
* Status kodunun "200" olmalıdır
* Json cavabında "title" deyeri "Cədvəldən" beraberdir
* Yeni API sorğusu hazırla
* Body olaraq "{\"title\": \"Patched\"}" metnini elave et
* Endpoint "/products/1" olsun
* Patch request and display respons
* Json cavabında "title" deyeri "Patched" beraberdir
* Initalize request specification
* Add Endpoint "/products/1"
* Put request and display respons
* Status kodunun "200" olmalıdır
* Initalize request specification
* Add Endpoint "/products/1"
* Delete request and display response
* Status kodunun "200" olmalıdır
* Json cavabında "isDeleted" deyeri "true" beraberdir
* Json cavabında "deletedOn" deyeri boş olmamalıdır

## Request body-nin cavabda əks olunması (echo), dəyişənlər, random data
tags: selftest, api, echo, data

* Set base Url to "https://postman-echo.com"
* "orderId" deyişenine "ORD-${random.number}" deyerini ver
* Initalize request specification
* Add Endpoint "/post"
* Body olaraq "selftest-order.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "200" olmalıdır
* Json cavabında "json.orderId" deyeri "${orderId}" beraberdir
* Json cavabında "json.customer.address.city" deyerini "city" olaraq yadda saxla
* Json cavabında "json.customer.address.city" deyeri "city" ile eynidir
* Json cavabında "json.customer.name" deyeri "selftest-order.json" request body-sindeki "customer.name" ile eyni olmalıdır
* Json cavabında "json.items[1].qty" deyeri "selftest-order.json" request body-sindeki "items.1.qty" ile eyni olmalıdır
* Json cavabında "json.customer.email" deyeri "test_.+@test\.com" regex-ine uyğun olmalıdır
* Json cavabında "json.customer.email" deyerinde "@test.com" olmalıdır
* Json cavabında "json.items" massivinin ölçüsü "2" olmalıdır
* Json cavabında "json.items.sum { it.qty * it.price }" deyeri "==" "120" olmalıdır
* Json cavabında "json.paid" deyeri "true" beraberdir
* Json cavabında "json.paid" deyerinin tipi "boolean" olmalıdır
* Json cavabında "json.coupon" deyeri null olmalıdır
* Json cavabında "json.coupon" açarı mövcud olmalıdır
* Json cavabında "json.coupon" deyerinin tipi "null" olmalıdır
* Json cavabında "json.orderId" deyerini "savedOrder" olaraq bütün testler üçün yadda saxla
* "savedOrder" deyişeni "${orderId}" olmalıdır
* "tarix" global deyişenine "${today}" deyerini ver
* "tarix" deyişeninin deyerini çap et

## Header, query, form, multipart, basic auth, API key
tags: selftest, api, request

* Set base Url to "https://postman-echo.com"
* Yeni API sorğusu hazırla
* Header elave et "X-Trace-Id" = "${random.uuid}"
* Headerleri elave et

   |key          |value        |
   |-------------|-------------|
   |X-Client     |gauge        |
   |Accept       |application/json|

* API key header elave et "x-api-key" = "secret-123"
* Query parametri elave et "page" = "2"
* Query parametri elave et "q" = "Bakı şəhəri"
* "GET" sorğusu gönder "/get"
* Json cavabında "headers.x-client" deyeri "gauge" beraberdir
* Json cavabında "headers.x-api-key" deyeri "secret-123" beraberdir
* Json cavabında "headers.x-trace-id" deyeri "[0-9a-f-]{36}" regex-ine uyğun olmalıdır
* Json cavabında "args.page" deyeri "2" beraberdir
* Json cavabında "args.q" deyeri "Bakı şəhəri" beraberdir
* Yeni API sorğusu hazırla
* Form parametri elave et "username" = "anar"
* Form parametri elave et "role" = "qa"
* "POST" sorğusu gönder "/post"
* Json cavabında "form.username" deyeri "anar" beraberdir
* Json cavabında "form.role" deyeri "qa" beraberdir
* Yeni API sorğusu hazırla
* Multipart fayl elave et "file" = "sample.txt"
* "POST" sorğusu gönder "/post"
* Json cavabında "files" deyeri boş olmamalıdır
* Json cavabında "files" deyerinde "sample.txt" olmalıdır
* Yeni API sorğusu hazırla
* Basic auth elave et istifadeci "postman" şifre "password"
* "GET" sorğusu gönder "/basic-auth"
* Status kodunun "200" olmalıdır
* Json cavabında "authenticated" deyeri "true" beraberdir
* Yeni API sorğusu hazırla
* "GET" sorğusu gönder "/response-headers?X-Test=abc"
* Header "X-Test" deyerinde "abc" olmalıdır
* Header "X-Test" deyerini "testHeader" olaraq yadda saxla
* "testHeader" deyişeni "abc" olmalıdır
* API e GET request gönder "https://postman-echo.com/status/404"
* Status kodunun "404" olmalıdır
* Cavabı çap et
* API base URL "https://dummyjson.com" olsun
* API e GET request gönder "/test"
* Status kodunun "200" olmalıdır
