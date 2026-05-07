"""SR 0.142.117.437 Art. 8

Generated from: ch/0/de/0.142.117.437.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class became_stagiaire(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Became stagiaire (Art. 8 SR 0.142.117.437)"

    def formula(person, period, parameters):
        return True  # Implement the two conditions (finding a job and supported job search) using events or business rules
