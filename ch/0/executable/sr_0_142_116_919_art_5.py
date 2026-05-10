"""SR 0.142.116.919 Art. 5

Generated from: ch/0/de/0.142.116.919.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class country_of_provenance(Variable):
    value_type = bool
    label = "Provenance country"
    entity = Household

class is_stateless_person(Variable):
    value_type = bool
    label = "Stateless person"
    entity = Person

class visa_status(Variable):
    value_type = str
    label = "Visa status"
    entity = Household

class short_term_visitor(Variable):
    value_type = bool
    label = "Short-term visa"
    entity = Household

class foreign_national(Variable):
    value_type = bool
    label = "Foreign national"
    entity = Household

class legal_entry_history(Variable):
    value_type = bool
    label = "Legal entry history within threshold"
    entity = Household

class has_long_stay_document(Variable):
    value_type = bool
    label = "Holds valid long-stay document (permit, visa)"
    entity = Household

class has_valid_long_stay_permit_from_country(Variable):
    value_type = bool
    label = "Holds valid long-stay permit from country"
    entity = Household

class has_geneva_convention_status(Variable):
    value_type = bool
    label = "Recognized refugee or asylum seeker with international protection"
    entity = Household

class asylum_return_history(Variable):
    value_type = bool
    label = "History of asylum return"
    entity = Household

class has_identity_document_from_country(Variable):
    value_type = bool
    label = "Holds identity document from country"
    entity = Household

class is_in_compliance_with_return_obligation(Variable):
    value_type = bool
    label = "Is in compliance with return obligation"
    entity = Household

    def formula(household, period, parameters):
        foreign_national_1 = household("foreign_national_1", period)
        foreign_national_2 = household("foreign_national_2", period)

        short_term_visitor_1 = household("short_term_visitor_1", period)
        short_term_visitor_2 = household("short_term_visitor_2", period)

        visa_status_1 = household("visa_status_1", period)
        visa_status_2 = household("visa_status_2", period)

        has_valid_long_stay_permit_from_country_1 = household("has_valid_long_stay_permit_from_country_1", period)
        has_valid_long_stay_permit_from_country_2 = household("has_valid_long_stay_permit_from_country_2", period)

        has_geneva_convention_status = household("has_geneva_convention_status", period)

        asylum_return_history = household("asylum_return_history", period)

        has_id_from_country_1 = household("has_id_from_country_1", period)
        has_id_from_country_2 = household("has_id_from_country_2", period)

        if (foreign_national):
            if (short_term_visitor or (visa_status == "temporary_visas") and (has_valid_long_stay_permit_from_country == True) or (has_id_from_country == True) or (has_geneva_convention_status == True) or (asylum_return_history == True)):
                return True
        else:
            if (short_term_visitor or visa_status == "temporary_visas" or has_valid_long_stay_permit_from_country == False or has_id_from_country == True or has_geneva_convention_status == True or asylum_return_history == True):
                return False
        return False
