"""SR 0.142.117.432 Art. 1

Generated from: ch/0/de/0.142.117.432.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class visa_free_residence(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for visa-free residence in another country"

    def formula(person, period, parameters):
        # Implement conditions from Art. 1 para. 1, 2, 3 and 5
        # For now, it's a placeholder
        return True

class visa_free_work(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for visa-free work in another country"

    def formula(person, period, parameters):
        # Implement conditions from Art. 1 para. 4 and 5
        # For now, it's a placeholder
        return True
