"""SR 173.712.243 Art. 18

Generated from: ch/173/de/173.712.243.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Federal Criminal Court electronic case management regulation. Procedural, no computable rule.
