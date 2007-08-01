"""SR 173.711.33 Art. 14

Generated from: ch/173/de/173.711.33.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Judges' travel and per diem regulation. Organizational/procedural, no computable rule.
