# Harmonogramy — BIŁ KG PSP

Statyczne strony z harmonogramami realizacji projektów prowadzonych przez Biuro Informatyki i Łączności Komendy Głównej Państwowej Straży Pożarnej.

**Strona:** https://kgpsp.github.io/harmonogramy/

## Zawartość

| Harmonogram | Adres | Termin |
|---|---|---|
| **ALARM.soia** — portal ostrzegania + aplikacje mobilne Android/iOS | [`/alarm-soia/`](https://kgpsp.github.io/harmonogramy/alarm-soia/) | 30.11.2026 |

## Struktura

```
index.html              strona główna — lista harmonogramów
alarm-soia/index.html   harmonogram ALARM.soia (samodzielny plik, bez zależności zewnętrznych poza Google Fonts)
og-alarm-soia.png       miniatura do udostępniania linku
.nojekyll               wyłącza przetwarzanie Jekyll
```

Każdy harmonogram jest pojedynczym plikiem HTML — style są osadzone w pliku, brak build stepu i zależności npm. Publikacja: GitHub Pages z gałęzi `main`, katalog `/`.

## Jak dodać kolejny harmonogram

1. Utwórz katalog `<slug>/` z plikiem `index.html`.
2. Dodaj kafelek w `index.html` w sekcji „Aktualne".
3. Commit na `main` — Pages przebuduje się automatycznie.

## Uwagi

Harmonogramy mają charakter planistyczny. Daty zależne od podmiotów zewnętrznych (m.in. czas weryfikacji aplikacji w App Store i Google Play) są szacunkowe i nie podlegają harmonogramowi KG PSP.
