# irshad.az — Ana səhifə, naviqasiya, dil, footer və mağazalar

Test mühiti: https://irshad.az
Excel: "UI Test Cases" vərəqi (TS-UI-02 Ana səhifə, TS-UI-03 Naviqasiya, TS-UI-04 Dil, TS-UI-16 Mağazalar, TS-UI-17 Footer)
Qeyd: dəyişkən məzmun (banner, "Həftənin təklifi", axtarış placeholder-i) yoxlanılmır.

tags: ui, irshad

## TC-UI-HOME-001 Ana səhifənin xətasız açılması və əsas blokların görünməsi

tags: home, smoke

* Brauzeri aç ve keçid et "https://irshad.az/az"
* Sehifenin tam yüklenmesini gözle
* "Header Logo" görünür olmalıdır
* "Kataloq Button" görünür olmalıdır
* "Axtaris Input" görünür olmalıdır
* "Muqayise Link" görünür olmalıdır
* "Beyendim Link" görünür olmalıdır
* "Sebet Link" görünür olmalıdır
* "Sexsi Kabinet Link" görünür olmalıdır
* "Qaynar Xett Link" görünür olmalıdır
* "Footer" elementine scroll et
* "Footer" görünür olmalıdır

## TC-UI-HOME-002 Header-də qaynar xətt nömrəsinin (*0171) göstərilməsi

tags: home

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Qaynar Xett Link" görünür olmalıdır
* "Qaynar Xett Link" elementinin "href" atributu "tel:*0171" olmalıdır

## TC-UI-HOME-003 Loqoya klikləməklə daxili səhifədən ana səhifəyə qayıtmaq

tags: home

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* "Header Logo" elementine klik et
* URL "https://irshad.az/az" olmalıdır

## TC-UI-HOME-004 Kateqoriya menyusunda 15 əsas kateqoriyanın göstərilməsi

tags: home, navigation

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Kataloq Button" elementine klik et
* "Menyu Telefon ve aksesuarlar" görsensin deye maksimum "5" saniye gözle
* "Kataloq Esas Kateqoriya" elementlerinin sayı "15" olmalıdır
* Sehifede "Telefon və aksesuarlar" yazısı olmalıdır
* Sehifede "Böyük məişət texnikası" yazısı olmalıdır
* Sehifede "Kiçik məişət texnikası" yazısı olmalıdır
* Sehifede "TV və Audio" yazısı olmalıdır
* Sehifede "Foto texnika" yazısı olmalıdır
* Sehifede "Notbuk, planşet və kompüter texnikası" yazısı olmalıdır
* Sehifede "Evə uyğun məhsullar" yazısı olmalıdır
* Sehifede "Mebellər və tekstil" yazısı olmalıdır
* Sehifede "Nəqliyyat və Əyləncə" yazısı olmalıdır
* Sehifede "İdman və sağlamlıq" yazısı olmalıdır
* Sehifede "Avtomobil üçün məhsullar" yazısı olmalıdır
* Sehifede "İnşaat" yazısı olmalıdır
* Sehifede "Dəftərxana ləvazimatları" yazısı olmalıdır
* Sehifede "Hədiyyə kartları" yazısı olmalıdır

## TC-UI-HOME-005 Header elementlərinin bütün əsas səhifələrdə eyni qalması

tags: home

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* "Header Logo" görünür olmalıdır
* "Kataloq Button" görünür olmalıdır
* "Axtaris Input" görünür olmalıdır
* "Sebet Link" görünür olmalıdır
* "Sexsi Kabinet Link" görünür olmalıdır
* "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white" adresine keçid et
* "Header Logo" görünür olmalıdır
* "Kataloq Button" görünür olmalıdır
* "Axtaris Input" görünür olmalıdır
* "Sebet Link" görünür olmalıdır
* "Sexsi Kabinet Link" görünür olmalıdır
* "https://irshad.az/az/magazalar" adresine keçid et
* "Header Logo" görünür olmalıdır
* "Kataloq Button" görünür olmalıdır
* "Axtaris Input" görünür olmalıdır
* "Sebet Link" görünür olmalıdır
* "Sexsi Kabinet Link" görünür olmalıdır

## TC-UI-HOME-008 Header-dəki "Bəyəndim" ikonu ilə Bəyəndiklərim səhifəsinin açılması

tags: home

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Beyendim Link" elementine klik et
* URL "https://irshad.az/az/beyendiklerim" olmalıdır

## TC-UI-HOME-011 Header-in üst xəttindəki linklərin göstərilməsi

tags: home

Narıncı çərçivəli sonuncu link mövsümi kampaniyadır və adı dəyişir (06–15.10: "Kondisionerlər", 15.10-dan: "Kombilər") — test onu adına görə yox, yerinə və stilinə görə yoxlayır.

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Ust Xett Kampaniyalar" görünür olmalıdır
* "Ust Xett Magazalar" görünür olmalıdır
* "Ust Xett Korporativ" görünür olmalıdır
* "Ust Xett Samsung" görünür olmalıdır
* "Ust Xett Apple" görünür olmalıdır
* "Ust Xett Honor" görünür olmalıdır
* "Ust Xett Outlet" görünür olmalıdır
* "Ust Xett Movsumi Kampaniya Linki" görünür olmalıdır
* "Ust Xett Movsumi Kampaniya Linki" elementinin "class" atributunda "btn-orange-transparent" olmalıdır

## TC-UI-HOME-012 Header-in üst xəttindəki linklərin hər birinin xətasız açılması

tags: home

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Ust Xett Kampaniyalar" elementine klik et
* URL "/az/kampaniyalar" içermelidir
* Sehifenin tam yüklenmesini gözle
* "Sehife 404 Mesaji" sehifede mövcud olmamalıdır
* "Ust Xett Magazalar" elementine klik et
* URL "/az/magazalar" içermelidir
* Sehifenin tam yüklenmesini gözle
* "Sehife 404 Mesaji" sehifede mövcud olmamalıdır
* "Ust Xett Korporativ" elementine klik et
* URL "/az/musteri-ucun/korporativ-satislar" içermelidir
* Sehifenin tam yüklenmesini gözle
* "Sehife 404 Mesaji" sehifede mövcud olmamalıdır
* "Ust Xett Samsung" elementine klik et
* URL "/brend/samsung" içermelidir
* Sehifenin tam yüklenmesini gözle
* "Sehife 404 Mesaji" sehifede mövcud olmamalıdır
* "Ust Xett Apple" elementine klik et
* URL "/brend/apple" içermelidir
* Sehifenin tam yüklenmesini gözle
* "Sehife 404 Mesaji" sehifede mövcud olmamalıdır
* "Ust Xett Honor" elementine klik et
* URL "/brend/honor" içermelidir
* Sehifenin tam yüklenmesini gözle
* "Sehife 404 Mesaji" sehifede mövcud olmamalıdır
* "Ust Xett Outlet" elementine klik et
* URL "/az/outlet" içermelidir
* Sehifenin tam yüklenmesini gözle
* "Sehife 404 Mesaji" sehifede mövcud olmamalıdır
* "https://irshad.az/az" adresine keçid et
* "Ust Xett Movsumi Kampaniya Linki" elementinin "href" atributunu "kampaniyaLinki" olaraq yadda saxla
* "Ust Xett Movsumi Kampaniya Linki" elementine klik et
* URL "${kampaniyaLinki}" içermelidir
* Sehifenin tam yüklenmesini gözle
* "Sehife 404 Mesaji" sehifede mövcud olmamalıdır
* "Header Logo" görünür olmalıdır

## TC-UI-NAV-001 Menyudan Mobil telefonlar kateqoriyasına keçid

tags: navigation, smoke

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Kataloq Button" elementine klik et
* "Menyu Telefon ve aksesuarlar" görsensin deye maksimum "5" saniye gözle
* "Menyu Telefon ve aksesuarlar" elementinin üzerine gel
* "Menyu Mobil telefonlar" kliklene bilene qeder gözle
* "Menyu Mobil telefonlar" elementine klik et
* URL "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar" olmalıdır
* Sehifede "Mobil telefonlar" yazısı olmalıdır

## TC-UI-NAV-002 Kateqoriya səhifəsində breadcrumb-ın düzgün göstərilməsi

tags: navigation

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* "Breadcrumb Elementleri" elementlerinin sayı "3" olmalıdır
* "Breadcrumb Irshad" görünür olmalıdır
* "Breadcrumb Telefon ve aksesuarlar" görünür olmalıdır
* "Breadcrumb Mobil telefonlar" görünür olmalıdır

## TC-UI-NAV-003 Breadcrumb-dakı ana kateqoriya linkinin işləməsi

tags: navigation

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* "Breadcrumb Telefon ve aksesuarlar" elementine klik et
* URL "https://irshad.az/az/telefon-ve-aksesuarlar" olmalıdır
* Sehifede "Telefon və aksesuarlar" yazısı olmalıdır

## TC-UI-NAV-004 Breadcrumb-ın birinci elementi ilə ana səhifəyə qayıtmaq

tags: navigation

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* "Breadcrumb Irshad" elementine klik et
* URL "https://irshad.az/az" olmalıdır

## TC-UI-NAV-006 Məhsul səhifəsində breadcrumb-ın məhsulun kateqoriyasını göstərməsi

tags: navigation, pdp

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white"
* "Breadcrumb Telefon ve aksesuarlar" görünür olmalıdır
* "Breadcrumb Mobil telefonlar" görünür olmalıdır
* "Breadcrumb Mobil telefonlar" elementine klik et
* URL "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar" olmalıdır

## TC-UI-NAV-007 15 əsas kateqoriyanın hər birinin xətasız açılması

tags: navigation

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar"
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/boyuk-meiset-texnikasi" adresine keçid et
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/kicik-meiset-texnikasi" adresine keçid et
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/tv-ve-audio" adresine keçid et
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/foto-texnika" adresine keçid et
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/notbuk-planset-ve-komputer-texnikasi" adresine keçid et
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/eve-uygun" adresine keçid et
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/mebeller-ve-tekstil" adresine keçid et
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/neqliyyat-ve-eylence" adresine keçid et
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/idman-ve-saglamliq" adresine keçid et
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/avtomobil-ucun-mehsullar" adresine keçid et
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/insaat-mehsullari" adresine keçid et
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/defterxana-levazimatlari" adresine keçid et
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/outlet" adresine keçid et
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/hediyye-kartlari" adresine keçid et
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır

## TC-UI-NAV-008 Outlet bölməsinin açılması

tags: navigation

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Ust Xett Outlet" elementine klik et
* URL "https://irshad.az/az/outlet" olmalıdır
* Sehifede "Outlet" yazısı olmalıdır

## TC-UI-NAV-009 Kampaniyalar səhifəsinin açılması

tags: navigation

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Ust Xett Kampaniyalar" elementine klik et
* URL "https://irshad.az/az/kampaniyalar" olmalıdır
* Sehifede "Kampaniyalar" yazısı olmalıdır

## TC-UI-NAV-010 Brauzerin "Geri" düyməsi ilə əvvəlki səhifəyə qayıtmaq

tags: navigation

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar" adresine keçid et
* "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white" adresine keçid et
* Evvelki sehifeye qayıt
* URL "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar" olmalıdır
* Evvelki sehifeye qayıt
* URL "https://irshad.az/az" olmalıdır

## TC-UI-LANG-001 Saytın rus dilinə keçirilməsi

tags: language

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Dil Secici" elementinin üzerine gel
* "Rus Dili Link" kliklene bilene qeder gözle
* "Rus Dili Link" elementine klik et
* URL "https://irshad.az/ru" içermelidir
* Sehifede "Русский язык" yazısı olmalıdır

## TC-UI-LANG-002 Rus dilindən Azərbaycan dilinə geri keçid

tags: language

* Brauzeri aç ve keçid et "https://irshad.az/ru"
* "Dil Secici" elementinin üzerine gel
* "Azerbaycan Dili Link" kliklene bilene qeder gözle
* "Azerbaycan Dili Link" elementine klik et
* URL "https://irshad.az/az" içermelidir
* Sehifede "Azərbaycan dili" yazısı olmalıdır
* Sehifede "Kataloq" yazısı olmalıdır

## TC-UI-LANG-003 Kateqoriya səhifəsində dil dəyişəndə eyni kateqoriyada qalmaq

tags: language

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* "Dil Secici" elementinin üzerine gel
* "Rus Dili Link" kliklene bilene qeder gözle
* "Rus Dili Link" elementine klik et
* URL "https://irshad.az/ru/" içermelidir
* "Breadcrumb Elementleri" elementlerinin sayı "3" olmalıdır

## TC-UI-FT-001 Footer bölmələrinin və linklərinin göstərilməsi

tags: footer

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Footer" elementine scroll et
* "Footer" görünür olmalıdır
* "Footer" elementin içinde "Şirkət" yazısı var
* "Footer" elementin içinde "Şadkart" yazısı var
* "Footer" elementin içinde "Əlaqə" yazısı var
* "Footer" elementin içinde "Bizi izləyin" yazısı var
* "Footer Daxili Linkler" elementlerinin sayı "14" olmalıdır
* "Footer Sosial Ikonlar" elementlerinin sayı "8" olmalıdır
* "Footer Tetbiq Duymeleri" elementlerinin sayı "2" olmalıdır
* "Footer Copyright" elementin içinde "Bütün hüquqlar qorunur" yazısı var

## TC-UI-FT-002 Footer linklərinin hər birinin xətasız açılması

tags: footer

Qeyd: footer linklərinə birbaşa klik "element click intercepted" xətası verir (səhifənin aşağısındakı sabit elementlər linki örtür) — klik əvəzinə hər linkin ünvanı yoxlanılır və həmin ünvan açılır.

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Footer Haqqimizda" elementinin "href" atributu "https://irshad.az/az/sirket/haqqimizda" olmalıdır
* "Footer Magazalar" elementinin "href" atributu "https://irshad.az/az/magazalar" olmalıdır
* "Footer Vakansiyalar" elementinin "href" atributu "https://irshad.az/az/sirket/vakansiyalar" olmalıdır
* "Footer Kampaniyalar" elementinin "href" atributu "https://irshad.az/az/kampaniyalar" olmalıdır
* "Footer Sertlerimiz" elementinin "href" atributu "https://irshad.az/az/musteri-ucun/sertlerimiz" olmalıdır
* "Footer Catdirilma qaydalari" elementinin "href" atributu "https://irshad.az/az/musteri-ucun/catdirilma-qaydalari" olmalıdır
* "Footer Bonus qaydalari" elementinin "href" atributu "https://irshad.az/az/musteri-ucun/bonuslardan-istifade-qaydalari" olmalıdır
* "Footer Sual-Cavab" elementinin "href" atributu "https://irshad.az/az/musteri-ucun/sual-cavab" olmalıdır
* "Footer Hisse-hisse odenis" elementinin "href" atributu "https://irshad.az/az/musteri-ucun/hisse-hisse-oedenis" olmalıdır
* "Footer Mexfilik siyaseti" elementinin "href" atributu "https://irshad.az/az/musteri-ucun/mexfilik-siyaseti" olmalıdır
* "Footer Korporativ satislar" elementinin "href" atributu "https://irshad.az/az/musteri-ucun/korporativ-satislar" olmalıdır
* "Footer Istifade qaydalari" elementinin "href" atributu "https://irshad.az/az/musteri-ucun/istifade-qaydalari" olmalıdır
* "Footer Bloq" elementinin "href" atributu "https://irshad.az/az/musteri-ucun/bloq" olmalıdır
* "Footer Sikayet ve teklifler" elementinin "href" atributu "https://irshad.az/az/musteri-ucun/sikayet-ve-teklifler" olmalıdır
* "https://irshad.az/az/sirket/haqqimizda" adresine keçid et
* URL "/az/sirket/haqqimizda" içermelidir
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/magazalar" adresine keçid et
* URL "/az/magazalar" içermelidir
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/sirket/vakansiyalar" adresine keçid et
* URL "/az/sirket/vakansiyalar" içermelidir
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/kampaniyalar" adresine keçid et
* URL "/az/kampaniyalar" içermelidir
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/musteri-ucun/sertlerimiz" adresine keçid et
* URL "/az/musteri-ucun/sertlerimiz" içermelidir
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/musteri-ucun/catdirilma-qaydalari" adresine keçid et
* URL "/az/musteri-ucun/catdirilma-qaydalari" içermelidir
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/musteri-ucun/bonuslardan-istifade-qaydalari" adresine keçid et
* URL "/az/musteri-ucun/bonuslardan-istifade-qaydalari" içermelidir
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/musteri-ucun/sual-cavab" adresine keçid et
* URL "/az/musteri-ucun/sual-cavab" içermelidir
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/musteri-ucun/hisse-hisse-oedenis" adresine keçid et
* URL "/az/musteri-ucun/hisse-hisse-oedenis" içermelidir
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/musteri-ucun/mexfilik-siyaseti" adresine keçid et
* URL "/az/musteri-ucun/mexfilik-siyaseti" içermelidir
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/musteri-ucun/korporativ-satislar" adresine keçid et
* URL "/az/musteri-ucun/korporativ-satislar" içermelidir
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/musteri-ucun/istifade-qaydalari" adresine keçid et
* URL "/az/musteri-ucun/istifade-qaydalari" içermelidir
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/musteri-ucun/bloq" adresine keçid et
* URL "/az/musteri-ucun/bloq" içermelidir
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır
* "https://irshad.az/az/musteri-ucun/sikayet-ve-teklifler" adresine keçid et
* URL "/az/musteri-ucun/sikayet-ve-teklifler" içermelidir
* "Breadcrumb Elementleri" elementlerinin sayı en az "2" olmalıdır

## TC-UI-FT-005 Footer-in bütün əsas səhifələrdə eyni olması

tags: footer

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Footer Daxili Linkler" elementlerinin sayı "14" olmalıdır
* "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar" adresine keçid et
* "Footer Daxili Linkler" elementlerinin sayı "14" olmalıdır
* "https://irshad.az/az/mehsullar/iphone-air-256-gb-cloud-white" adresine keçid et
* "Footer Daxili Linkler" elementlerinin sayı "14" olmalıdır
* "https://irshad.az/az/magazalar" adresine keçid et
* "Footer Daxili Linkler" elementlerinin sayı "14" olmalıdır

## TC-UI-FT-007 Footer-dəki copyright ilinin cari il olması

tags: footer

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Footer Copyright" elementine scroll et
* "Footer Copyright" elementin içinde "© 2000 - 2026" yazısı var

## TC-UI-STR-001 Mağazalar səhifəsinin açılması və 3 bölmənin göstərilməsi

tags: stores

* Brauzeri aç ve keçid et "https://irshad.az/az"
* "Ust Xett Magazalar" elementine klik et
* URL "https://irshad.az/az/magazalar" olmalıdır
* "Tab Baki uzre" görünür olmalıdır
* "Tab Bolgeler uzre" görünür olmalıdır
* "Tab Servis merkezi" görünür olmalıdır
* "Tab Baki uzre" elementin içinde "(" yazısı var

## TC-UI-STR-002 "Bakı üzrə" bölməsindəki sayın siyahıdakı mağaza sayına bərabər olması

tags: stores

* Brauzeri aç ve keçid et "https://irshad.az/az/magazalar"
* "Tab Baki uzre" elementine klik et
* "Tab Baki uzre" elementin içinde "(27)" yazısı var
* "Baki Magaza Kartlari" elementlerinin sayı "27" olmalıdır

## TC-UI-STR-003 "Bölgələr üzrə" bölməsindəki sayın siyahıya bərabər olması

tags: stores

* Brauzeri aç ve keçid et "https://irshad.az/az/magazalar"
* "Tab Bolgeler uzre" elementine klik et
* "Tab Bolgeler uzre" elementin içinde "(31)" yazısı var
* "Bolge Magaza Kartlari" elementlerinin sayı "31" olmalıdır

## TC-UI-STR-004 "Servis mərkəzi" bölməsindəki sayın siyahıya bərabər olması

tags: stores

* Brauzeri aç ve keçid et "https://irshad.az/az/magazalar"
* "Tab Servis merkezi" elementine klik et
* "Tab Servis merkezi" elementin içinde "(3)" yazısı var
* "Servis Merkezi Kartlari" elementlerinin sayı "3" olmalıdır

## TC-UI-STR-005 Bölmələr arasında keçid

tags: stores

* Brauzeri aç ve keçid et "https://irshad.az/az/magazalar"
* "Tab Bolgeler uzre" elementine klik et
* "Bolge Magaza Siyahisi" görünür olmalıdır
* "Baki Magaza Siyahisi" görünmemelidir
* "Tab Servis merkezi" elementine klik et
* "Servis Merkezi Siyahisi" görünür olmalıdır
* "Bolge Magaza Siyahisi" görünmemelidir
* "Tab Baki uzre" elementine klik et
* "Baki Magaza Siyahisi" görünür olmalıdır
* "Servis Merkezi Siyahisi" görünmemelidir

## TC-UI-STR-006 Hər mağaza kartında ad, ünvan və iş saatının olması

tags: stores

* Brauzeri aç ve keçid et "https://irshad.az/az/magazalar"
* "Baki Magaza Kartlari" elementlerinin sayı en az "1" olmalıdır
* "Natamam Magaza Kartlari" elementlerinin sayı "0" olmalıdır

## TC-UI-STR-008 Mağaza siyahısında dublikatın olmaması

tags: stores

Hər bölmədə (Bakı, Bölgələr, Servis mərkəzi) eyni ad və eyni ünvanla təkrarlanan kart axtarılır — kartın data-title və data-address atributları əvvəlki kartlarla müqayisə olunur; tapılan sayı 0 olmalıdır.

* Brauzeri aç ve keçid et "https://irshad.az/az/magazalar"
* "Baki Magaza Kartlari" elementlerinin sayı en az "1" olmalıdır
* "Bolge Magaza Kartlari" elementlerinin sayı en az "1" olmalıdır
* "Baki Dublikat Magaza Kartlari" elementlerinin sayı "0" olmalıdır
* "Bolge Dublikat Magaza Kartlari" elementlerinin sayı "0" olmalıdır
* "Servis Merkezi Dublikat Magaza Kartlari" elementlerinin sayı "0" olmalıdır

## TC-UI-STR-011 Mağaza siyahısında axtarış (qismən ad ilə)

tags: stores

* Brauzeri aç ve keçid et "https://irshad.az/az/magazalar"
* "Magaza Axtaris Input" görsensin deye maksimum "10" saniye gözle
* "Magaza Axtaris Input" elementine "yasa" yaz
* "Yasamal Magaza Karti" görünür olmalıdır
* "Bas Ofis Karti" görünmemelidir

## TC-UI-NAV-011 Filtrli siyahıdan məhsula keçib "Geri" qayıdanda filtrin saxlanması

tags: navigation, filter

* Brauzeri aç ve keçid et "https://irshad.az/az/telefon-ve-aksesuarlar/mobil-telefonlar"
* Sehifenin tam yüklenmesini gözle
* "400" piksel vertical scroll et
* "Brend Samsung" elementine klik et
* "Brend Samsung Checkbox" seçilmiş olmalıdır
* URL "brands" içermelidir
* Sehifeni yenile
* "Samsung Olmayan Mehsul Adlari" elementlerinin sayı "0" olmalıdır
* "Samsung Mehsul Adlari" siyahısında "1" nömreli elemente klik et
* URL "/az/mehsullar/" içermelidir
* Evvelki sehifeye qayıt
* Sehifenin tam yüklenmesini gözle
* URL "brands" içermelidir
* "Samsung Olmayan Mehsul Adlari" elementlerinin sayı "0" olmalıdır
* "Samsung Mehsul Adlari" elementlerinin sayı en az "1" olmalıdır

## TC-UI-NAV-012 Mövcud olmayan kateqoriya URL-inin 404 ilə idarə olunması

tags: navigation, negative

* Brauzeri aç ve keçid et "https://irshad.az/az/olmayan-kateqoriya-qa123"
* Sehifede "404" yazısı olmalıdır
* Sehifede "Axtardığınız səhifə tapılmadı" yazısı olmalıdır
* "Sehife 404 Mesaji" görünür olmalıdır
* "Header Logo" görünür olmalıdır
* "Kataloq Button" görünür olmalıdır
* "Footer" görünür olmalıdır

## TC-UI-NAV-013 Mövcud olmayan məhsul URL-inin 404 ilə idarə olunması

tags: navigation, negative

* Brauzeri aç ve keçid et "https://irshad.az/az/mehsullar/olmayan-mehsul-qa123"
* Sehifede "404" yazısı olmalıdır
* Sehifede "Axtardığınız səhifə tapılmadı" yazısı olmalıdır
* "PDP Basliq" sehifede mövcud olmamalıdır
* "PDP Sebete Elave Button" sehifede mövcud olmamalıdır
