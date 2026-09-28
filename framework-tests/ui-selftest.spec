# Framework self-test — Web UI step-ləri

Bu spec framework-ün BÜTÜN web UI step-lərini lokal playground səhifəsində yoxlayır
və eyni zamanda hər step-in istifadə nümunəsidir.
İcra: `./framework-tests/run-selftest.sh ui`  (lokal server: http://localhost:8765)

## Form: yazmaq, təmizləmək, dropdown, checkbox, input dəyəri
tags: selftest, ui, form

* Brauzeri aç ve keçid et "http://localhost:8765/playground.html"
* Sehifenin tam yüklenmesini gözle
* Sehife başlığı "Gauge Playground" olmalıdır
* Sehife başlığında "Playground" olmalıdır
* URL "playground.html" içermelidir
* URL "http://localhost:8765/playground.html" olmalıdır
* "PG Title" görünür olmalıdır
* "PG Title" elementinin metni "Playground" olmalıdır
* "PG Name Input" elementine "Anar" yaz
* "PG Name Input" input deyeri "Anar" olmalıdır
* "PG Name Input" elementini temizle
* "PG Name Input" input deyeri "" olmalıdır
* "PG Name Input" elementine "Anar" yaz ve Tab düymesine bas
* "PG Email Input" elementine "${random.email}" yaz
* "PG Email Input" elementinin "value" atributunda "@test.com" olmalıdır
* "PG Password Input" elementine "Gizli123!" yaz ve Enter düymesine bas
* "PG Prefilled Input" input deyeri "hazır" olmalıdır
* "PG City Select" dropdown-undan "Gəncə" metnini seç
* "PG City Select" input deyeri "ganja" olmalıdır
* "PG City Select" dropdown-undan "sumqayit" deyerini seç
* "PG City Select" dropdown-undan "0" indeksli seçimi seç
* "PG Agree Checkbox" checkbox-unu işaretle
* "PG Agree Checkbox" seçilmiş olmalıdır
* "PG Agree Checkbox" checkbox-unun işaretini kaldır
* "PG Agree Checkbox" seçilmemiş olmalıdır
* "PG Agree Checkbox" checkbox-unu işaretle
* "PG Submit Button" aktiv olmalıdır
* "PG Disabled Button" deaktiv olmalıdır
* "PG Disabled Button" elementin içinde "Deaktiv" yazısı var
* "PG Submit Button" elementine klik et
* "PG Result" elementinin metni "Salam, Anar / baku / true" olmalıdır
* "PG Submit Button" elementinin "class" atributu "btn primary" olmalıdır

## Klaviatura, dəyişənlər və inline locator
tags: selftest, ui, keyboard, data

* Brauzeri aç ve keçid et "http://localhost:8765/playground.html"
* "PG Name Input" elementinde "ARROW_DOWN" düymesine bas
* "PG Key Result" elementinin metni "key: ArrowDown" olmalıdır
* Sehifede "ESCAPE" düymesine bas
* "PG Key Result" elementinin metni "key: Escape" olmalıdır
* "PG Name Input" elementine "Leyla" yaz ve Shift düymesine bas
* "css=#name" input deyeri "Leyla" olmalıdır
* "PG Title" elementinin metnini "basliq" olaraq yadda saxla
* "basliq" deyişeni "Playground" olmalıdır
* "PG Title" elementinin "id" atributunu "basliqId" olaraq yadda saxla
* "xpath=//h1[@id='${basliqId}']" elementinin metni "${basliq}" olmalıdır
* "ad" deyişenine "Nigar" deyerini ver
* "id=name" elementine "${ad}" yaz
* "PG Name Input" input deyeri "Nigar" olmalıdır
* "ad" deyişeninin deyerini çap et

## Mouse: iki klik, sağ klik, hover, drag & drop, JS klik
tags: selftest, ui, mouse

* Brauzeri aç ve keçid et "http://localhost:8765/playground.html"
* "PG Double Button" elementine iki defe klik et
* "PG Mouse Result" elementinin metni "iki klik" olmalıdır
* "PG Context Area" elementine sağ klik et
* "PG Mouse Result" elementinin metni "sag klik" olmalıdır
* "PG Hover Menu" görünmemelidir
* "PG Hover Area" elementinin üzerine gel
* "PG Hover Menu" görünür olmalıdır
* "PG Drag Source" elementini "PG Drop Target" elementinin üzerine sürükle
* "PG Drop Result" elementinin metni "Düşdü" olmalıdır
* "PG Double Button" elementine JavaScript ile klik et

## Siyahılar, mətnə görə klik, linklər
tags: selftest, ui, list

* Brauzeri aç ve keçid et "http://localhost:8765/playground.html"
* "PG List Items" elementlerinin sayı "3" olmalıdır
* "PG List Items" elementlerinin sayı en az "2" olmalıdır
* "PG List Items" siyahısında "Armud" metnli elemente klik et
* "PG Item Result" elementinin metni "Seçildi: Armud" olmalıdır
* "PG List Items" siyahısında "3" nömreli elemente klik et
* "PG Item Result" elementinin metni "Seçildi: Heyva" olmalıdır
* "Mətnlə tap məni" metnli elemente klik et
* "PG Item Result" elementinin metni "mətnlə klik" olmalıdır
* "PG Docs Link" elementine klik et
* URL "#docs" içermelidir
* "PG Item Result" elementinin metni "link" olmalıdır
* Sehifede "Mətnlə tap məni" yazısı olmalıdır

## Gözləmələr və dinamik elementlər
tags: selftest, ui, wait

* Brauzeri aç ve keçid et "http://localhost:8765/playground.html"
* "PG Delay Button" kliklene bilene qeder gözle
* "PG Delay Button" elementine klik et
* "PG Delayed Text" görsensin deye maksimum "5" saniye gözle
* "PG Spinner" yox olana qeder maksimum "5" saniye gözle
* "PG Removable" görünür olmalıdır
* "PG Remove Button" elementine klik et
* "PG Removable" sehifede mövcud olmamalıdır
* "id=notExisting" elementi "1" saniye içinde görünerse klik et
* "1" saniye gözle

## Alert, confirm, prompt
tags: selftest, ui, alert

* Brauzeri aç ve keçid et "http://localhost:8765/playground.html"
* "PG Alert Button" elementine klik et
* Alert metninde "Salam alert" olmalıdır
* Alert-i qebul et
* "PG Confirm Button" elementine klik et
* Alert-i qebul et
* "PG Dialog Result" elementinin metni "OK" olmalıdır
* "PG Confirm Button" elementine klik et
* Alert-i legv et
* "PG Dialog Result" elementinin metni "Cancel" olmalıdır
* "PG Prompt Button" elementine klik et
* Alert-e "Anar" yaz ve qebul et
* "PG Dialog Result" elementinin metni "Prompt: Anar" olmalıdır

## Tab, iframe, naviqasiya
tags: selftest, ui, window

* Brauzeri aç ve keçid et "http://localhost:8765/playground.html"
* "PG New Tab Link" elementine klik et
* Yeni açılan taba keç
* Sehife başlığı "Second Page" olmalıdır
* "PG Second Title" elementinin metni "İkinci səhifə" olmalıdır
* Cari tabı bağla ve esas taba qayıt
* Sehife başlığı "Gauge Playground" olmalıdır
* Yeni tabda "http://localhost:8765/second.html" aç
* "2" nömreli taba keç
* URL "second.html" içermelidir
* "1" nömreli taba keç
* "PG Frame" iframe-ine keç
* "PG Frame Button" elementine klik et
* "PG Frame Result" elementinin metni "frame klik" olmalıdır
* Iframe-den esas sehifeye qayıt
* "http://localhost:8765/second.html" adresine keçid et
* Evvelki sehifeye qayıt
* URL "playground.html" içermelidir
* Növbeti sehifeye keç
* URL "second.html" içermelidir
* Sehifeni yenile
* Pencere ölçüsünü "1280" x "800" et

## Scroll, fayl yükləmə, cookie, storage, JS, screenshot
tags: selftest, ui, misc

* "chrome-headless" brauzeri aç ve keçid et "http://localhost:8765/playground.html"
* Sehifenin aşağısına scroll et
* "PG Bottom Button" görünür olmalıdır
* Sehifenin yuxarısına scroll et
* "500" piksel vertical scroll et
* "50" piksel horizontal scroll et
* "PG Bottom Button" elementine scroll et
* "PG Bottom Button" elementine scroll et ve klik et
* "PG Bottom Button" elementin içinde "aşağı kliklendi" yazısı var
* "PG Upload Input" elementine "sample.txt" faylını yükle
* "PG Upload Result" elementinin metni "sample.txt" olmalıdır
* Cookie elave et "sessiya" = "abc123"
* "sessiya" cookie-si mövcud olmalıdır
* Bütün cookie-leri sil
* LocalStorage-e yaz "lang" = "az"
* Sehifeni yenile
* "PG Storage Result" elementinin metni "storage: az" olmalıdır
* LocalStorage ve SessionStorage-i temizle
* JavaScript icra et "document.getElementById('title').textContent = 'JS dəyişdi'"
* "PG Title" elementinin metni "JS dəyişdi" olmalıdır
* Ekran görüntüsü çek
* Brauzeri bağla
