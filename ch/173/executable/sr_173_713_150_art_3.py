"""SR 173.713.150 Art. 3

Generated from: ch/173/de/173.713.150.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 3 sets entry into force date. Purely temporal.
