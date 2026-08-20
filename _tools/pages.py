# -*- coding: utf-8 -*-
"""Dane harmonogramów. Zmiana treści = zmiana tego pliku + `python3 _tools/build.py`.

Konwencja belek: s = pierwszy tydzień (1-indeksowany), e = tydzień PO ostatnim.
Tydzień 1 zaczyna się w dniu `start` (poniedziałek).
"""

# =============================================================== ALARM.soia

ALARM_ASIDE = """
    <div class="done" style="margin-top:6px">
      <span class="eyebrow" style="margin-right:2px">Za nami</span>
      <span class="chip"><b>22.05</b> Decyzja nr 59 KG PSP — powołanie Zespołu</span>
      <span class="chip"><b>02.06</b> Prezentacja MVP na posiedzeniu Zespołu</span>
      <span class="chip"><b>20.06</b> Uwagi RCB, MSWiA i urzędów wojewódzkich</span>
      <span class="chip"><b>15.07</b> I faza wersji produkcyjnej portalu</span>
    </div>
"""

ALARM_SECTIONS = """  <section class="critical">
    <div class="hd">
      <span class="tag">Ścieżka krytyczna</span>
      <h3 style="flex:1 1 320px">O terminie całości rozstrzyga jedna sprawa: konto Apple</h3>
    </div>
    <p class="lead" style="max-width:80ch">Aplikacji na iPhone’a nie da się przekazać testerom ani opublikować bez uprawnień na firmowym koncie Apple Developer. Kod powstaje równolegle z Androidem i nie jest problemem — problemem jest to, że <b>od momentu uzyskania uprawnień do publikacji w App Store potrzeba około ośmiu tygodni</b>. Licząc wstecz od 30 listopada, uprawnienia muszą być na miejscu <b>najpóźniej 30 września</b>. Każdy tydzień opóźnienia po tej dacie to tydzień opóźnienia wersji na iPhone’a — Android i portal zdążą niezależnie.</p>
    <div class="chain">
      <div class="step first"><span class="sn">Warunek</span><span class="st">Uprawnienia na koncie Apple Developer</span><span class="sd">do 30.09</span></div>
      <div class="step"><span class="sn">Krok 1</span><span class="st">Certyfikaty i profile, pierwszy build</span><span class="sd">ok. 2 tyg.</span></div>
      <div class="step"><span class="sn">Krok 2</span><span class="st">Beta w TestFlight z użytkownikami</span><span class="sd">ok. 4 tyg.</span></div>
      <div class="step"><span class="sn">Krok 3</span><span class="st">Weryfikacja Apple przed publikacją</span><span class="sd">do 2 tyg.</span></div>
      <div class="step last"><span class="sn">Efekt</span><span class="st">Aplikacja dostępna w App Store</span><span class="sd">27.11</span></div>
    </div>
  </section>

"""

ALARM = {
    "slug": "alarm-soia",
    "title": "Harmonogram ALARM.soia — KG PSP",
    "ogtitle": "Harmonogram ALARM.soia",
    "desc": "Harmonogram produkcji ALARM.soia: portal ostrzegania oraz aplikacje mobilne Android i iOS. Fazy, testy, kamienie milowe i ścieżka krytyczna do gotowości produkcyjnej 30.11.2026.",
    "ogimage": "og-alarm-soia.png",
    "favicon": "🚨",
    "eyebrow": "SOiA · Biuro Informatyki i Łączności KG PSP",
    "h1": "Harmonogram<br>ALARM.soia",
    "lead": "Publiczna warstwa ostrzegania: <b>portal ALARM.soia</b> (dotychczas SOiA-ALERT) wraz z otwartym feedem alertów oraz <b>aplikacjami mobilnymi na Android i iOS</b>. Linia czasu pokazuje, co budujemy, kiedy testujemy i co musi się wydarzyć, żeby całość była gotowa produkcyjnie w listopadzie 2026.",
    "facts": [
        {"k": "Dziś", "v": "20.08.2026", "n": "14 tygodni do końca", "auto_date": True, "auto_left": True},
        {"k": "Data ostateczna", "v": "30.11.2026", "n": "gotowość produkcyjna całości", "critical": True},
        {"k": "Portal", "v": "na ukończeniu", "n": "wdrożenie etapami od września"},
        {"k": "Aplikacje mobilne", "v": "iOS zablokowany", "n": "brak uprawnień na koncie Apple", "critical": True},
    ],
    "aside": ALARM_ASIDE,
    "chart_title": "Linia czasu produkcji",
    "chart_note": "Sierpień – listopad 2026 · podział tygodniowy · przewiń w bok, aby zobaczyć całość",
    "start": "2026-08-03", "weeks": 18, "deadline": "2026-11-30", "minw": 1060,
    "months": [("Sierpień", 4), ("Wrzesień", 4), ("Październik", 5), ("Listopad", 5)],
    "milestones": [
        {"date": "2026-08-31", "label": "Kontrakt API zamrożony"},
        {"date": "2026-09-30", "label": "Zamrożenie zakresu portalu<br><b>i ostateczny termin konta Apple</b>", "critical": True, "raise": True},
        {"date": "2026-10-20", "label": "Wersje kandydujące → beta"},
        {"date": "2026-11-15", "label": "Zgłoszenie aplikacji do sklepów", "raise": True},
        {"date": "2026-11-30", "label": "Gotowość produkcyjna", "final": True},
    ],
    "legend_blocker": True,
    "lanes": [
        {"name": "Portal ALARM.soia", "color": "portal", "meta": "warstwa publiczna: operatorzy CZK, obywatele, urządzenia (otwarty feed)", "rows": [
            {"name": "Dokończenie funkcji z uwag RCB i MSWiA", "dates": "3.08 – 18.09", "s": 1, "e": 8},
            {"name": "Stabilizacja i zamrożenie zakresu", "dates": "21.09 – 2.10", "s": 8, "e": 10},
            {"name": "Testy integracyjne i wydajnościowe", "dates": "28.09 – 23.10", "s": 9, "e": 13},
            {"name": "Wdrożenie etapami — ściana wschodnia", "dates": "7.09 – 6.11 · podlaskie · lubelskie · podkarpackie", "s": 6, "e": 15, "key": True},
            {"name": "Wsparcie powdrożeniowe i dostrajanie", "dates": "9.11 – 30.11", "s": 15, "e": 19},
        ]},
        {"name": "Wspólne API i feed alertów", "color": "api", "meta": "jedno źródło dla portalu, aplikacji i urządzeń — standard PL-CAP", "rows": [
            {"name": "Zamrożenie kontraktu API (PL-CAP)", "dates": "3.08 – 31.08 · warunek startu prac mobilnych", "s": 1, "e": 6, "key": True},
            {"name": "Powiadomienia push i kolejka masowej wysyłki", "dates": "31.08 – 16.10 · Google FCM + Apple APNs", "s": 5, "e": 12},
            {"name": "Testy obciążeniowe otwartego feedu", "dates": "12.10 – 6.11", "s": 11, "e": 15},
        ]},
        {"name": "Aplikacja Android", "color": "and", "meta": "React Native · dystrybucja Google Play", "rows": [
            {"name": "Budowa funkcji aplikacji", "dates": "3.08 – 9.10", "s": 1, "e": 11},
            {"name": "Testy wewnętrzne na urządzeniach", "dates": "28.09 – 23.10", "s": 9, "e": 13},
            {"name": "Beta zamknięta z użytkownikami", "dates": "19.10 – 13.11", "s": 12, "e": 16},
            {"name": "Publikacja i weryfikacja sklepu", "dates": "9.11 – 20.11", "s": 15, "e": 17, "key": True},
        ]},
        {"name": "Aplikacja iOS", "color": "ios", "meta": "React Native · dystrybucja App Store — ścieżka krytyczna", "rows": [
            {"name": "⚠ Uprawnienia na koncie Apple Developer", "dates": "stan na dziś: BRAK · potrzebne najpóźniej 30.09", "s": 1, "e": 10, "blocked": True},
            {"name": "Budowa funkcji aplikacji", "dates": "3.08 – 9.10 · równolegle z Androidem", "s": 1, "e": 11},
            {"name": "Certyfikaty, profile, pierwszy build testowy", "dates": "1.10 – 16.10 · wymaga konta Apple", "s": 10, "e": 12},
            {"name": "Beta w TestFlight", "dates": "19.10 – 13.11", "s": 12, "e": 16},
            {"name": "Publikacja i weryfikacja Apple", "dates": "9.11 – 27.11 · najdłuższa weryfikacja", "s": 15, "e": 18, "key": True},
        ]},
        {"name": "Testy i bezpieczeństwo", "color": "qa", "meta": "cały łańcuch razem, nie każdy element osobno", "rows": [
            {"name": "Testy pełnej ścieżki: portal → API → aplikacje", "dates": "12.10 – 6.11", "s": 11, "e": 15},
            {"name": "Testy bezpieczeństwa i usunięcie podatności", "dates": "19.10 – 13.11", "s": 12, "e": 16},
            {"name": "Próba sprawdzająca z RCB i WCZK", "dates": "9.11 – 20.11 · zadanie z Decyzji nr 59", "s": 15, "e": 17, "key": True},
        ]},
        {"name": "Wdrożenie, szkolenia, odbiór", "color": "dep", "meta": "żeby system był nie tylko gotowy, ale i używany", "rows": [
            {"name": "Dokumentacja i instrukcje dla operatorów", "dates": "19.10 – 20.11", "s": 12, "e": 17},
            {"name": "Szkolenia operatorów RCB i WCZK", "dates": "26.10 – 20.11", "s": 13, "e": 17},
            {"name": "Odbiór i potwierdzenie gotowości produkcyjnej", "dates": "23.11 – 30.11", "s": 17, "e": 19, "key": True},
        ]},
    ],
    "sections": ALARM_SECTIONS + """  <section class="panel">
    <h2>Co może przesunąć termin</h2>
    <div class="tablewrap">
      <table>
        <thead><tr><th style="width:34%">Ryzyko</th><th style="width:12%">Waga</th><th style="width:27%">Skutek, jeśli się zmaterializuje</th><th style="width:27%">Co je zdejmuje</th></tr></thead>
        <tbody>
          <tr><td><b>Brak uprawnień na koncie Apple</b> po 30.09</td><td class="sev"><span class="pill hi">Krytyczne</span></td><td>Wersja na iPhone’a nie zdąży na listopad. Portal i Android — bez zmian.</td><td>Decyzja właściciela konta Apple i nadanie ról do 30.09.</td></tr>
          <tr><td><b>Rozrastanie się zakresu portalu</b> — nowe uwagi po zamrożeniu</td><td class="sev"><span class="pill hi">Wysokie</span></td><td>Testy startują później, kaskadowo przesuwa się wszystko za nimi.</td><td>Twarde zamrożenie zakresu 30.09; nowe uwagi → kolejna wersja po odbiorze.</td></tr>
          <tr><td><b>Skala masowej wysyłki</b> — powiadomienia do setek tysięcy urządzeń naraz</td><td class="sev"><span class="pill md">Średnie</span></td><td>Opóźnienia w dostarczaniu alertów przy realnym zagrożeniu.</td><td>Testy obciążeniowe w październiku, przed próbą z RCB.</td></tr>
          <tr><td><b>Dostępność partnerów</b> — RCB, urzędy wojewódzkie, gminy w terminach testów</td><td class="sev"><span class="pill md">Średnie</span></td><td>Próba sprawdzająca przesuwa się poza listopad.</td><td>Terminy prób uzgodnione i rozesłane do 30.09.</td></tr>
          <tr><td><b>Weryfikacja w sklepach</b> — odrzucenie zgłoszenia przez Apple lub Google</td><td class="sev"><span class="pill lo">Niskie</span></td><td>Poprawki i ponowne zgłoszenie — zwykle kilka dni.</td><td>Zapas dwóch tygodni między zgłoszeniem a 30.11.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

""",
    "footnotes": """    <p><b>Założenia planu.</b> „Listopad 2026” przyjęto jako 30.11.2026. Terminy weryfikacji w sklepach (Apple, Google) są szacunkowe — zależą od operatorów sklepów i nie podlegają naszemu harmonogramowi. Prace nad aplikacjami mobilnymi liczone od zamrożenia kontraktu API 31.08.</p>
    <p><b>Kontekst.</b> ALARM.soia to nowa nazwa systemu SOiA-ALERT (Decyzja nr 59 KG PSP z 22.05.2026). Portal jest warstwą publiczną rodziny SOiA — obok SYRENY.soia i SWD.soia przeznaczonych dla służb.</p>""",
}

# =============================================================== ZKSWD

ZKSWD_SECTIONS = """  <section class="critical neutral">
    <div class="hd">
      <span class="tag">Zasada działania</span>
      <h3 style="flex:1 1 320px">Dlaczego co tydzień, a nie jedno duże wdrożenie w grudniu</h3>
    </div>
    <p class="lead" style="max-width:80ch">System jest już na produkcji — od 21 sierpnia, w wersji minimalnej, ale działającej. Kolejne funkcje dochodzą co tydzień, w małych porcjach. Dla decydenta ma to trzy konsekwencje: <b>ryzyko jest rozłożone</b> (nie ma jednego dnia, w którym wszystko może pójść źle), <b>uwagi wracają do systemu w ciągu tygodnia</b>, a nie po kwartale, oraz <b>na każdym etapie widać realny stan prac</b> — działającą aplikację, nie prezentację. Grudniowy termin dotyczy pełnego zakresu i pełnego kraju, nie pierwszego uruchomienia.</p>
    <div class="chain">
      <div class="step first"><span class="sn">Poniedziałek</span><span class="st">Zakres tygodnia ustalony z użytkownikami</span><span class="sd">1 dzień</span></div>
      <div class="step"><span class="sn">Wt.–czw.</span><span class="st">Budowa i testy funkcji</span><span class="sd">3 dni</span></div>
      <div class="step"><span class="sn">Piątek</span><span class="st">Regresja i wydanie na produkcję</span><span class="sd">1 dzień</span></div>
      <div class="step"><span class="sn">Kolejny tydzień</span><span class="st">Uwagi z eksploatacji wracają do zakresu</span><span class="sd">pętla</span></div>
      <div class="step last"><span class="sn">Efekt</span><span class="st">18 wydań między sierpniem a grudniem</span><span class="sd">18.12</span></div>
    </div>
  </section>

  <section class="panel">
    <h2>Co może przesunąć termin</h2>
    <div class="tablewrap">
      <table>
        <thead><tr><th style="width:34%">Ryzyko</th><th style="width:12%">Waga</th><th style="width:27%">Skutek, jeśli się zmaterializuje</th><th style="width:27%">Co je zdejmuje</th></tr></thead>
        <tbody>
          <tr><td><b>Skala krajowa</b> — 16 województw, 380 powiatów, 2 479 gmin naraz</td><td class="sev"><span class="pill hi">Wysokie</span></td><td>System zwalnia przy równoczesnej pracy wszystkich szczebli w sytuacji kryzysowej.</td><td>Testy wydajnościowe w listopadzie, przed włączaniem gmin.</td></tr>
          <tr><td><b>Integracje z systemami trzecimi</b> — SWD PSP, ALARM.soia, CivCom</td><td class="sev"><span class="pill hi">Wysokie</span></td><td>Blok III nie domyka się w listopadzie, integracje przechodzą na 2027.</td><td>Uzgodnienie interfejsów do 30.09; integracje jako osobny blok z zapasem.</td></tr>
          <tr><td><b>Bezpieczeństwo danych</b> przed produkcją krajową</td><td class="sev"><span class="pill hi">Wysokie</span></td><td>Wejście na cały kraj bez potwierdzonego poziomu zabezpieczeń.</td><td>Testy bezpieczeństwa jako warunek wejścia w produkcję krajową (23.11 – 11.12).</td></tr>
          <tr><td><b>Tempo zmian dla użytkownika</b> — nowa funkcja co tydzień</td><td class="sev"><span class="pill md">Średnie</span></td><td>Operatorzy nie nadążają za zmianami, spada zaufanie do narzędzia.</td><td>Krótki opis zmian przy każdym wydaniu, szkolenia falami, baza wiedzy WIEDZA.soia.</td></tr>
          <tr><td><b>Okres świąteczny</b> na końcu harmonogramu</td><td class="sev"><span class="pill md">Średnie</span></td><td>Brak obsady do reakcji na problemy tuż po wdrożeniu krajowym.</td><td>Zamrożenie zmian od 18.12, dyżur wsparcia do końca roku.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

"""

ZKSWD = {
    "slug": "zkswd",
    "title": "Harmonogram ZKSWD — KG PSP",
    "ogtitle": "Harmonogram ZKSWD",
    "desc": "Harmonogram ZKSWD — systemu wspomagania decyzji dla zarządzania kryzysowego. MVP produkcyjny od 21.08.2026, nowe funkcje co tydzień, pełna produkcja krajowa do grudnia 2026.",
    "favicon": "🧭",
    "eyebrow": "SOiA · Biuro Informatyki i Łączności KG PSP",
    "h1": "Harmonogram<br>ZKSWD",
    "lead": "<b>ZKSWD</b> — system wspomagania decyzji dla zarządzania kryzysowego, obsługujący centra zarządzania kryzysowego, stanowiska kierowania PSP i RCB. System działa produkcyjnie <b>od 21 sierpnia 2026</b> w wersji minimalnej; kolejne funkcje dochodzą <b>co tydzień</b>, aż do pełnego zakresu i pełnego zasięgu krajowego w grudniu 2026.",
    "facts": [
        {"k": "Dziś", "v": "20.08.2026", "n": "17 tygodni do końca", "auto_date": True, "auto_left": True},
        {"k": "Data ostateczna", "v": "18.12.2026", "n": "pełna produkcja krajowa", "critical": True},
        {"k": "Start produkcyjny", "v": "21.08.2026", "n": "MVP — produkcyjnie, nie testowo"},
        {"k": "Rytm wydań", "v": "co tydzień", "n": "18 wydań między sierpniem a grudniem"},
    ],
    "aside": "",
    "chart_title": "Linia czasu produkcji",
    "chart_note": "Sierpień – grudzień 2026 · podział tygodniowy · numery nad osią to kolejne wydania",
    "start": "2026-08-17", "weeks": 20, "deadline": "2026-12-18", "minw": 1120,
    "months": [("Sierpień", 2), ("Wrzesień", 4), ("Październik", 5), ("Listopad", 4), ("Grudzień", 5)],
    "releases": {"first": "2026-08-21", "count": 18},
    "legend_release": True,
    "milestones": [
        {"date": "2026-08-21", "label": "MVP produkcyjny", "edge_l": True},
        {"date": "2026-09-25", "label": "Blok I gotowy:<br>zdarzenia, meldunki, mapa", "raise": True},
        {"date": "2026-10-30", "label": "Blok II gotowy:<br>siły i środki, raporty"},
        {"date": "2026-11-27", "label": "Blok III gotowy:<br>integracje i bezpieczeństwo", "raise": True},
        {"date": "2026-12-18", "label": "Pełna produkcja krajowa", "final": True},
    ],
    "lanes": [
        {"name": "Wdrożenie produkcyjne", "color": "portal", "meta": "od pilotażu w SK PSP i wybranych WCZK do wszystkich szczebli zarządzania kryzysowego", "rows": [
            {"name": "MVP produkcyjny — pilotaż (SK PSP i wybrane WCZK)", "dates": "21.08 – 25.09", "s": 1, "e": 7, "key": True},
            {"name": "Rozszerzenie na wszystkie WCZK (16 województw)", "dates": "28.09 – 27.11", "s": 7, "e": 16},
            {"name": "Włączanie PCZK i GCZK", "dates": "2.11 – 18.12 · 380 powiatów · 2 479 gmin", "s": 12, "e": 19},
            {"name": "Pełna produkcja krajowa", "dates": "14.12 – 31.12", "s": 18, "e": 21, "key": True},
        ]},
        {"name": "Iteracje funkcjonalne", "color": "api", "meta": "nowa funkcjonalność co tydzień — cztery bloki tematyczne", "rows": [
            {"name": "Blok I — rejestr zdarzeń, meldunki, mapa sytuacyjna", "dates": "21.08 – 25.09 · wydania 1–5", "s": 1, "e": 7},
            {"name": "Blok II — siły i środki, raportowanie dobowe, wymiana z RCB", "dates": "28.09 – 30.10 · wydania 6–10", "s": 7, "e": 12},
            {"name": "Blok III — integracje: SWD PSP, ALARM.soia, CivCom", "dates": "2.11 – 27.11 · wydania 11–14", "s": 12, "e": 16},
            {"name": "Blok IV — analityka, wsparcie decyzji, eksporty i archiwum", "dates": "30.11 – 18.12 · wydania 15–17", "s": 16, "e": 19},
        ]},
        {"name": "Jakość i bezpieczeństwo", "color": "qa", "meta": "każde wydanie przechodzi ten sam zestaw kontroli", "rows": [
            {"name": "Regresja automatyczna przy każdym wydaniu", "dates": "21.08 – 18.12 · co tydzień", "s": 1, "e": 19},
            {"name": "Testy wydajnościowe w skali krajowej", "dates": "2.11 – 27.11", "s": 12, "e": 16},
            {"name": "Testy bezpieczeństwa przed produkcją krajową", "dates": "23.11 – 11.12 · warunek wejścia na kraj", "s": 15, "e": 18, "key": True},
        ]},
        {"name": "Wdrożenie i szkolenia", "color": "dep", "meta": "użytkownik ma nadążać za tempem zmian", "rows": [
            {"name": "Szkolenia falami — kolejne WCZK, PCZK, GCZK", "dates": "28.09 – 18.12", "s": 7, "e": 19},
            {"name": "Opis zmian przy każdym wydaniu i baza wiedzy", "dates": "21.08 – 18.12 · WIEDZA.soia", "s": 1, "e": 19},
            {"name": "Wsparcie użytkowników po wdrożeniu", "dates": "30.11 – 31.12", "s": 16, "e": 21},
        ]},
    ],
    "sections": ZKSWD_SECTIONS,
    "footnotes": """    <p><b>Założenia planu.</b> „Grudzień 2026” przyjęto jako <b>18.12.2026</b> (pełna produkcja krajowa), z zamrożeniem zmian i dyżurem wsparcia do końca roku. Podział na cztery bloki tematyczne oraz przypisanie funkcji do wydań to propozycja planistyczna do potwierdzenia z użytkownikami — potwierdzony jest rytm tygodniowy i data startu MVP.</p>
    <p><b>Kontekst.</b> ZKSWD należy do rodziny systemów SOiA — obok ALARM.soia (warstwa publiczna) i SYRENY.soia (uruchamianie syren). Jest systemem służbowym: odbiorcami są centra zarządzania kryzysowego, stanowiska kierowania PSP i RCB.</p>""",
}

# =============================================================== CivCom

CIVCOM_SECTIONS = """  <section class="critical">
    <div class="hd">
      <span class="tag">Warunek wydania</span>
      <h3 style="flex:1 1 320px">Aplikacja na komputer wymaga podpisów, zanim trafi do użytkowników</h3>
    </div>
    <p class="lead" style="max-width:80ch">Sam komunikator działa w przeglądarce i nie zależy od niczyich zgód. Inaczej jest z <b>aplikacją na komputer</b>: Windows i macOS blokują uruchomienie programu, który nie ma podpisu producenta. Bez certyfikatu Authenticode użytkownik zobaczy ostrzeżenie SmartScreen, bez Developer ID i notaryzacji Apple — macOS w ogóle nie pozwoli jej otworzyć. To ten sam typ przeszkody co konto Apple w harmonogramie ALARM.soia i <b>trzeba go domknąć przed decyzją go / no-go 1 września</b>.</p>
    <div class="chain">
      <div class="step first"><span class="sn">Warunek</span><span class="st">Certyfikat Authenticode (Windows)</span><span class="sd">przed 01.09</span></div>
      <div class="step first"><span class="sn">Warunek</span><span class="st">Developer ID (Apple)</span><span class="sd">przed 01.09</span></div>
      <div class="step"><span class="sn">Krok</span><span class="st">Podpisanie i notaryzacja pakietów</span><span class="sd">ok. 1 tyg.</span></div>
      <div class="step"><span class="sn">Krok</span><span class="st">Wydanie publiczne i strona pobierania</span><span class="sd">ok. 1 tyg.</span></div>
      <div class="step last"><span class="sn">Efekt</span><span class="st">Instalacja bez ostrzeżeń systemowych</span><span class="sd">14.09</span></div>
    </div>
  </section>

  <section class="panel">
    <h2>Co może przesunąć termin</h2>
    <div class="tablewrap">
      <table>
        <thead><tr><th style="width:34%">Ryzyko</th><th style="width:12%">Waga</th><th style="width:27%">Skutek, jeśli się zmaterializuje</th><th style="width:27%">Co je zdejmuje</th></tr></thead>
        <tbody>
          <tr><td><b>Brak podpisu Windows i notaryzacji Apple</b> dla aplikacji na komputer</td><td class="sev"><span class="pill hi">Krytyczne</span></td><td>Aplikacja na komputer nie może zostać wydana publicznie; zostaje wersja w przeglądarce.</td><td>Uzyskanie certyfikatu Authenticode i Developer ID przed 01.09.</td></tr>
          <tr><td><b>Dwa tygodnie</b> między decyzją go / no-go a zakończeniem etapu</td><td class="sev"><span class="pill hi">Wysokie</span></td><td>Uwagi z odbioru nie zdążą zostać wdrożone przed 14.09.</td><td>Testy akceptacyjne przed decyzją, nie po niej (24.08 – 06.09).</td></tr>
          <tr><td><b>Logowanie kontem służbowym</b> — zależność od AD i usługi tożsamości</td><td class="sev"><span class="pill md">Średnie</span></td><td>Użytkownicy nie zalogują się kontem służbowym, potrzebne konta lokalne.</td><td>Uzgodniona ścieżka OIDC i środowisko zapasowe po stronie infrastruktury.</td></tr>
          <tr><td><b>Adopcja</b> — konkurencja z komunikatorami prywatnymi</td><td class="sev"><span class="pill md">Średnie</span></td><td>Komunikacja służbowa dalej odbywa się w aplikacjach prywatnych.</td><td>Ambasadorzy w jednostkach, gotowe pokoje startowe, prostota obsługi.</td></tr>
          <tr><td><b>Rozszerzenie na komendy wojewódzkie i powiatowe</b></td><td class="sev"><span class="pill lo">Niskie</span></td><td>Poza zakresem tego etapu — nie wpływa na termin 14.09.</td><td>Ujęte jako osobny etap po zamknięciu bieżącego.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

"""

CIVCOM = {
    "slug": "civcom",
    "title": "Harmonogram CivCom — KG PSP",
    "ogtitle": "Harmonogram CivCom",
    "desc": "Harmonogram CivCom — komunikatora zarządzania kryzysowego i ochrony ludności (civcom.soia.info). Od rozpoznania w marcu 2026 do zakończenia etapu 14.09.2026.",
    "favicon": "💬",
    "eyebrow": "SOiA · Biuro Informatyki i Łączności KG PSP",
    "h1": "Harmonogram<br>CivCom",
    "lead": "<b>CivCom</b> (<code>civcom.soia.info</code>) — służbowy komunikator zarządzania kryzysowego i ochrony ludności: szyfrowana komunikacja, logowanie kontem służbowym, katalog osób i gotowe pokoje robocze. Zastępuje komunikatory prywatne używane nieformalnie do spraw służbowych. Linia czasu obejmuje etap od rozpoznania technologii w marcu 2026 do zamknięcia etapu 14 września 2026.",
    "facts": [
        {"k": "Dziś", "v": "20.08.2026", "n": "4 tygodnie do końca", "auto_date": True, "auto_left": True},
        {"k": "Data ostateczna", "v": "14.09.2026", "n": "zakończenie etapu", "critical": True},
        {"k": "Start", "v": "marzec 2026", "n": "rozpoznanie i wybór technologii"},
        {"k": "Aplikacja na komputer", "v": "czeka na podpisy", "n": "Authenticode i notaryzacja Apple", "critical": True},
    ],
    "aside": "",
    "chart_title": "Linia czasu etapu",
    "chart_note": "Marzec – wrzesień 2026 · podział tygodniowy, opisane co drugi tydzień · przewiń w bok",
    "start": "2026-03-02", "weeks": 29, "deadline": "2026-09-14", "minw": 1100,
    "label_every": 2,
    "months": [("Marzec", 4), ("Kwiecień", 5), ("Maj", 4), ("Czerwiec", 4), ("Lipiec", 5), ("Sierpień", 4), ("Wrzesień", 3)],
    "legend_blocker": True,
    "milestones": [
        {"date": "2026-05-06", "label": "Analiza wdrożeniowa v1.0<br>i decyzje architektoniczne", "raise": True},
        {"date": "2026-06-05", "label": "Logowanie kontem służbowym"},
        {"date": "2026-07-20", "label": "Mapowanie grup AD"},
        {"date": "2026-09-01", "label": "Decyzja go / no-go", "critical": True, "raise": True, "edge_r": True},
        {"date": "2026-09-14", "label": "Zakończenie etapu", "final": True},
    ],
    "lanes": [
        {"name": "Analiza i decyzje", "color": "dep", "meta": "wybór technologii i przesądzenia, których później się nie zmienia", "rows": [
            {"name": "Rozpoznanie i wybór technologii (Matrix / Synapse / Element)", "dates": "2.03 – 3.05", "s": 1, "e": 10},
            {"name": "Analiza wdrożeniowa v1.0 i decyzje architektoniczne", "dates": "4.05 – 24.05 · domena, tożsamość, model kont", "s": 10, "e": 13, "key": True},
        ]},
        {"name": "Platforma CivCom", "color": "portal", "meta": "serwer, tożsamość, katalog — civcom.soia.info", "rows": [
            {"name": "Serwer komunikacji i domena civcom.soia.info", "dates": "25.05 – 5.07", "s": 13, "e": 19},
            {"name": "Logowanie kontem służbowym (SSO / AD)", "dates": "1.06 – 20.07", "s": 14, "e": 22, "key": True},
            {"name": "Katalog osób, pokoje startowe, mapowanie grup AD", "dates": "29.06 – 6.08", "s": 18, "e": 24},
            {"name": "Panel administracyjny i synchronizacja grup", "dates": "20.07 – 6.08", "s": 21, "e": 24},
        ]},
        {"name": "Klienty użytkownika", "color": "api", "meta": "przeglądarka oraz aplikacja na komputer (Windows, macOS, Linux)", "rows": [
            {"name": "Prekonfigurowany klient w przeglądarce", "dates": "1.06 – 20.07", "s": 14, "e": 22},
            {"name": "Aplikacja na komputer — budowa i testy", "dates": "3.08 – 7.09", "s": 23, "e": 29},
            {"name": "⚠ Podpis Windows i notaryzacja Apple", "dates": "warunek wydania publicznego · potrzebne przed 1.09", "s": 25, "e": 30, "blocked": True},
        ]},
        {"name": "Wdrożenie i szkolenia", "color": "and", "meta": "od pilotażu do gotowości organizacyjnej", "rows": [
            {"name": "Pilotaż z grupą użytkowników", "dates": "6.07 – 30.08", "s": 19, "e": 27},
            {"name": "Szkolenia ambasadorów i procedury offboardingu", "dates": "3.08 – 23.08", "s": 23, "e": 26},
            {"name": "Dokumentacja i baza wiedzy", "dates": "20.07 – 14.09 · WIEDZA.soia", "s": 21, "e": 30},
        ]},
        {"name": "Odbiór", "color": "qa", "meta": "warunki wejścia do eksploatacji", "rows": [
            {"name": "Testy akceptacyjne i bezpieczeństwa", "dates": "24.08 – 6.09", "s": 26, "e": 28},
            {"name": "Decyzja go / no-go produkcja", "dates": "1.09", "s": 27, "e": 28, "key": True},
            {"name": "Zamknięcie etapu i przekazanie do eksploatacji", "dates": "7.09 – 20.09", "s": 28, "e": 30, "key": True},
        ]},
    ],
    "sections": CIVCOM_SECTIONS,
    "footnotes": """    <p><b>Założenia planu.</b> Daty kamieni milowych od maja 2026 pochodzą z karty projektu prowadzonej w KG PSP; okres marzec – kwiecień 2026 obejmuje rozpoznanie poprzedzające formalne otwarcie projektu. Strona pokazuje <b>planowany przebieg etapu</b> — bieżący stan realizacji poszczególnych kamieni milowych prowadzony jest w karcie projektu, nie tutaj.</p>
    <p><b>Kontekst.</b> CivCom jest komunikatorem służbowym rodziny SOiA. Aplikacja na komputer jest cienkim klientem strony <code>civcom.soia.info</code> i jest rozwijana jako otwarte oprogramowanie na licencji EUPL-1.2.</p>""",
}

PAGES = [ALARM, ZKSWD, CIVCOM]

# =============================================================== strona główna

HUB = """<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Harmonogramy BIŁ KG PSP</title>
<meta name="description" content="Harmonogramy realizacji projektów prowadzonych przez Biuro Informatyki i Łączności Komendy Głównej Państwowej Straży Pożarnej.">
<meta name="author" content="Biuro Informatyki i Łączności KG PSP">
<meta property="og:type" content="website">
<meta property="og:title" content="Harmonogramy BIŁ KG PSP">
<meta property="og:description" content="Harmonogramy realizacji projektów Biura Informatyki i Łączności KG PSP.">
<meta property="og:url" content="https://kgpsp.github.io/harmonogramy/">
<meta property="og:locale" content="pl_PL">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🗓️</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<link rel="stylesheet" href="assets/harmonogram.css">
<style>
  .wrap{max-width:920px}
  .list{display:flex;flex-direction:column;gap:14px}
  .card{
    text-decoration:none;color:inherit;
    background:var(--surface);border:1px solid var(--rule);border-left:5px solid var(--c);
    border-radius:4px;box-shadow:var(--shadow);padding:22px 24px;
    display:grid;grid-template-columns:1fr auto;gap:6px 20px;align-items:start;
    transition:border-color .15s ease, transform .15s ease;
  }
  .card:hover,.card:focus-visible{border-color:var(--rule-strong);transform:translateY(-1px)}
  .card:focus-visible{outline:2px solid var(--c);outline-offset:3px}
  .card .n{font-family:"Barlow Condensed",sans-serif;font-size:29px;font-weight:700;line-height:1;text-transform:uppercase;letter-spacing:.02em}
  .card .d{grid-column:1;color:var(--ink-2);font-size:14.5px;max-width:60ch}
  .card .meta{grid-column:1;display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}
  .card .go{grid-row:1;grid-column:2;font-family:"IBM Plex Mono",monospace;font-size:12px;font-weight:600;color:var(--c);white-space:nowrap;padding-top:5px}
  .tag{display:inline-flex;align-items:baseline;gap:6px;border:1px solid var(--rule);border-radius:999px;background:var(--surface-2);padding:3px 11px;font-size:12px;color:var(--ink-2)}
  .tag b{font-family:"IBM Plex Mono",monospace;font-size:11.5px;font-weight:600;font-variant-numeric:tabular-nums}
  .tag.term b{color:var(--alarm)}
  .tag.live b{color:var(--ok)}
  .soon{border:1px dashed var(--rule-strong);border-radius:4px;padding:18px 22px;color:var(--muted);font-size:14px}
  @media (max-width:560px){
    .card{grid-template-columns:1fr}
    .card .go{grid-row:auto;grid-column:1;padding-top:2px}
  }
</style>
</head>
<body>
<div class="wrap">

  <header style="gap:12px">
    <p class="eyebrow">Komenda Główna PSP · Biuro Informatyki i Łączności</p>
    <h1>Harmonogramy</h1>
    <div class="title-rule"></div>
    <p class="lead">Harmonogramy realizacji projektów prowadzonych przez BIŁ KG PSP. Każdy harmonogram to jedna strona: fazy prac, testy, kamienie milowe i termin — w formie czytelnej bez znajomości szczegółów technicznych. Linia „dziś” na każdym wykresie ustawia się sama.</p>
  </header>

  <section class="list">
    <h2>Aktualne</h2>

    <a class="card" href="alarm-soia/" style="--c:var(--lane-portal)">
      <span class="n">ALARM.soia</span>
      <span class="go">Otwórz →</span>
      <span class="d">Publiczna warstwa ostrzegania: portal ALARM.soia wraz z otwartym feedem alertów oraz aplikacje mobilne na Android i iOS.</span>
      <span class="meta">
        <span class="tag live"><b>●</b> w realizacji</span>
        <span class="tag term">termin <b>30.11.2026</b></span>
        <span class="tag">portal + aplikacje mobilne</span>
      </span>
    </a>

    <a class="card" href="zkswd/" style="--c:var(--lane-api)">
      <span class="n">ZKSWD</span>
      <span class="go">Otwórz →</span>
      <span class="d">System wspomagania decyzji dla zarządzania kryzysowego. Działa produkcyjnie od 21.08.2026; nowe funkcje co tydzień, pełny zasięg krajowy w grudniu.</span>
      <span class="meta">
        <span class="tag live"><b>●</b> na produkcji</span>
        <span class="tag term">termin <b>18.12.2026</b></span>
        <span class="tag">wydania co tydzień</span>
      </span>
    </a>

    <a class="card" href="civcom/" style="--c:var(--lane-and)">
      <span class="n">CivCom</span>
      <span class="go">Otwórz →</span>
      <span class="d">Służbowy komunikator zarządzania kryzysowego i ochrony ludności (civcom.soia.info) — szyfrowana komunikacja, logowanie kontem służbowym, aplikacja na komputer.</span>
      <span class="meta">
        <span class="tag live"><b>●</b> w odbiorze</span>
        <span class="tag term">termin <b>14.09.2026</b></span>
        <span class="tag">komunikator ZK i OL</span>
      </span>
    </a>

    <p class="soon">Kolejne harmonogramy będą dodawane w tym miejscu.</p>
  </section>

  <section class="orgs">
    <h2>Współdziałanie</h2>
    <div class="plate">
      <img class="l-psp" src="assets/logo/psp.svg" alt="Państwowa Straż Pożarna" width="45" height="58" loading="lazy">
      <img class="l-mswia" src="assets/logo/mswia.svg" alt="Ministerstwo Spraw Wewnętrznych i Administracji" width="143" height="28" loading="lazy">
      <img class="l-rcb" src="assets/logo/rcb.svg" alt="Rządowe Centrum Bezpieczeństwa" width="82" height="46" loading="lazy">
      <img class="l-olioc" src="assets/logo/olioc.svg" alt="Ochrona Ludności i Obrona Cywilna" width="100" height="34" loading="lazy">
    </div>
    <p class="names">Państwowa Straż Pożarna · Ministerstwo Spraw Wewnętrznych i Administracji · Rządowe Centrum Bezpieczeństwa · Ochrona Ludności i Obrona Cywilna</p>
  </section>

  <footer>
    <p>Harmonogramy mają charakter planistyczny — daty zależne od podmiotów zewnętrznych (m.in. weryfikacja w sklepach z aplikacjami, wydanie certyfikatów) są szacunkowe.</p>
    <p>Opracowanie: Biuro Informatyki i Łączności KG PSP · <span data-updated>stan na {built}</span> · <a href="https://github.com/KGPSP/harmonogramy">źródło strony</a></p>
  </footer>

</div>
<script src="assets/timeline.js"></script>
</body>
</html>
"""
