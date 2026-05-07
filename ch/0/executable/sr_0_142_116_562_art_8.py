"""SR 0.142.116.562 Art. 8

Generated from: ch/0/de/0.142.116.562.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country as Entity

# Use the generic name 'Country' instead of an entity import from the code
class international_obligation_exempt(Variable):
    value_type = bool
    entity = Entity
    definition_period = YEAR
    label = "International obligations exempt under SR 0.142.116.562 Art. 8"

    def formula(country, period, parameters):
        return True
