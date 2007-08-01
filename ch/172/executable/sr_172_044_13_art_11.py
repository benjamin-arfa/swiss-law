"""SR 172.044.13 Art. 11

Generated from: ch/172/de/172.044.13.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Federal financial administration regulation. Organizational/procedural, no computable rule.
