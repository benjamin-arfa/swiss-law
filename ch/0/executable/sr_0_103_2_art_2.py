"""SR 0.103.2 Art. 2

Generated from: ch/0/de/0.103.2.md
"""

From the provided information it is not possible to create any variable, since there is no information about entities or periods, but for the sake of completeness, here's how it could be defined:
from openfisca_core.model_api import *
from openfisca_country_entities import Person


class iccpr_compliance(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Compliance with the International Covenant on Civil and Political Rights (ICCPR)"

    def formula(person, period, parameters):
        return False  # for default value, as no concrete conditions were identified
