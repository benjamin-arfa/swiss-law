"""SR 0.142.116.657 Art. 3

Generated from: ch/0/de/0.142.116.657.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class trainee_status(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR  # Evaluation unnecessary, but here for dynamic simulation compatibility
    label = "Trainee Status (Art. 3 of the SR 0.142.116.657)"

    def formula(person, period, parameters):
        born_on = person("birth_date", period)
        current_age = (period.date - born_on).days / 365.25
        max_age = 30
        min_age = 18

        trainee = (min_age <= current_age) & (current_age < max_age)

        # Assuming this is covered elsewhere in OpenFisca code
        # health_check = True  # Assuming this is covered elsewhere in OpenFisca code

        education_completed = person("education_completed", period)
        return trainee & education_completed
