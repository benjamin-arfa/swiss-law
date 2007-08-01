"""SR 192.121 Art. 4

Generated from: ch/192/de/192.121.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 4 defines the concept of the principal beneficiary person (hauptberechtigte Person). Purely definitional, no computable rule.
