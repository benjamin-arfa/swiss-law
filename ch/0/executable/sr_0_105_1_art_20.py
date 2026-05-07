"""SR 0.105.1 Art. 20

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class data_access_to_deprivations_of_liberty(Variable):
    value_type = bool
    entity = Institution
    definition_period = YEAR
    label = "Data access for places of deprivation of liberty (SR 0.105.1)"

    def formula(institution, period, parameters):
        return True

class locations_of_deprivation_of_liberty_accessibility(Variable):
    value_type = bool
    entity = NationalPreventionMechanism
    definition_period = YEAR
    label = "Physical access to places of deprivation of liberty (SR 0.105.1)"


class ability_to_visit_deprivation_of_liberty(Variable):
    value_type = bool
    entity = NationalPreventionMechanism
    definition_period = YEAR
    label = "Autonomy of the National Prevention Mechanism (SR 0.105.1, Art. 20(e))"
