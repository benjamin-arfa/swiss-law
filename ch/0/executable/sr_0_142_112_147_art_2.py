"""SR 0.142.112.147 Art. 2

Generated from: ch/0/de/0.142.112.147.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class is_stagiaire(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Is a stagiaire (Art. 2 SR 0.142.112.147)"

    def formula(person, period, parameters):
        age = (period.date - person('birth_date', period)).days / 365.25
        return (age >= 18) & (age < 35) & person('completed_vocational_training', period)
