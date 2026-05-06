"""SR 196.1 Art. 21

Generated from: ch/196/de/196.1.md

Beschwerde: Gegen Verfuegungen kann Beschwerde gefuehrt werden.
Die Beschwerde hat keine aufschiebende Wirkung.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 21 regulates the appeals procedure.
# Procedural provision, no computable rule.
