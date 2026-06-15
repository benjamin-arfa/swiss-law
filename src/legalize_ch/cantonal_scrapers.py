"""Dedicated scrapers for LexFind-only cantons that serve HTML law texts.

GE (Geneva):  silgeneve.ch/legis/program/books/rsg/
NE (Neuchâtel): rsn.ne.ch/DATA/program/books/rsne/
"""
from __future__ import annotations

import logging
import re
import time
from datetime import date

import requests

from .cantonal import CantonalLawEntry, CantonalLawText

logger = logging.getLogger(__name__)

MAX_RETRIES = 3
INITIAL_BACKOFF = 2.0
RETRYABLE_HTTP_CODES = {429, 500, 502, 503, 504}


class _HTMLFetcher:
    """Base for HTML-scraping cantonal fetchers."""

    def __init__(self, rate_limit: float = 1.0):
        self.rate_limit = rate_limit
        self._last_request = 0.0
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "legalize-ch/0.1 (swiss-law pipeline)",
            "Accept": "text/html",
        })

    def _throttle(self):
        elapsed = time.time() - self._last_request
        if elapsed < self.rate_limit:
            time.sleep(self.rate_limit - elapsed)
        self._last_request = time.time()

    def _get(self, url: str, encoding: str = "utf-8") -> str:
        backoff = INITIAL_BACKOFF
        for attempt in range(1, MAX_RETRIES + 1):
            self._throttle()
            try:
                resp = self.session.get(url, timeout=30)
                if resp.status_code == 404:
                    return ""
                if resp.status_code in RETRYABLE_HTTP_CODES and attempt < MAX_RETRIES:
                    time.sleep(backoff)
                    backoff *= 2
                    continue
                resp.raise_for_status()
                resp.encoding = encoding
                return resp.text
            except requests.exceptions.RequestException as e:
                if attempt < MAX_RETRIES:
                    time.sleep(backoff)
                    backoff *= 2
                else:
                    logger.error("Failed %s: %s", url, e)
        return ""


# ─── Geneva (GE) ─────────────────────────────────────────────────────────────

GE_BASE = "https://silgeneve.ch/legis/program/books/rsg"
GE_TOC = f"{GE_BASE}/toc.htm"
GE_HTM = f"{GE_BASE}/htm"


class GeneveFetcher(_HTMLFetcher):
    """Fetch Geneva cantonal law from silgeneve.ch (RSG)."""

    def fetch_catalog(self, lang: str = "fr") -> list[CantonalLawEntry]:
        html = self._get(GE_TOC, encoding="latin-1")
        if not html:
            return []

        entries: list[CantonalLawEntry] = []
        rows = re.findall(
            r'<a\s+href="htm/(rsg_[^"]+\.htm)"[^>]*>\s*([^<]+)</a>'
            r'.*?</td>\s*<td[^>]*>\s*<p[^>]*>(.*?)</p>',
            html,
            re.DOTALL,
        )

        for filename, sys_num_raw, title_raw in rows:
            sys_num = re.sub(r"\s+", " ", sys_num_raw).strip()
            title = re.sub(r"<[^>]+>", "", title_raw).strip()
            title = re.sub(r"\s+", " ", title)

            entries.append(CantonalLawEntry(
                canton="ge",
                systematic_number=sys_num,
                title=title,
                abbreviation=_extract_abbreviation(title),
                enactment_date=None,
                is_active=True,
                lexfind_id=filename,
            ))

        logger.info("GE catalog: fetched %d laws", len(entries))
        return entries

    def fetch_law_text(
        self, systematic_number: str, lang: str = "fr",
        filename: str = "",
    ) -> CantonalLawText | None:
        if not filename:
            filename = _sys_num_to_ge_filename(systematic_number)

        url = f"{GE_HTM}/{filename}"
        html = self._get(url, encoding="latin-1")
        if not html:
            return None

        return _parse_ge_html(html, systematic_number, lang)


def _sys_num_to_ge_filename(sys_num: str) -> str:
    """Convert systematic number like 'A 2 04' to filename 'rsg_a2_04.htm'."""
    parts = sys_num.strip().lower().split()
    if len(parts) >= 3:
        return f"rsg_{'_'.join(parts)}.htm"
    cleaned = re.sub(r"\s+", "_", sys_num.strip().lower())
    return f"rsg_{cleaned}.htm"


def _parse_ge_html(html: str, systematic_number: str, lang: str) -> CantonalLawText | None:
    title_m = re.search(r"<title[^>]*>([^<]+)</title>", html, re.IGNORECASE)
    title = ""
    if title_m:
        raw = title_m.group(1).strip()
        title = re.sub(r"^rsGE\s+[A-Z]\s*\d+\s*\d+\S*\s*:\s*", "", raw).strip()

    body_m = re.search(r"<body[^>]*>(.*?)</body>", html, re.DOTALL | re.IGNORECASE)
    content = body_m.group(1) if body_m else html

    version_date = None
    date_m = re.search(
        r"(?:du|Derni.res modifications au)\s+(\d{1,2})\s*(?:er)?\s*(\w+)\s+(\d{4})",
        content,
    )
    if date_m:
        version_date = _parse_french_date(date_m.group(1), date_m.group(2), date_m.group(3))

    if len(content) < 100:
        return None

    return CantonalLawText(
        canton="ge",
        systematic_number=systematic_number,
        title=title,
        html_content=content,
        language=lang,
        version_date=version_date,
        abbreviation=_extract_abbreviation(title),
    )


# ─── Neuchâtel (NE) ──────────────────────────────────────────────────────────

NE_BASE = "https://rsn.ne.ch/DATA/program/books/rsne"
NE_TOC = f"{NE_BASE}/toc.htm"
NE_HTM = f"{NE_BASE}/htm"


class NeuchatelFetcher(_HTMLFetcher):
    """Fetch Neuchâtel cantonal law from rsn.ne.ch (RSN)."""

    def fetch_catalog(self, lang: str = "fr") -> list[CantonalLawEntry]:
        html = self._get(NE_TOC, encoding="latin-1")
        if not html:
            return []

        entries: list[CantonalLawEntry] = []
        rows = re.findall(
            r'<a\s+href="htm/([^"]+\.htm)"[^>]*>\s*([^<]+)</a>'
            r'.*?</td>\s*<td[^>]*>\s*<p[^>]*>(.*?)</p>',
            html,
            re.DOTALL,
        )

        for filename, sys_num_raw, title_raw in rows:
            sys_num = re.sub(r"\s+", " ", sys_num_raw).strip()
            title = re.sub(r"<[^>]+>", "", title_raw).strip()
            title = re.sub(r"\s+", " ", title)

            entries.append(CantonalLawEntry(
                canton="ne",
                systematic_number=sys_num,
                title=title,
                abbreviation=_extract_abbreviation(title),
                enactment_date=None,
                is_active=True,
                lexfind_id=filename,
            ))

        logger.info("NE catalog: fetched %d laws", len(entries))
        return entries

    def fetch_law_text(
        self, systematic_number: str, lang: str = "fr",
        filename: str = "",
    ) -> CantonalLawText | None:
        if not filename:
            filename = f"{systematic_number}.htm"

        url = f"{NE_HTM}/{filename}"
        html = self._get(url, encoding="latin-1")
        if not html:
            return None

        return _parse_ne_html(html, systematic_number, lang)


def _parse_ne_html(html: str, systematic_number: str, lang: str) -> CantonalLawText | None:
    title_m = re.search(r"<title[^>]*>([^<]+)</title>", html, re.IGNORECASE)
    title = ""
    if title_m:
        raw = title_m.group(1).strip()
        title = re.sub(r"^\d[\d.]*\s*:\s*", "", raw).strip()

    body_m = re.search(r"<body[^>]*>(.*?)</body>", html, re.DOTALL | re.IGNORECASE)
    content = body_m.group(1) if body_m else html

    version_date = None
    date_m = re.search(
        r"du\s+(\d{1,2})\s*(?:er)?\s*(\w+)\s+(\d{4})",
        content,
    )
    if date_m:
        version_date = _parse_french_date(date_m.group(1), date_m.group(2), date_m.group(3))

    if len(content) < 100:
        return None

    return CantonalLawText(
        canton="ne",
        systematic_number=systematic_number,
        title=title,
        html_content=content,
        language=lang,
        version_date=version_date,
        abbreviation=_extract_abbreviation(title),
    )


# ─── Shared helpers ───────────────────────────────────────────────────────────

_FR_MONTHS = {
    "janvier": 1, "février": 2, "mars": 3, "avril": 4,
    "mai": 5, "juin": 6, "juillet": 7, "août": 8,
    "septembre": 9, "octobre": 10, "novembre": 11, "décembre": 12,
    "fevrier": 2, "aout": 8, "decembre": 12,
}


def _parse_french_date(day: str, month: str, year: str) -> date | None:
    m = _FR_MONTHS.get(month.lower())
    if not m:
        return None
    try:
        return date(int(year), m, int(day))
    except ValueError:
        return None


def _extract_abbreviation(title: str) -> str:
    m = re.search(r"\(([A-ZÀÂÉÈÊËÎÏÔÙÛÜÆŒÇ][A-ZÀÂÉÈÊËÎÏÔÙÛÜÆŒÇ-]{1,10})\)", title)
    return m.group(1) if m else ""
