"""SR 192.121 Art. 6

Generated from: ch/192/de/192.121.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 6 lists which institutional beneficiaries receive privileges. Enumerative/declaratory, no computable rule.
