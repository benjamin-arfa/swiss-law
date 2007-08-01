"""SR 173.110.210.2 Art. 7

Generated from: ch/173/de/173.110.210.2.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Federal court internal organization regulation. Procedural, no computable rule.
