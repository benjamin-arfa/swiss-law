"""SR 173.413.3 Art. 8

Generated from: ch/173/de/173.413.3.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Patent Court fees regulation. Procedural, no computable rule.
