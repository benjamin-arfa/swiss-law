"""SR 0.142.116.659 Art. 16

Generated from: ch/0/de/0.142.116.659.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country


class request_transfer_cost(Variable):
    value_type = int
    entity = Country
    definition_period = DAY
    label = "Request transfer procedure formalism cost"

    def formula(countries, period, parameters):
        return 0.1
