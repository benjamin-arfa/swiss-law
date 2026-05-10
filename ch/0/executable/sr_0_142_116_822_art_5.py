"""SR 0.142.116.822 Art. 5

Generated from: ch/0/de/0.142.116.822.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class multiple_entry_swiss_visa(Variable):
    value_type = bool
    entity = Person
    definition_period = WEEK
    label = "Multiple entry Swiss visa for person"

    def formula(person, period, parameters):
        # conditions for categories to obtain 5-year multiple entry visa
        categories_5_years = [
            (person("is_a_member_official_delegation", period)),
            (person("is_member_regional_government", period) & ~person("is_free_of_visa_requirements", period)),
            (person("is_spouse_child_of_serbian_citizen", period) & person("has_serbian_citizen_residence", period)),
        ]

        # conditions for categories to obtain 1-year multiple entry visa
        categories_1_year = [
            (person("is_a_member_official_delegation", period) & person("already_received_single_entry_visa", period)),
            (person("is_business_traveller", period) & person("already_received_single_entry_visa", period)),
            (person("is_driver", period) & person("already_received_single_entry_visa", period)),
            (person("is_train_engineer", period) & person("already_received_single_entry_visa", period)),
            (person("is_journalist", period) & person("already_received_single_entry_visa", period)),
            (person("is_scientist", period) & person("already_received_single_entry_visa", period)),
            (person("is_studying_in_ch", period) & person("already_received_single_entry_visa", period)),
            (person("is_athlete", period) & person("already_received_single_entry_visa", period)),
            (person("is_member_of_cultural_event", period) & person("already_received_single_entry_visa", period)),
            (person("is_doctor", period) & person("already_received_single_entry_visa", period)),
            (person("is_representative_of_zghc", period) & person("already_received_single_entry_visa", period)),
            (person("is_freelancer", period) & person("already_received_single_entry_visa", period)),
        ]

        # conditions for multiple entry visa
        return [
            ((x == True).evalf() if x else False for x in categories_5_years) |
            ((x == True).evalf() if x else False for x in categories_1_year)
        ]


# TODO: This needs to be split into conditions for each category of multiple entry visa
# The variable must have parameters to represent each type of multiple entry visa
