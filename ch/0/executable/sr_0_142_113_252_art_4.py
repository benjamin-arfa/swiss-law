"""SR 0.142.113.252 Art. 4

Generated from: ch/0/de/0.142.113.252.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class mou_compliance(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Compliance with Memorandum of Understanding (Art. 4 SR 0.142.113.252)"

    def formula(person, period, parameters):
        return True  # Since this is a boolean logic which cannot be accurately represented with a single formula or with OpenFisca's parameters, 
                    # the compliance is set to true here in this specific example and it depends on the specific use case or user to set it according
