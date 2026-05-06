"""SR 321.0 Art. 38

Generated from: ch/321/de/321.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class probezeit_min_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Mindestdauer der Probezeit (2 Jahre)"
    reference = "SR 321.0 Art. 38 Abs. 1"
    default_value = 2


class probezeit_max_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Hoechstdauer der Probezeit (5 Jahre)"
    reference = "SR 321.0 Art. 38 Abs. 1"
    default_value = 5
