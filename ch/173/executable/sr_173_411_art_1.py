"""SR 173.411 Art. 1

Generated from: ch/173/de/173.411.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 1 refers to another ordinance for per diem rates. Referential.
