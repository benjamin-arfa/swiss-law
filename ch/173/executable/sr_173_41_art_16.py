"""SR 173.41 Art. 16

Generated from: ch/173/de/173.41.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Patent Court Act (PatGG). Organizational/procedural, no computable rule.
