"""SR 513.51 Art. 4

Generated from: ch/513/de/513.51.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


# Skipped: Art. 4 is a transitional/repeal provision.
# It repeals prior federal decisions and sets the entry into force date.
# No computable rule.
