"""SR 0.142.116.907 Art. 1

Generated from: ch/0/de/0.142.116.907.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class eligible_for_stages_program(Variable):
    value_type = bool
    entity = Stagiaire
    definition_period = YEAR
    label = "Eligibility for the work exchange stages program"

    def formula(stagiaire, period, parameters):
        age = (period.date - stagiaire("birth_date")).days / 365.25
        min_age = parameters(period).slovakia_stages_program.min_age
        max_age = parameters(period).slovakia_stages_program.max_age
        is_between = (age >= min_age) & (age <= max_age)

        nationality = stagiaire("nationality", period)
        is_swiss_or_slovak = nationality == "CH" or nationality == "SK"
        restricted_professions = parameters(period).slovakia_stages_program.restricted_professions

        is_eligible_profession = (
            stagiaire("profession", period) not in restricted_professions
            if not is_swiss_or_slovak else True
        )

        # Additional permit check
        permit_check = stagiaire("has_permitted_profession", period)

        return is_between & is_eligible_profession & permit_check


class has_permitted_profession(Variable):
    value_type = bool
    entity = Stagiaire
    definition_period = YEAR
    label = "Has a permitted profession for the work exchange stages program"

    def formula(stagiaire, period, parameters):
        # This would generally require external data integration.
        # For simplicity, assume a hypothetical variable that indicates if permit is required for profession.
        required_permit = parameters(period).slovakia_stages_program.need_special_permit[stagiaire("profession")]
        permit_required = required_permit and not stagiaire("has_special_permit", period)
        return permit_required


class need_special_permit(Variable):
    value_type = dict
    entity = Stagiaire
    definition_period = YEAR
    label = "Need a special permit for the work exchange stages program"

    def formula(stagiaire, period, parameters):
        # This requires data to be predefined.
        permit_requirements = parameters(period).slovakia_stages_program.need_special_permit
        return permit_requirements
