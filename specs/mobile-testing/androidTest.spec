# Android Mobile Test

Bu spec-i işlətmək üçün əvvəlcədən:
  1. `appium` serverini işə sal (default port 4723)
  2. Android emulyator boot et (`emulator -avd <name>`)
  3. env dəyişənləri: `ANDROID_APP_PACKAGE=com.android.settings ANDROID_APP_ACTIVITY=.Settings`

## Android Settings tətbiqini açma pozitiv ssenari

* Android tətbiqini aç
* Android mətni "Network & internet" görsənsin deyə maksimum "15" saniyə gözlə
* Android mətni "Network & internet" üzərinə klik et
* Android mətni "Internet" görsənsin deyə maksimum "10" saniyə gözlə
* Android tətbiqini bağla
