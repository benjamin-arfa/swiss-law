"""SR 451.1 Art. 6

Generated from: ch/451/de/451.1.md

Skipped: Rein deklarativ - Beitragsberechtigt sind nur tatsaechlich entstandene
und erforderliche Aufwendungen. Keine berechenbare Formel.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Rein deklarativ - Definition beitragsberechtigter Aufwendungen
