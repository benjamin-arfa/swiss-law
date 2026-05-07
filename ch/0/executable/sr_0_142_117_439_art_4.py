"""SR 0.142.117.439 Art. 4

Generated from: ch/0/de/0.142.117.439.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import ThirdStateNational


class extradition_requested(Variable):
    value_type = bool
    entity = ThirdStateNational
    definition_period = ANY
    label = "Extradition request for third state national (Art. 4 SR 0.142.117.439)"

    def formula(third_state_national, period, parameters):
        condition_a = (third_state_national("stay_duration", period) <= 5)
        valid_permit_present = third_state_national("has_valid_residence_permit", period)

        return condition_a | valid_permit_present
