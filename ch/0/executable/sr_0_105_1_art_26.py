"""SR 0.105.1 Art. 26

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import Variable
from openfisca_switzerland.entities import Government


class preventive_measures_donation(Variable):
    value_type = float
    entity = Government
    default_unit = "CHF"
    label = "Preventive measures donation for SR 0.105.1 Art. 26"

    def formula(government, period, parameters):
        # No fixed amount in the law
        return 0
