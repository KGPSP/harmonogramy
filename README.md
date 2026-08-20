# Harmonogramy — BIŁ KG PSP

Statyczne strony z harmonogramami realizacji projektów prowadzonych przez Biuro Informatyki i Łączności Komendy Głównej Państwowej Straży Pożarnej.

**Strona:** https://kgpsp.github.io/harmonogramy/

## Zawartość

| Harmonogram | Adres | Zakres | Termin |
|---|---|---|---|
| **ALARM.soia** | [`/alarm-soia/`](https://kgpsp.github.io/harmonogramy/alarm-soia/) | portal ostrzegania + aplikacje mobilne Android/iOS | 30.11.2026 |
| **ZKSWD** | [`/zkswd/`](https://kgpsp.github.io/harmonogramy/zkswd/) | wspomaganie decyzji ZK — MVP od 21.08.2026, wydania co tydzień | 18.12.2026 |
| **CivCom** | [`/civcom/`](https://kgpsp.github.io/harmonogramy/civcom/) | komunikator ZK i OL (civcom.soia.info) | 14.09.2026 |

## Struktura

```
index.html                strona główna — lista harmonogramów
alarm-soia/index.html     harmonogram ALARM.soia
zkswd/index.html          harmonogram ZKSWD
civcom/index.html         harmonogram CivCom
assets/harmonogram.css    wspólny system wizualny (motyw jasny i ciemny)
assets/timeline.js        automatyczne pozycjonowanie linii „dziś”
assets/logo/              oficjalne logotypy: PSP, MSWiA, RCB, OLiOC
_tools/build.py           generator stron
_tools/pages.py           dane harmonogramów (belki, kamienie milowe, ryzyka)
og-alarm-soia.png         miniatura do udostępniania linku
.nojekyll                 wyłącza przetwarzanie Jekyll
```

Brak build stepu i zależności npm — publikacja to GitHub Pages z gałęzi `main`, katalog `/`.

## Linia „dziś” ustawia się sama

Każdy wykres deklaruje trzy atrybuty na elemencie `.chart`:

```html
data-t-start="2026-08-03"     poniedziałek pierwszej kolumny
data-t-weeks="18"             liczba kolumn tygodniowych
data-t-deadline="2026-11-30"  data ostateczna
```

`assets/timeline.js` wylicza z nich pozycję pionowej linii „dziś”, jej etykietę, dzisiejszą datę w kaflu nagłówka, pozostały czas do terminu (z polską odmianą: *1 tydzień / 2 tygodnie / 5 tygodni*) oraz stopkę „stan na …”. Strona nie starzeje się między wypchnięciami do repozytorium. Gdy dzisiejsza data wypada poza zakresem wykresu, linia jest ukrywana.

## Jak zmienić harmonogram

Strony są zwykłym HTML i można je edytować ręcznie. Wygodniej jednak zmienić **dane** i przegenerować:

```sh
# edytuj _tools/pages.py — belki, kamienie milowe, ryzyka, teksty
python3 _tools/build.py
```

Generator pilnuje, żeby matematyka kolumn była identyczna na każdej stronie. Model siatki: jedna kolumna = jeden tydzień (poniedziałek–niedziela); pozycja daty na osi = `(dni_od_startu + 0,5) / (tygodnie × 7)`.

Konwencja belek w `pages.py`: `s` = pierwszy tydzień (numerowany od 1), `e` = tydzień **po** ostatnim.

## Jak dodać kolejny harmonogram

1. Dopisz słownik strony w `_tools/pages.py` i dodaj go do listy `PAGES`.
2. Dodaj kafelek w sekcji „Aktualne" w `HUB` (ten sam plik).
3. `python3 _tools/build.py`, commit na `main` — Pages przebuduje się automatycznie.

## Logotypy

Logotypy w `assets/logo/` pochodzą z repozytorium [`KGPSP/loga-partnerzy`](https://github.com/KGPSP/loga-partnerzy). Do plików RCB i OLiOC dodano atrybut `viewBox`, żeby skalowały się w przeglądarce; poza tym nie były modyfikowane. Pasek instytucji jest osadzony na białej płycie, dzięki czemu znaki zachowują poprawne barwy również w ciemnym motywie strony.

## Uwagi

Harmonogramy mają charakter planistyczny. Daty zależne od podmiotów zewnętrznych (czas weryfikacji aplikacji w App Store i Google Play, wydanie certyfikatów podpisu kodu) są szacunkowe i nie podlegają harmonogramowi KG PSP. Bieżący stan realizacji poszczególnych kamieni milowych prowadzony jest w kartach projektów, nie na tych stronach.
