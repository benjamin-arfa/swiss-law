"""SR 451.1 Art. 4

Generated from: ch/451/de/451.1.md

Skipped: Rein prozedural - Regelung zu globalen Finanzhilfen auf Basis von
Programmvereinbarungen. Keine konkreten berechenbaren Betraege.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Rein prozedural - Globale Finanzhilfen Programmvereinbarung
