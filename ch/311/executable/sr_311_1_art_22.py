"""SR 311.1 Art. 22

Generated from: ch/311/de/311.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class verweis_probezeit_min_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Minimale Probezeit bei Verweis (6 Monate)"
    reference = "SR 311.1 Art. 22 Abs. 2"
    default_value = 6


class verweis_probezeit_max_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Probezeit bei Verweis (2 Jahre)"
    reference = "SR 311.1 Art. 22 Abs. 2"
    default_value = 2
