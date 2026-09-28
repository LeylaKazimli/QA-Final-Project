# API GET Testleri — api.anarabbas.com

Baza URL: https://api.anarabbas.com
Public endpoint-lər (token tələb etməyən): /users, /users/:id, /products, /products/:id, /products/:id/reviews, /posts, /posts/:id, /posts/:id/comments

* Set base Url to "https://api.anarabbas.com"

## GET /users — bütün istifadəçilərin siyahısı
tags: get, users, list

* API e GET request gönder "https://api.anarabbas.com/users"
* Status kodunun "200" olmalıdır
* Json cavabında "[0].id" deyeri boş olmamalıdır
* Json cavabında "[0].name" deyeri boş olmamalıdır
* Json cavabında "[0].email" deyeri boş olmamalıdır

## GET /users/:id — tək istifadəçi
tags: get, users

* API e GET request gönder "https://api.anarabbas.com/users/1"
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "1" beraberdir
* Json cavabında "name" deyeri boş olmamalıdır
* Json cavabında "email" deyeri boş olmamalıdır

## GET /users/:id — Server header mövcud olmalıdır
tags: get, header

* API e GET request gönder "https://api.anarabbas.com/users/1"
* Status kodunun "200" olmalıdır
* Header "Server" movcud olmalıdır

## GET /users/:id — cavab müddəti 1500 ms-dən az
tags: get, performance

* API e GET request gönder "https://api.anarabbas.com/users/1"
* Status kodunun "200" olmalıdır
* Respons cavab müddeti "1500" milliSaniyeden az olmalıdır

## GET /users/:id — mövcud olmayan resurs 404
tags: get, error

* API e GET request gönder "https://api.anarabbas.com/users/9999999"
* Status kodunun "404" olmalıdır

## GET /products — məhsullar massivi
tags: get, products

* API e GET request gönder "https://api.anarabbas.com/products"
* Status kodunun "200" olmalıdır
* Json cavabında "[0].id" deyeri boş olmamalıdır
* Json cavabında "[0].name" deyeri boş olmamalıdır

## GET /products/:id — tək məhsul
tags: get, products

* API e GET request gönder "https://api.anarabbas.com/products/prod_001"
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "prod_001" beraberdir
* Json cavabında "name" deyeri boş olmamalıdır

## GET /products/:id/reviews — rəylər və reytinq
tags: get, products, reviews

* API e GET request gönder "https://api.anarabbas.com/products/prod_001/reviews"
* Status kodunun "200" olmalıdır
* Json cavabında "productId" deyeri "prod_001" beraberdir
* Json cavabında verilen "rating" deyeri ededdir
* Json cavabında verilen "reviewCount" deyeri ededdir

## GET /posts — total sayı və data massivi
tags: get, posts

* API e GET request gönder "https://api.anarabbas.com/posts"
* Status kodunun "200" olmalıdır
* Json cavabında verilen "total" deyeri ededdir
* Json cavabında "data[0].id" deyeri boş olmamalıdır
* Json cavabında "data[0].title" deyeri boş olmamalıdır

## GET /posts/:id — tam post detalı
tags: get, posts

* API e GET request gönder "https://api.anarabbas.com/posts/post_001"
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "post_001" beraberdir
* Json cavabında "title" deyeri boş olmamalıdır
* Json cavabında verilen "stats.views" deyeri ededdir

## GET /posts/:id/comments — postun şərhləri
tags: get, posts, comments

* API e GET request gönder "https://api.anarabbas.com/posts/post_001/comments"
* Status kodunun "200" olmalıdır
* Json cavabında "postId" deyeri "post_001" beraberdir
* Json cavabında verilen "total" deyeri ededdir