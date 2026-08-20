#!/usr/bin/env python3
"""Wersja artefaktowa strony harmonogramu (claude.ai).

Artefakt musi być samowystarczalny — polityka bezpieczeństwa strony blokuje
zasoby z zewnętrznych hostów poza Google Fonts. Skrypt bierze gotową stronę
z repozytorium i wbudowuje w nią arkusz stylów, skrypt oraz logotypy
(jako data: URI), a także usuwa szkielet dokumentu, który środowisko
artefaktu dokleja samo.

    python3 _tools/build_artifact.py alarm-soia /sciezka/do/pliku.html

Dzięki temu artefakt i strona publiczna pochodzą z jednego źródła.
"""

import base64
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
HUB_URL = "https://kgpsp.github.io/harmonogramy/"


def data_uri(path):
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/svg+xml;base64,{b64}"


def build(slug, out_path):
    src = (ROOT / slug / "index.html").read_text(encoding="utf-8")

    # tytuł zachowujemy — jest nazwą artefaktu i nie może się zmieniać
    title = re.search(r"<title>(.*?)</title>", src).group(1)
    title = title.split(" — ")[0]

    body = src.split("<body>", 1)[1].rsplit("</body>", 1)[0]

    # arkusz stylów i skrypt — wbudowane w treść
    css = (ROOT / "assets/harmonogram.css").read_text(encoding="utf-8")
    js = (ROOT / "assets/timeline.js").read_text(encoding="utf-8")
    body = body.replace('<script src="../assets/timeline.js"></script>',
                        f"<script>\n{js}\n</script>")

    # logotypy — data: URI, każdy w osobnym dokumencie (bez kolizji identyfikatorów)
    for name in ("psp", "mswia", "rcb", "olioc"):
        body = body.replace(f'src="../assets/logo/{name}.svg"',
                            f'src="{data_uri(ROOT / "assets/logo" / f"{name}.svg")}"')

    # powrót do strony głównej prowadzi na stronę publiczną, nie do katalogu wyżej
    body = body.replace('<a class="back" href="../">← Harmonogramy</a>',
                        f'<a class="back" href="{HUB_URL}">Harmonogramy KG PSP ↗</a>')

    fonts = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
             '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
             '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
             "family=Barlow+Condensed:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600"
             '&family=IBM+Plex+Mono:wght@400;500;600&display=swap">')

    out = f"<title>{title}</title>\n{fonts}\n\n<style>\n{css}\n</style>\n{body}"
    pathlib.Path(out_path).write_text(out, encoding="utf-8")
    return out_path, len(out)


if __name__ == "__main__":
    slug = sys.argv[1] if len(sys.argv) > 1 else "alarm-soia"
    out = sys.argv[2] if len(sys.argv) > 2 else f"{slug}-artefakt.html"
    path, size = build(slug, out)
    print(f"zapisano: {path} ({size / 1024:.0f} KB)")
