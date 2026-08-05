"""Tests for the LexFind frontend API client's version-group parsing."""
from __future__ import annotations

from legalize_ch.lexfind_frontend import LexfindFrontend


def _client_returning(payload):
    client = LexfindFrontend.__new__(LexfindFrontend)
    client.lang = "de"
    client._get = lambda path: payload
    return client


def _version(active_since, inactive_since=None, is_active=False, badge=None):
    v = {"family_active_since": "01.01.1970",
         "version_active_since": active_since,
         "is_active": is_active}
    if inactive_since:
        v["version_inactive_since"] = inactive_since
    if badge:
        v["info_badge"] = badge
    return v


class TestFamilyDates:
    def test_repealed_family_gets_inactive_since(self):
        payload = {"families": [[[
            _version("01.01.1970", "01.06.1990"),
            _version("01.06.1990", "31.12.2015"),
        ]]]}
        fam = _client_returning(payload).fetch_family_dates(7)
        assert fam.inactive_since is not None
        assert fam.inactive_since.isoformat() == "2015-12-31"

    def test_active_family_has_no_inactive_since(self):
        payload = {"families": [[[
            _version("01.01.1970", "01.06.1990"),
            _version("01.06.1990", is_active=True, badge="current"),
        ]]]}
        fam = _client_returning(payload).fetch_family_dates(7)
        assert fam.is_active is True
        assert fam.inactive_since is None

    def test_family_and_version_dates_still_parsed(self):
        payload = {"families": [[[
            _version("01.01.1970", "01.06.1990"),
            _version("01.06.1990", is_active=True, badge="current"),
        ]]]}
        fam = _client_returning(payload).fetch_family_dates(7)
        assert fam.family_active_since.isoformat() == "1970-01-01"
        assert [d.isoformat() for d in fam.version_dates] == [
            "1970-01-01", "1990-06-01"]
