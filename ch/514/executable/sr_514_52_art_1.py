"""SR 514.52 Art. 1

Generated from: ch/514/de/514.52.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


# Skipped: Art. 1 is a mandate to the Federal Council to procure new fighter jets.
# It sets a deadline (end of 2030) but contains no computable rule per se.
