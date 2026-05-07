"""SR 0.142.116.919 Art. 18

Generated from: ch/0/de/0.142.116.919.md
"""

This treaty regulation does not specify any direct application or calculation logic that can be translated into the OpenFisca framework.
However, for a hypothetical scenario where data is exchanged and used to determine benefits for policy recipients, one might create variables to track data transmission.

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class data_transmitted(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Data transmission status (Art. 18 SR 0.142.116.919)"
    set_input = set_input_divide_by_period

    def formula(person, period, parameters):
        return person("data_notification", period) and person("data_acknowledged", period)
