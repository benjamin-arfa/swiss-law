"""SR 196.1 Art. 22

Generated from: ch/196/de/196.1.md

Zusammenarbeit unter schweizerischen Behoerden.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 22 regulates inter-agency cooperation.
# Procedural/organizational provision, no computable rule.
