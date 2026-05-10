"""SR 0.142.111.368 Art. 13

Generated from: ch/0/de/0.142.111.368.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class entry_into_force_date(Variable):
    value_type = int
    default_value = 2024
    label = "Entry into force date for this agreement (SR 0.142.111.368, Art. 13)"

    def formula(_input, period, parameters):
        return period.year
