"""SR 0.104 Art. 2

Generated from: ch/0/de/0.104.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class racial_discrimination indicator(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Indicator for being subject to racial discrimination"

    def formula(person, period, parameters):
        return True  # A placeholder, but does not accurately represent the real-world implications of racial discrimination.

class counteractive_measures_taken(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Benefit from counteractive measures taken against racial discrimination"

    def formula(person, period, parameters):
        multiracial_organizations_supported = person("multiracial_organizations_supported", period)
        return multiracial_organizations_supported
