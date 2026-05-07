"""SR 0.142.115.989 Art. 3

Generated from: ch/0/de/0.142.115.989.md
"""

from openfisca_core.model_api import *
from openfisca_core periods import Month


class extradition_transport_costs(Variable):
    value_type = float
    definition_period = DURATION
    label = "Extradition transport costs (Art. 3 Protocol)"

    def formula(d, period, parameters):
        return parameters(period).miscellaneous.extradition_transport_costs
