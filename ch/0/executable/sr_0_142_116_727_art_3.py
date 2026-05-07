"""SR 0.142.116.727 Art. 3

Generated from: ch/0/de/0.142.116.727.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class young_worker_limit(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Young worker limit (SR 0.142.116.727 Art. 3)"

    def formula(person, period, parameters):
        return parameters(period).labour_market.young_worker_limit
