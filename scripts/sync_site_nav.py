#!/usr/bin/env python3
"""Keep the site's header/navbar identical on every page.

The site pages under ``swiss-law-as-source`` are hand-maintained HTML, and each
one used to carry its own ``<nav>`` markup plus its own ``header``/``nav`` CSS.
They drifted: api.html listed three links, crossrefs.html listed "Dashboard"
twice, diff.html had no navbar at all, and data.html rendered a left-aligned
header while every other page centred it.

This script is the single source of truth for the chrome:

* ``NAV_ITEMS`` is the canonical link list — every navbar-bearing page shows all
  of it, with the current page marked ``aria-current="page"``.
* the shared look lives in ``assets/site-chrome.css``; page-local ``header``/
  ``nav`` rules are stripped so the shared file always wins.

Usage::

    python scripts/sync_site_nav.py            # rewrite the site pages
    python scripts/sync_site_nav.py --check    # exit 1 if anything drifted
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

SITE_DIR = Path(os.environ.get("SWISS_LAW_SITE_REPO", "/home/ubuntu/swiss-law-as-source"))

CHROME_CSS = "assets/site-chrome.css"
CHROME_LINK = f'    <link rel="stylesheet" href="{CHROME_CSS}">'

# The canonical navbar — five entries, in the site's information hierarchy.
# Nothing else belongs here: a navbar that grows per page is what drifted before.
NAV_ITEMS: list[tuple[str, str]] = [
    ("index.html", "Dashboard"),
    ("laws.html", "Laws"),
    ("data.html", "Data"),
    ("verification.html", "Verification"),
    ("api.html", "API"),
]

# Secondary pages: they carry the same chrome and the same five-item navbar, but
# they are reached from the footer tools row rather than from the navbar itself.
TOOL_ITEMS: list[tuple[str, str]] = [
    ("crossrefs.html", "Federal cross-refs"),
    ("cross_level_refs.html", "Federal ↔ cantonal"),
    ("diff.html", "Diff viewer"),
    ("undated.html", "Undated laws"),
]

# Pages that carry the chrome.  embed.html is an iframe target and
# stats.html / swagger.html are redirect stubs — all three stay bare.
PAGES = [href for href, _ in NAV_ITEMS] + [href for href, _ in TOOL_ITEMS]

# Page-local rules that must give way to the shared stylesheet.
CHROME_SELECTORS = [
    "header",
    "header h1",
    "header p",
    "header a",
    "nav",
    "nav a",
    "nav a:hover",
    "nav a strong",
]


def render_nav(current: str) -> str:
    """The canonical <nav> block, with `current` marked as the active page.

    On a secondary page nothing is marked — the page is not in the navbar.
    """
    lines = ["    <nav>"]
    for href, label in NAV_ITEMS:
        mark = ' aria-current="page"' if href == current else ""
        lines.append(f'        <a href="{href}"{mark}>{label}</a>')
    lines.append("    </nav>")
    return "\n".join(lines)


def render_tools(current: str) -> str:
    """The footer row that keeps the off-navbar pages one click away."""
    lines = ['        <p class="site-tools">More tools:']
    for i, (href, label) in enumerate(TOOL_ITEMS):
        mark = ' aria-current="page"' if href == current else ""
        sep = "" if i == len(TOOL_ITEMS) - 1 else " &middot;"
        lines.append(f'            <a href="{href}"{mark}>{label}</a>{sep}')
    lines.append("        </p>")
    return "\n".join(lines)


def strip_chrome_css(html: str) -> str:
    """Drop page-local header/nav rules so assets/site-chrome.css governs."""
    for selector in CHROME_SELECTORS:
        pattern = re.compile(
            r"^[ \t]*" + re.escape(selector) + r"[ \t]*\{[^{}]*\}[ \t]*\n",
            re.MULTILINE,
        )
        html = pattern.sub("", html)
    return html


def ensure_chrome_link(html: str) -> str:
    """Link the shared stylesheet last in <head> so it wins on ties."""
    if CHROME_CSS in html:
        return html
    return html.replace("</head>", f"{CHROME_LINK}\n</head>", 1)


NAV_RE = re.compile(r"^[ \t]*<nav>.*?</nav>[ \t]*$", re.DOTALL | re.MULTILINE)
HEADER_END_RE = re.compile(r"^([ \t]*</header>[ \t]*)$", re.MULTILINE)
TOOLS_RE = re.compile(r'^[ \t]*<p class="site-tools">.*?</p>[ \t]*$', re.DOTALL | re.MULTILINE)
FOOTER_END_RE = re.compile(r"^([ \t]*</footer>[ \t]*)$", re.MULTILINE)
BODY_END_RE = re.compile(r"^([ \t]*</body>[ \t]*)$", re.MULTILINE)


def sync_page(path: Path) -> str:
    """Return `path`'s content with canonical chrome applied."""
    html = path.read_text(encoding="utf-8")
    nav = render_nav(path.name)

    if NAV_RE.search(html):
        html = NAV_RE.sub(lambda _: nav, html, count=1)
    elif HEADER_END_RE.search(html):
        html = HEADER_END_RE.sub(lambda m: f"{m.group(1)}\n{nav}", html, count=1)
    else:
        raise SystemExit(f"{path.name}: no <nav> and no </header> to anchor the navbar")

    tools = render_tools(path.name)
    if TOOLS_RE.search(html):
        html = TOOLS_RE.sub(lambda _: tools, html, count=1)
    elif FOOTER_END_RE.search(html):
        html = FOOTER_END_RE.sub(lambda m: f"{tools}\n{m.group(1)}", html, count=1)
    elif BODY_END_RE.search(html):
        footer = f'    <footer class="site-footer">\n{tools}\n    </footer>'
        html = BODY_END_RE.sub(lambda m: f"{footer}\n{m.group(1)}", html, count=1)
    else:
        raise SystemExit(f"{path.name}: no footer and no </body> to anchor the tools row")

    html = strip_chrome_css(html)
    return ensure_chrome_link(html)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report drift, change nothing")
    args = parser.parse_args()

    drifted: list[str] = []
    for name in PAGES:
        path = SITE_DIR / name
        if not path.exists():
            raise SystemExit(f"missing site page: {path}")
        current = path.read_text(encoding="utf-8")
        wanted = sync_page(path)
        if current == wanted:
            continue
        drifted.append(name)
        if not args.check:
            path.write_text(wanted, encoding="utf-8")

    if args.check:
        if drifted:
            print("navbar drift in: " + ", ".join(drifted))
            return 1
        print(f"navbar in sync across {len(PAGES)} pages")
        return 0

    print(f"updated {len(drifted)} of {len(PAGES)} pages" + (": " + ", ".join(drifted) if drifted else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
