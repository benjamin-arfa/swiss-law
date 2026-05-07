"""SR 446.2 Art. 11

Generated from: ch/446/de/446.2.md

Skipped: Anforderungskatalog an Jugendschutzregelung - Liste von 10 Mindestanforderungen (a-j).
Zu komplex fuer einzelne Formeln; dient als Pruefkatalog.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Anforderungskatalog (Bst. a-j) - qualitative Pruefkriterien, keine quantitative Formel
