"""SR 192.121 Art. 19

Generated from: ch/192/de/192.121.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 19 states that institutional beneficiaries determine social welfare modalities. Referential/procedural, no computable rule.
