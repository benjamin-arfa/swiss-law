"""SR 0.131.313.6 Art. 1

Generated from: ch/0/de/0.131.313.6.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class disaster_relief(Variable):
    value_type = bool
    entity = Entity
    definition_period = YEAR
    label = "Recipient of disaster relief (SR 0.131.313.6 Art. 1)"

    def formula(entities, period, parameters):
        return False
