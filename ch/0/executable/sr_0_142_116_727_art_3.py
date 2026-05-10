"""SR 0.142.116.727 Art. 3

Generated from: ch/0/de/0.142.116.727.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class young_worker_limit(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Young worker limit (SR 0.142.116.727 Art. 3)"

    def formula(person, period, parameters):
        return parameters(period).labour_market.young_worker_limit
