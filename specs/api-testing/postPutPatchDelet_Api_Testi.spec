# POST / PUT / PATCH / DELETE — api.anarabbas.com

Bu spec-də mühafizəli endpoint-lər test olunur. Hər ssenaridən əvvəl `Login Test User` konsepti icra olunur — admin credentials ilə giriş edir və Bearer token yaddaşa saxlayır. Sonra `Authorization = "token"` header substitution ilə həmin token istifadə olunur.

* Login Test User

## 1. POST /users — yeni istifadəçi yaratma
tags: post, users, create

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/users"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "created-user.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyeri boş olmamalıdır
* Json cavabında "email" deyeri "nicat@test.az" beraberdir
* Json cavabında "name" deyeri "Nicat Əliyev" beraberdir

## 2. POST /users — boş body ilə 400 xəta
tags: post, users, validation

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/users"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{}"
* Post request and display respons
* Status kodunun "400" olmalıdır

## 3. POST /transfers — iki eyni transferin ID-si fərqli olmalıdır
tags: post, transfers, idempotency

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/transfers"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "valid-post-user.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Save value of "receipt.id" as "firstTransferId"

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/transfers"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "valid-post-user.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "receipt.id" deyeri "firstTransferId" ile ferqlidir

## 4. GET /me — Bearer token ilə profil
tags: get, me, token

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/me"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "email" deyeri "admin@test.com" beraberdir

## 5. PUT /users/:id — tam yeniləmə
tags: put, users

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/users/1"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "full-update-post.json"
* Put request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "1" beraberdir
* Json cavabında "name" deyeri boş olmamalıdır
* Json cavabında "email" deyeri boş olmamalıdır

## 6. PUT /users/:id — mövcud olmayan resurs 404
tags: put, users, error

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/users/9999999999"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "full-update-post.json"
* Put request and display respons
* Status kodunun "404" olmalıdır

## 7. POST /posts/:id/comments — şərh əlavə (partial content)
tags: post, posts, comments

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/posts/post_001/comments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"content\": \"Çox faydalı məqalə idi!\"}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "content" deyeri "Çox faydalı məqalə idi!" beraberdir

## 8. PATCH /loans/:id/status — mövcud olmayan loan 404
tags: patch, loans, error

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/loans/loan_nonexistent/status"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"status\": \"approved\", \"note\": \"Sənədlər yoxlanıldı\"}"
* Patch request and display respons
* Status kodunun "404" olmalıdır

## 9. DELETE /users/:id — uğurlu silmə
tags: delete, users

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/users/3"
* Add as a header "Authorization" = "token"
* Delete request and display response
* Status kodunun "200" olmalıdır
* Respons cavab müddeti "1500" milliSaniyeden az olmalıdır

## 10. POST /products/:id/reviews — məhsula rəy əlavə
tags: post, products, reviews

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/products/prod_002/reviews"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"rating\": 5, \"title\": \"Əla\", \"comment\": \"Çox məmnun qaldım.\"}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyeri boş olmamalıdır
* Json cavabında "comment" deyeri "Çox məmnun qaldım." beraberdir

## 11. POST /products/:id/reviews — rating/comment olmadan 400
tags: post, products, reviews, validation

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/products/prod_002/reviews"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{}"
* Post request and display respons
* Status kodunun "400" olmalıdır

## 12. POST /posts/:id/like — post bəyəni
tags: post, posts, like

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/posts/post_001/like"
* Add as a header "Authorization" = "token"
* Post request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında verilen "likes" deyeri ededdir

## 13. POST /transactions — hesablar arası köçürmə
tags: post, transactions

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/transactions"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"senderAccountId\":\"acc_001\",\"receiverAccountId\":\"acc_002\",\"amount\":50,\"description\":\"Test payment\"}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "type" deyeri "transfer" beraberdir
* Json cavabında "status" deyeri "completed" beraberdir

## 14. POST /transactions — balansdan çox məbləğ 400
tags: post, transactions, validation

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/transactions"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"senderAccountId\":\"acc_001\",\"receiverAccountId\":\"acc_002\",\"amount\":9999999,\"description\":\"Overdraft\"}"
* Post request and display respons
* Status kodunun "400" olmalıdır

## 15. POST /loans — kredit müraciəti
tags: post, loans

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/loans"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"amount\":5000,\"termMonths\":24,\"purpose\":\"car\",\"accountId\":\"acc_001\"}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "loan.status" deyeri boş olmamalıdır
* Json cavabında verilen "loan.monthlyPayment" deyeri ededdir

## 16. POST /loans — yanlış müddət 400
tags: post, loans, validation

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/loans"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"amount\":5000,\"termMonths\":9,\"purpose\":\"car\",\"accountId\":\"acc_001\"}"
* Post request and display respons
* Status kodunun "400" olmalıdır

## 17. POST /auth/logout — token ləğvi
tags: post, auth, logout

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/auth/logout"
* Add as a header "Authorization" = "token"
* Post request and display respons
* Status kodunun "200" olmalıdır