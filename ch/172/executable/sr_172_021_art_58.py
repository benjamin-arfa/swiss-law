"""SR 172.021 Art. 58

Generated from: ch/172/de/172.021.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Administrative procedure regulation. Procedural, no computable rule.
