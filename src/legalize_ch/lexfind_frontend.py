"""Client for LexFind's real frontend API (/api/frontend/v1/{lang}/).

Discovered by enumerating the SPA bundle's routes (the legacy /api/fe/
carries no dates; this API does). Key endpoint:
``texts-of-law/{id}/with-version-groups`` returns, per law "family":
``family_active_since`` (the ORIGINAL date of the act) and every version
with ``version_active_since``/``version_inactive_since`` — for all 26
cantons. ``entities/{id}/recent-changes`` carries change types incl.
``abrogated`` and ``removed``; ``global/stats`` gives LexFind's total
tol counts (incl. inactive) for coverage cross-checks.
"""
from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from datetime import date

from .cantonal import CantonalFetcher

logger = logging.getLogger(__name__)

FRONTEND_API = "https://www.lexfind.ch/api/frontend/v1"

_DDMMYYYY = re.compile(r"^(\d{2})\.(\d{2})\.(\d{4})$")


def _parse_ddmmyyyy(s: str | None) -> date | None:
    m = _DDMMYYYY.match(str(s or "").strip())
    if not m:
        return None
    try:
        return date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
    except ValueError:
        return None


@dataclass
class FamilyDates:
    tol_id: int
    family_active_since: date | None = None
    version_dates: list[date] = field(default_factory=list)  # sorted asc
    is_active: bool | None = None
    # date the family left force: the LAST version's inactive date, only
    # meaningful when no version is still active (repealed families)
    inactive_since: date | None = None


class LexfindFrontend:
    """Thin wrapper reusing CantonalFetcher's retry/backoff HTTP stack."""

    def __init__(self, rate_limit: float = 0.1, lang: str = "de"):
        self.fetcher = CantonalFetcher(rate_limit=rate_limit)
        self.lang = lang

    def _get(self, path: str):
        return self.fetcher._get_json(f"{FRONTEND_API}/{self.lang}{path}")

    def fetch_family_dates(self, tol_id: int | str) -> FamilyDates | None:
        """Family (original) date + all version dates for one law."""
        data = self._get(f"/texts-of-law/{tol_id}/with-version-groups")
        if not isinstance(data, dict):
            return None
        fam = FamilyDates(tol_id=int(tol_id))
        earliest_family = None
        vdates: set[date] = set()
        inactive: set[date] = set()
        any_version_active = False
        for family in data.get("families", []):
            for group in family:
                for v in group if isinstance(group, list) else [group]:
                    if not isinstance(v, dict):
                        continue
                    fa = _parse_ddmmyyyy(v.get("family_active_since"))
                    if fa and (earliest_family is None or fa < earliest_family):
                        earliest_family = fa
                    vs = _parse_ddmmyyyy(v.get("version_active_since"))
                    if vs:
                        vdates.add(vs)
                    vi = _parse_ddmmyyyy(v.get("version_inactive_since"))
                    if vi:
                        inactive.add(vi)
                    if v.get("is_active"):
                        any_version_active = True
                    if v.get("info_badge") == "current":
                        fam.is_active = bool(v.get("is_active", True))
        fam.family_active_since = earliest_family
        fam.version_dates = sorted(vdates)
        if inactive and not any_version_active:
            fam.inactive_since = max(inactive)
        return fam

    def fetch_global_stats(self) -> dict | None:
        return self._get("/global/stats")

    def fetch_recent_changes(self, entity_id: int) -> dict | None:
        return self._get(f"/entities/{entity_id}/recent-changes")
