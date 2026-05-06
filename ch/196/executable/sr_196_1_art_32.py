"""SR 196.1 Art. 32

Generated from: ch/196/de/196.1.md

Uebergangsbestimmungen: Bereits gesperrte Vermoegenswerte bleiben gesperrt.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 32 contains transitional provisions.
# Procedural provision, no computable rule.
