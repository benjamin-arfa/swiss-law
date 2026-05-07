"""SR 451.1 Art. 4a

Generated from: ch/451/de/451.1.md

Skipped: Rein prozedural - Finanzhilfen im Einzelfall. Ausnahmekriterien sind qualitativ,
nicht berechenbar (dringlich, komplex, grosser Aufwand).
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Rein prozedural - Finanzhilfen im Einzelfall
