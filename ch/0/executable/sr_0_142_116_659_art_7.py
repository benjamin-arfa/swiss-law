"""SR 0.142.116.659 Art. 7

Generated from: ch/0/de/0.142.116.659.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class personal_details(Variable):
    value_type = str
    entity = Household
    definition_period = YEAR
    label = "Personaliy details for social security requests"

    def formula(household, period, parameters):
        first_name = household("first_name", period)
        surname = household("surname", period)
        date_of_birth = household("date_of_birth", period)
        possible_foreign_status = household("foreign_status", period)

        return str(first_name) + " " + str(surname) + " " + str(date_of_birth) + " " + str(possible_foreign_status)
