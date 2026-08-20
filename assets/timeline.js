/* Harmonogramy BIŁ KG PSP — automatyczne pozycjonowanie linii „dziś”.
 *
 * Wykres deklaruje trzy atrybuty:
 *   data-t-start    poniedziałek pierwszej kolumny  (RRRR-MM-DD)
 *   data-t-weeks    liczba kolumn tygodniowych
 *   data-t-deadline data ostateczna harmonogramu    (RRRR-MM-DD)
 *   data-t-left-suffix  podpis odliczania, domyślnie "do końca"
 *
 * Skrypt ustawia pozycję linii, jej etykietę, dzisiejszą datę w kaflu
 * oraz pozostały czas do terminu. Dzięki temu strona nie starzeje się
 * między kolejnymi wypchnięciami do repozytorium.
 */
(function () {
  "use strict";

  var DAY = 86400000;

  function pad(n) { return n < 10 ? "0" + n : "" + n; }
  function dm(date) { return pad(date.getDate()) + "." + pad(date.getMonth() + 1); }
  function dmy(date) { return dm(date) + "." + date.getFullYear(); }

  function parseDate(iso) {
    var p = iso.split("-");
    return new Date(+p[0], +p[1] - 1, +p[2]);
  }

  /* polska odmiana: 1 tydzień, 2–4 tygodnie, 5+ tygodni */
  function weeksPl(n) {
    if (n === 1) return "1 tydzień";
    var last = n % 10, two = n % 100;
    if (last >= 2 && last <= 4 && (two < 12 || two > 14)) return n + " tygodnie";
    return n + " tygodni";
  }
  function daysPl(n) { return n === 1 ? "1 dzień" : n + " dni"; }

  function timeLeft(today, deadline, suffix) {
    var days = Math.round((deadline - today) / DAY);
    if (days < 0) return "termin minął " + daysPl(-days) + " temu";
    if (days === 0) return "termin dzisiaj";
    if (days <= 21) return daysPl(days) + " " + suffix;
    return weeksPl(Math.round(days / 7)) + " " + suffix;
  }

  function run() {
    var chart = document.querySelector("[data-t-start]");
    var now = new Date();
    var today = new Date(now.getFullYear(), now.getMonth(), now.getDate());

    document.querySelectorAll("[data-today-date]").forEach(function (el) {
      el.textContent = dmy(today);
    });
    document.querySelectorAll("[data-updated]").forEach(function (el) {
      el.textContent = "stan na " + dmy(today);
    });

    if (!chart) return;

    var start = parseDate(chart.getAttribute("data-t-start"));
    var weeks = parseInt(chart.getAttribute("data-t-weeks"), 10);
    var deadlineAttr = chart.getAttribute("data-t-deadline");
    var span = weeks * 7;
    var dayIdx = Math.round((today - start) / DAY);

    var line = chart.querySelector("[data-today-line]");
    if (line) {
      if (dayIdx >= 0 && dayIdx < span) {
        line.style.left = ((dayIdx + 0.5) / span * 100).toFixed(3) + "%";
        line.setAttribute("data-label", dm(today));
        line.hidden = false;
      } else {
        line.hidden = true;
      }
    }

    if (deadlineAttr) {
      var suffix = chart.getAttribute("data-t-left-suffix") || "do końca";
      var left = timeLeft(today, parseDate(deadlineAttr), suffix);
      document.querySelectorAll("[data-time-left]").forEach(function (el) {
        el.textContent = left;
      });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run);
  } else {
    run();
  }
})();
