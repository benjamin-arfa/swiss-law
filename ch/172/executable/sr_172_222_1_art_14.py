"""SR 172.222.1 Art. 14

Generated from: ch/172/de/172.222.1.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Federal personnel regulation. Organizational/procedural, no computable rule.
