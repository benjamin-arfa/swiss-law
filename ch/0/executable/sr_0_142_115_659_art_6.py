"""SR 0.142.115.659 Art. 6

Generated from: ch/0/de/0.142.115.659.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Determine whether an application for transfer is required
class application_for_transfer_required(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Whether an application for transfer is required (art 6)"

    def formula(person, period, parameters):
        is_third_country_national = person("third_country_nationality", period)
        person_has_documents = (person("valid_passport", period) or 
                                person("valid_visum", period))

        country_parameters = parameters(period).social_security.application_for_transfer
        country_authority_exemption = country_parameters.require_documents
        valid_documents_period = country_parameters.document_validity_period

        return not is_third_country_national or (person_has_documents and 
                                                country_authority_exemption and 
                                                any((person.date('birth_date') + valid_documents_period) > today()))
