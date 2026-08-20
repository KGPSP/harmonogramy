#!/usr/bin/env python3
"""Generator stron harmonogramów.

Strony w repozytorium są zwykłym HTML i można je edytować ręcznie.
Ten skrypt pozwala zmieniać *dane* (belki, kamienie milowe) zamiast znaczników
i gwarantuje, że matematyka kolumn jest identyczna na każdej stronie.

    python3 _tools/build.py          # regeneruje alarm-soia/, zkswd/, civcom/, index.html

Model siatki: jedna kolumna = jeden tydzień (poniedziałek–niedziela).
Pozycja daty na osi = (dni_od_startu + 0.5) / (tygodnie * 7).
"""

import datetime as dt
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PL_MONTHS = ["stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca",
             "lipca", "sierpnia", "września", "października", "listopada", "grudnia"]


def d(s):
    return dt.date.fromisoformat(s)


def dm(s):
    """2026-08-31 -> 31.08"""
    x = d(s)
    return f"{x.day}.{x.month:02d}"


def dmy(s):
    x = d(s)
    return f"{x.day:02d}.{x.month:02d}.{x.year}"


def pos(start, weeks, date):
    """Pozycja daty na osi w procentach szerokości toru."""
    return ((d(date) - d(start)).days + 0.5) / (weeks * 7) * 100


# ---------------------------------------------------------------- render helpers

def render_months(months):
    out = ['          <div style="grid-column:1"></div>']
    col = 2
    for name, count in months:
        out.append(f'          <div class="m" style="grid-column:{col}/{col + count}">{name}</div>')
        col += count
    return "\n".join(out)


def render_weeks(start, weeks, every=1):
    out = ["          <div></div>"]
    for k in range(weeks):
        day = d(start) + dt.timedelta(days=7 * k)
        label = f"{day.day}.{day.month:02d}" if k % every == 0 else "&nbsp;"
        out.append(f'          <div class="w">{label}</div>')
    return "\n".join(out)


def render_gridlines(weeks, months):
    bounds, acc = set(), 0
    for _, count in months[:-1]:
        acc += count
        bounds.add(acc)
    out = ['            <div class="gl strong" style="left:0%"></div>']
    for k in range(1, weeks):
        p = k / weeks * 100
        cls = "gl strong" if k in bounds else "gl"
        out.append(f'            <div class="{cls}" style="left:{p:.3f}%"></div>')
    return "\n".join(out)


def render_milestones(start, weeks, milestones):
    out = ['            <div class="rail-line"></div>']
    for ms in milestones:
        cls = "ms"
        if ms.get("raise"):
            cls += " raise"
        if ms.get("critical"):
            cls += " is-critical"
        if ms.get("final"):
            cls += " is-final edge-r"
        if ms.get("edge_l"):
            cls += " edge-l"
        if ms.get("edge_r"):
            cls += " edge-r"
        p = pos(start, weeks, ms["date"])
        out.append(f'            <div class="{cls}" style="left:{p:.2f}%">')
        out.append(f'              <span class="lbl"><span class="d">{dm(ms["date"])}</span>{ms["label"]}</span>')
        out.append('              <span class="dot"></span>')
        out.append("            </div>")
    return "\n".join(out)


def render_releases(start, weeks, first, count, step_days=7):
    """Rytm wydań — znacznik co tydzień (dla harmonogramu iteracyjnego)."""
    out = ['            <div class="rel-line"></div>']
    for k in range(count):
        day = d(first) + dt.timedelta(days=step_days * k)
        p = pos(start, weeks, day.isoformat())
        label = "MVP" if k == 0 else f"{k}"
        cls = "rel is-mvp" if k == 0 else "rel"
        title = f"{'MVP produkcyjny' if k == 0 else f'Iteracja {k}'} — {dmy(day.isoformat())}"
        out.append(f'            <span class="{cls}" style="left:{p:.2f}%" title="{title}">'
                   f'<span class="rel-n">{label}</span><span class="rel-tick"></span></span>')
    return "\n".join(out)


def render_lanes(lanes):
    out = []
    for lane in lanes:
        out.append(f'          <div class="lane" style="--c:var(--lane-{lane["color"]})">')
        out.append('            <div class="lane-title"><span class="t"><span class="swatch"></span>'
                   f'{lane["name"]}</span><span class="meta">{lane["meta"]}</span></div>')
        for r in lane["rows"]:
            rowcls = "row is-blocked" if r.get("blocked") else "row"
            barcls = "bar"
            if r.get("blocked"):
                barcls += " blocker"
            elif r.get("key"):
                barcls += " solid"
            dates = f'<span class="dates">{r["dates"]}</span>' if r.get("dates") else ""
            out.append(f'            <div class="{rowcls}"><span class="name">{r["name"]}{dates}</span>'
                       f'<span class="{barcls}" style="--s:{r["s"] + 1};--e:{r["e"] + 1}"></span></div>')
        out.append("          </div>")
    return "\n".join(out)


def render_facts(facts):
    out = []
    for f in facts:
        cls = "fact is-critical" if f.get("critical") else "fact"
        v = f'<span class="v"{" data-today-date" if f.get("auto_date") else ""}>{f["v"]}</span>'
        n = f'<span class="n"{" data-time-left" if f.get("auto_left") else ""}>{f["n"]}</span>'
        out.append(f'      <div class="{cls}"><span class="k">{f["k"]}</span>{v}{n}</div>')
    return "\n".join(out)


def render_risks(rows):
    out = []
    for r in rows:
        out.append("          <tr>")
        out.append(f'            <td>{r["risk"]}</td>')
        out.append(f'            <td class="sev"><span class="pill {r["lvl"]}">{r["lvl_txt"]}</span></td>')
        out.append(f'            <td>{r["effect"]}</td>')
        out.append(f'            <td>{r["fix"]}</td>')
        out.append("          </tr>")
    return "\n".join(out)


# ---------------------------------------------------------------- page template

PAGE = """<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Biuro Informatyki i Łączności KG PSP">
<meta property="og:type" content="article">
<meta property="og:title" content="{ogtitle}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://kgpsp.github.io/harmonogramy/{slug}/">
<meta property="og:locale" content="pl_PL">
{ogimage}<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>{favicon}</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<link rel="stylesheet" href="../assets/harmonogram.css">
</head>
<body>
<div class="wrap">

  <header>
    <p class="eyebrow"><a class="back" href="../">← Harmonogramy</a> · {eyebrow}</p>
    <h1>{h1}</h1>
    <div class="title-rule"></div>
    <p class="lead">{lead}</p>

    <div class="facts">
{facts}
    </div>
{aside}  </header>

  <section class="chart-card">
    <div class="chart-head">
      <h2>{chart_title}</h2>
      <p class="chart-note">{chart_note}</p>
    </div>

    <div class="scroll">
      <div class="chart" style="--weeks:{weeks};min-width:{minw}px" data-t-start="{start}" data-t-weeks="{weeks}" data-t-deadline="{deadline}">

        <div class="months">
{months}
        </div>

        <div class="weeks">
{weeklabels}
        </div>
{releases}
        <div class="rail">
          <div class="rail-track">
{milestones}
          </div>
        </div>

        <div class="lanes">
          <div class="grid-bg" aria-hidden="true">
{gridlines}
            <div class="today" data-today-line hidden></div>
          </div>

{lanes}
        </div>
      </div>
    </div>

    <div class="legend">
      <span><i class="plain"></i> prace bieżące</span>
      <span><i class="solidx"></i> etap krytyczny dla terminu</span>
{legend_extra}      <span><i class="diamond"></i> kamień milowy</span>
      <span class="lg-today">▌ linia „dziś”</span>
    </div>
  </section>

{sections}  <section class="orgs">
    <h2>Współdziałanie</h2>
    <div class="plate">
      <img class="l-psp" src="../assets/logo/psp.svg" alt="Państwowa Straż Pożarna" width="45" height="58" loading="lazy">
      <img class="l-mswia" src="../assets/logo/mswia.svg" alt="Ministerstwo Spraw Wewnętrznych i Administracji" width="143" height="28" loading="lazy">
      <img class="l-rcb" src="../assets/logo/rcb.svg" alt="Rządowe Centrum Bezpieczeństwa" width="82" height="46" loading="lazy">
      <img class="l-olioc" src="../assets/logo/olioc.svg" alt="Ochrona Ludności i Obrona Cywilna" width="100" height="34" loading="lazy">
    </div>
    <p class="names">Państwowa Straż Pożarna · Ministerstwo Spraw Wewnętrznych i Administracji · Rządowe Centrum Bezpieczeństwa · Ochrona Ludności i Obrona Cywilna</p>
  </section>

  <footer>
{footnotes}
    <p>Opracowanie: Biuro Informatyki i Łączności KG PSP · <span data-updated>stan na {built}</span></p>
  </footer>

</div>
<script src="../assets/timeline.js"></script>
</body>
</html>
"""


def build_page(p):
    releases = ""
    if p.get("releases"):
        r = p["releases"]
        releases = ('        <div class="rel-rail">\n'
                    + render_releases(p["start"], p["weeks"], r["first"], r["count"]) + "\n"
                    + '        </div>\n')
    ogimage = ""
    if p.get("ogimage"):
        ogimage = f'<meta property="og:image" content="https://kgpsp.github.io/harmonogramy/{p["ogimage"]}">\n'
    legend_extra = ""
    if p.get("legend_blocker"):
        legend_extra = '      <span><i class="hatch"></i> zablokowane — czeka na decyzję poza zespołem</span>\n'
    if p.get("legend_release"):
        legend_extra += '      <span><i class="tick"></i> cotygodniowe wydanie</span>\n'

    out = PAGE.format(
        title=p["title"], desc=p["desc"], ogtitle=p["ogtitle"], slug=p["slug"],
        ogimage=ogimage, favicon=p["favicon"], eyebrow=p["eyebrow"], h1=p["h1"],
        lead=p["lead"], facts=render_facts(p["facts"]), aside=p.get("aside", ""),
        chart_title=p["chart_title"], chart_note=p["chart_note"],
        weeks=p["weeks"], minw=p["minw"], start=p["start"], deadline=p["deadline"],
        months=render_months(p["months"]),
        weeklabels=render_weeks(p["start"], p["weeks"], p.get("label_every", 1)),
        releases=releases,
        milestones=render_milestones(p["start"], p["weeks"], p["milestones"]),
        gridlines=render_gridlines(p["weeks"], p["months"]),
        lanes=render_lanes(p["lanes"]),
        legend_extra=legend_extra,
        sections=p.get("sections", ""),
        footnotes=p["footnotes"],
        built=dmy(BUILT),
    )
    path = ROOT / p["slug"] / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(out, encoding="utf-8")
    return path


BUILT = "2026-08-20"

from pages import PAGES, HUB  # noqa: E402

if __name__ == "__main__":
    for page in PAGES:
        print("zapisano:", build_page(page).relative_to(ROOT))
    (ROOT / "index.html").write_text(HUB.replace("{built}", dmy(BUILT)), encoding="utf-8")
    print("zapisano: index.html")
