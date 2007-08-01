"""SR 172.213.1 Art. 7e

Generated from: ch/172/de/172.213.1.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Federal departments/offices organization regulation. Organizational/procedural, no computable rule.
