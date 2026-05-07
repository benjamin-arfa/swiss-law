"""SR 0.142.113.499 Art. 23

Generated from: ch/0/de/0.142.113.499.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Government


class international_cooperation Indicator:
    value_type = bool
    entity = Government
    definition_period = YEAR

    def formula(government, period, parameters):
        return True  # Indicator would be True by default, as it's an obligation to cooperate
