"""SR 173.320.11 Art. 8

Generated from: ch/173/de/173.320.11.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Federal Administrative Court internal regulation. Organizational/procedural, no computable rule.
