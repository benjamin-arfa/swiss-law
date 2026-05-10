"""SR 0.142.117.149 Art. 8

Generated from: ch/0/de/0.142.117.149.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class authorized_data_use(bool):
    entity = Person
    definition_period = 'forever'
    label = "Authorized data use (Art. 8.1a)"

    def formula(person, period, parameters):
        return True

class notified_data_user(bool):
    entity = Person
    definition_period = 'forever'
    label = "Data user notification (Art. 8.1b)"

    def formula(person, period, parameters):
        return True

class limited_access(bool):
    entity = Person
    definition_period = 'forever'
    label = "Limited data access (Art. 8.1c)"

    def formula(person, period, parameters):
        return True

class verified_data(bool):
    entity = Person
    definition_period = 'forever'
    label = "Data accuracy verification (Art. 8.1d)"

    def formula(person, period, parameters):
        return True

class informed_individual(bool):
    entity = Person
    definition_period = 'forever'
    label = "Individual informed about their data (Art. 8.1e)"

    def formula(person, period, parameters):
        return True

class stored_data(bool):
    entity = Person
    definition_period = 'forever'
    label = "Data storage and retention (Art. 8.1f)"

    def formula(person, period, parameters):
        return True

class protected_data(bool):
    entity = Person
    definition_period = 'forever'
    label = "Protected data from unauthorized access (Art. 8.1g)"

    def formula(person, period, parameters):
        return True

class returnedIndividualPersonalDataScope(scope):
    entity = Person
    definition_period = 'forever'
    label = "Scope of personal data for returned individuals (Art. 8.2)"

    def formula_affected_by(person, period, parameters):
        scope = [
            "personal_identifiers",
            "identity_documents",
            "additional_identifying_details",
            "travel_routes",
            "travel_authorizations",
        ]
        return scope
