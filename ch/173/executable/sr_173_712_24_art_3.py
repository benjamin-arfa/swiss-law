"""SR 173.712.24 Art. 3

Generated from: ch/173/de/173.712.24.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Federal Criminal Court data/information regulation. Procedural, no computable rule.
