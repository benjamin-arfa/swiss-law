"""SR 0.105.1 Art. 29

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country


class protocol_applies_without_restrictions(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Application of protocol without restrictions or exceptions (Art. 29 SR 0.105.1)"

    def formula(countries, period, parameters):
        return True
