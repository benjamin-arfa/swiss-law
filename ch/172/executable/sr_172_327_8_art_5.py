"""SR 172.327.8 Art. 5

Generated from: ch/172/de/172.327.8.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Federal justice administration regulation. Organizational/procedural, no computable rule.
