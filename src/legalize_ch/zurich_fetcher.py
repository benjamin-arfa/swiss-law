"""Fetch Zürich cantonal law from zh.ch (new API, replaces old zhlex.zh.ch).

The old ZHLex API at zhlex.zh.ch was decommissioned; the canton now serves
its law collection at zh.ch with a JSON catalog endpoint and server-rendered
HTML detail pages.
"""
from __future__ import annotations

import logging
import re
import time
from datetime import date
from typing import Any

import requests

from .cantonal import CantonalLawEntry, CantonalLawText, CantonalLawVersion

logger = logging.getLogger(__name__)

MAX_RETRIES = 4
INITIAL_BACKOFF = 2.0
BACKOFF_FACTOR = 2.0
RETRYABLE_HTTP_CODES = {429, 500, 502, 503, 504}

ZHCH_BASE = "https://www.zh.ch"
CATALOG_URL = (
    ZHCH_BASE
    + "/de/politik-staat/gesetze-beschluesse/gesetzessammlung"
    "/_jcr_content/main/lawcollectionsearch_312548694"
    ".zhweb-zhlex-ls.zhweb-cache.json"
)


class ZurichFetcher:
    """Fetches Zürich cantonal law from zh.ch."""

    def __init__(self, rate_limit: float = 1.0):
        self.rate_limit = rate_limit
        self._last_request = 0.0
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "legalize-ch/0.1 (swiss-law pipeline)",
        })

    def _throttle(self):
        elapsed = time.time() - self._last_request
        if elapsed < self.rate_limit:
            time.sleep(self.rate_limit - elapsed)
        self._last_request = time.time()

    def _get_json(self, url: str, params: dict | None = None) -> dict | None:
        backoff = INITIAL_BACKOFF
        for attempt in range(1, MAX_RETRIES + 1):
            self._throttle()
            try:
                resp = self.session.get(url, params=params, timeout=30,
                                        headers={"Accept": "application/json"})
                if resp.status_code == 404:
                    return None
                if resp.status_code in RETRYABLE_HTTP_CODES and attempt < MAX_RETRIES:
                    logger.warning("HTTP %d from %s (attempt %d)", resp.status_code, url, attempt)
                    time.sleep(backoff)
                    backoff *= BACKOFF_FACTOR
                    continue
                resp.raise_for_status()
                return resp.json()
            except requests.exceptions.RequestException as e:
                if attempt < MAX_RETRIES:
                    logger.warning("Failed %s (attempt %d): %s", url, attempt, e)
                    time.sleep(backoff)
                    backoff *= BACKOFF_FACTOR
                else:
                    logger.error("Failed %s after %d attempts: %s", url, MAX_RETRIES, e)
        return None

    def _get_html(self, url: str) -> str:
        backoff = INITIAL_BACKOFF
        for attempt in range(1, MAX_RETRIES + 1):
            self._throttle()
            try:
                resp = self.session.get(url, timeout=30,
                                        headers={"Accept": "text/html"})
                if resp.status_code in RETRYABLE_HTTP_CODES and attempt < MAX_RETRIES:
                    time.sleep(backoff)
                    backoff *= BACKOFF_FACTOR
                    continue
                resp.raise_for_status()
                return resp.text
            except requests.exceptions.RequestException as e:
                if attempt < MAX_RETRIES:
                    time.sleep(backoff)
                    backoff *= BACKOFF_FACTOR
                else:
                    logger.error("Failed %s: %s", url, e)
        return ""

    # ─── Catalog ──────────────────────────────────────────────────────────────

    def fetch_catalog(self, lang: str = "de") -> list[CantonalLawEntry]:
        entries: list[CantonalLawEntry] = []
        page = 1

        while True:
            data = self._get_json(CATALOG_URL, params={"page": page})
            if not data or "data" not in data:
                break

            items = data["data"]
            if not items:
                break

            for item in items:
                entry = _parse_catalog_entry(item)
                if entry:
                    entries.append(entry)

            total_pages = data.get("numberOfResultPages", 1)
            if page >= total_pages:
                break
            page += 1

        logger.info("ZH catalog: fetched %d laws", len(entries))
        return entries

    # ─── Law text ─────────────────────────────────────────────────────────────

    def fetch_law_text(
        self, systematic_number: str, lang: str = "de",
        erlass_id: str = "",
    ) -> CantonalLawText | None:
        link = erlass_id  # erlass_id stores the relative URL from catalog
        if not link:
            link = self._resolve_link(systematic_number)
        if not link:
            return None

        url = ZHCH_BASE + link if link.startswith("/") else link
        html = self._get_html(url)
        if not html:
            return None

        return _parse_law_html(html, systematic_number, lang)

    def _resolve_link(self, systematic_number: str) -> str:
        catalog = self.fetch_catalog()
        for entry in catalog:
            if entry.systematic_number == systematic_number:
                return entry.lexfind_id  # stores the link
        return ""

    # ─── Versions ─────────────────────────────────────────────────────────────

    def fetch_versions(self, systematic_number: str, erlass_id: str = "") -> list[CantonalLawVersion]:
        link = erlass_id or self._resolve_link(systematic_number)
        if not link:
            return []

        url = ZHCH_BASE + link if link.startswith("/") else link
        html = self._get_html(url)
        if not html:
            return []

        versions: list[CantonalLawVersion] = []
        for m in re.finditer(
            r'href="(/de/politik-staat/gesetze-beschluesse/gesetzessammlung/zhlex-ls/'
            r'erlass-[^"]+)"',
            html,
        ):
            v_link = m.group(1)
            v_match = re.search(
                r'erlass-([^-]+)-(\d{4})_(\d{2})_(\d{2})-(\d{4})_(\d{2})_(\d{2})',
                v_link,
            )
            if v_match:
                ref = v_match.group(1).replace("_", ".")
                try:
                    d = date(int(v_match.group(5)), int(v_match.group(6)), int(v_match.group(7)))
                except ValueError:
                    d = None
                versions.append(CantonalLawVersion(
                    canton="zh",
                    systematic_number=ref,
                    version_id=v_link,
                    title="",
                    date_in_force=d,
                    abbreviation="",
                ))

        versions.sort(key=lambda v: v.date_in_force or date.min)
        return versions

    def fetch_version_text(
        self, systematic_number: str, version_id: int | str,
        lang: str = "de",
    ) -> CantonalLawText | None:
        link = str(version_id)
        url = ZHCH_BASE + link if link.startswith("/") else link
        html = self._get_html(url)
        if not html:
            return None
        return _parse_law_html(html, systematic_number, lang)


# ─── Parsing helpers ──────────────────────────────────────────────────────────


def _parse_catalog_entry(item: dict) -> CantonalLawEntry | None:
    ref = item.get("referenceNumber", "")
    if not ref:
        return None

    title = item.get("enactmentTitle", "").strip()
    link = item.get("link", "")
    enactment_date = _parse_swiss_date(item.get("enactmentDate", ""))

    is_active = not item.get("withdrawalDate", "")

    return CantonalLawEntry(
        canton="zh",
        systematic_number=ref,
        title=title,
        abbreviation="",
        enactment_date=enactment_date,
        is_active=is_active,
        lexfind_id=link,
    )


def _parse_law_html(html: str, systematic_number: str, lang: str) -> CantonalLawText | None:
    title = ""
    m = re.search(r"<title[^>]*>([^<]+)</title>", html)
    if m:
        title = m.group(1).strip()
        title = re.sub(r"\s*\|.*$", "", title)

    content = _extract_content(html)
    if not content:
        return None

    version_date = None
    date_m = re.search(
        r'erlass-[^-]+-(\d{4})_(\d{2})_(\d{2})-(\d{4})_(\d{2})_(\d{2})',
        html,
    )
    if date_m:
        try:
            version_date = date(int(date_m.group(4)), int(date_m.group(5)), int(date_m.group(6)))
        except ValueError:
            pass

    return CantonalLawText(
        canton="zh",
        systematic_number=systematic_number,
        title=title,
        html_content=content,
        language=lang,
        version_date=version_date,
        abbreviation="",
    )


def _extract_content(html: str) -> str:
    for pattern in [
        r'<div[^>]*class="[^"]*mdl-richtext[^"]*"[^>]*>(.*?)</div>\s*</div>',
        r'<article[^>]*>(.*?)</article>',
        r'<main[^>]*>(.*?)</main>',
    ]:
        m = re.search(pattern, html, re.DOTALL)
        if m:
            block = m.group(1).strip()
            if len(block) > 200:
                return block

    sections = re.findall(
        r'(<(?:h[1-6]|p|div|table|ol|ul)[^>]*>.*?</(?:h[1-6]|p|div|table|ol|ul)>)',
        html,
        re.DOTALL,
    )
    candidate = "\n".join(sections)
    if len(candidate) > 500:
        return candidate

    body_m = re.search(r"<body[^>]*>(.*?)</body>", html, re.DOTALL)
    if body_m:
        return body_m.group(1)

    return html


def _parse_swiss_date(s: str) -> date | None:
    if not s:
        return None
    m = re.match(r"(\d{2})\.(\d{2})\.(\d{4})", s.strip())
    if m:
        try:
            return date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
        except ValueError:
            pass
    try:
        return date.fromisoformat(s.strip()[:10])
    except (ValueError, IndexError):
        pass
    return None
