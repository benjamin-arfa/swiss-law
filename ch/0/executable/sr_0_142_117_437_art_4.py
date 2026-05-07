"""SR 0.142.117.437 Art. 4

Generated from: ch/0/de/0.142.117.437.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Permit

class permit_unaffected_labour_market(Variable):
    value_type = bool
    entity = Permit
    definition_period = PERIOD.yearly
    label = "Permit unaffected by foreign country's labour market"
    reference = "SR 0.142.117.437 Art. 4"

    def formula(p, period, parameters):
        return True
