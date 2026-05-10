"""SR 0.142.116.829 Art. 8

Generated from: ch/0/de/0.142.116.829.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class citizenship_established(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "Person recognized as a citizen as per Art. 8 SR 0.142.116.829"

    def formula(person, period, parameters):
        documents_accepted = parameters(period).admin.protocol_documents_accepted
        valid_documents_presented = person("valid_documents_presented", period)

        return valid_documents_presented & any(doc in documents_accepted for doc in person("presented_documents", period))
