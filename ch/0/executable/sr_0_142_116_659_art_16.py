"""SR 0.142.116.659 Art. 16

Generated from: ch/0/de/0.142.116.659.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class request_transfer_cost(Variable):
    value_type = int
    entity = Country
    definition_period = DAY
    label = "Request transfer procedure formalism cost"

    def formula(countries, period, parameters):
        return 0.1
