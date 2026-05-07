"""SR 0.103.1 Art. 10

Generated from: ch/0/de/0.103.1.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person, Child


class child_vulnerable(Variable):
    value_type = bool
    label = "Vulnerable child status (age below protection threshold)"
    entity = Person
    definition_period = YEAR
    reference = "Social Security Act, Art. 10, para. 3"

    def formula(person, period, parameters):
        child_entity = person('child', period)
        min_age_limit = parameters(period).demographics.child_vulnerable_protection.min_age
        child_age = (child_entity("age", period) + 1)  # consider the upcoming birthday
        return (child_age < min_age_limit) & (child_entity("economically_active", period) == True)
