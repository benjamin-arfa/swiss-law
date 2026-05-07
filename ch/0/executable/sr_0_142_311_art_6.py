"""SR 0.142.311 Art. 6

Generated from: ch/0/de/0.142.311.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class valid_visa_for_treaty_country(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Valid visa for a crew member from another treaty country (Art. 6 SR 0.142.311)"

    def formula(person, period, parameters):
        visa = person("valid_visa", period)
        return visa
