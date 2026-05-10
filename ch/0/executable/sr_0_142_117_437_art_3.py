"""SR 0.142.117.437 Art. 3

Generated from: ch/0/de/0.142.117.437.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class internship_allowance_eligibility(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligibility for internship allowance under international agreement"

    def formula(person, period, parameters):
        application_submitted = person("internship_application_submitted", period)
        international_agreement = person("international_agreement", period)
        return application_submitted & international_agreement

class internship_application_submitted(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Internship application submitted"

    def formula(person, period, parameters):
        application_form = person("application_form_submission_date", period)
        return application_form != 0

class international_agreement(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligibility for international agreement regarding internship placements"

    def formula(person, period, parameters):
        country_residence = person("country_of_residency", period)
        return country_residence == "Eligible"
