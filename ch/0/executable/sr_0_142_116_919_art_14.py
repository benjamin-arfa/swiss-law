"""SR 0.142.116.919 Art. 14

Generated from: ch/0/de/0.142.116.919.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class is_escort_personnel(Variable):
    value_type = bool
    definition_period = YEAR
    label = "Indicator for escort personnel (Art. 14 SR 0.142.116.919)"

    def formula(individual, period, parameters):
        return individual("is_escort_personnel", period)
