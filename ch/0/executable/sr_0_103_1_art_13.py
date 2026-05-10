"""SR 0.103.1 Art. 13

Generated from: ch/0/de/0.103.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class education_accessibility(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Basic education accessibility for every citizen (Art. 13 (2) SR 0.103.1)"

    def formula(person, period, parameters):
        age_16 = (period.date.year - person("date_of_birth", period).year) < 16
        returned_to_school_since_age_14 = person("age_first_school_return", period)
        first_school_return_after_age_14 = period.overlap(returned_to_school_since_age_14, period.after(person("age_14", period)))

        free_access_to_primary_education = person("attended_freeprimary_school", period)

        return age_16 & free_access_to_primary_education & first_school_return_after_age_14


class higher_education_access(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Higher education accessible for everyone (Art. 13 (2) SR 0.103.1)"

    def formula(person, period, parameters):
        income_bracket_thresholds = parameters(period).education.higher_education.income_bracket_thresholds

        higher_education_funded = person("access_to_higher_education", period)
        has_net_income_less_than_1_yearly_income_bracket = person("net_income", period) < income_bracket_thresholds

        return higher_education_funded & has_net_income_less_than_1_yearly_income_bracket


class adult_education_services_access(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Adult education and further education services accessible for everyone (Art. 13 (2) SR 0.103.1)"

    def formula(person, period, parameters):
        age_25 = (period.date.year - person("date_of_birth", period).year) < 25
        participated_in_vocational_training_program = person("completed_vocational_training", period)
        is_net_income_above_all_income_brackets = person("net_income", period) > parameters(period).education.higher_education.income_bracket_thresholds

        return age_25 & participated_in_vocational_training_program & is_net_income_above_all_income_brackets
