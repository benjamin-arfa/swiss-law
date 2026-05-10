"""SR 0.142.113.679 Art. 3

Generated from: ch/0/de/0.142.113.679.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class accepted_document_type(Variable):
    value_type = str
    entity = Person
    definition_period = DAY
    label = "List of valid document types for ID purposes (Art. 3 SR 0.142.113.679)"

    def formula(person, period, parameters):
        document_types = parameters(period).acceptance_document.list
        return person("document_type", period)

class document_accepted(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "Whether a document is accepted to prove identity (Art. 3 SR 0.142.113.679)"

    def formula(person, period, parameters):
        document_types = parameters(period).acceptance_document.list
        document_currently_valid = person("document_currently_valid", period)
        is_document_type_currently_valid = person("document_type", period) in document_types
        if document_currently_valid:
            return is_document_type_currently_valid
        elif params_period.legacy:
            return doc_type_past in params_period.legacy

class has_document_type(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "Whether a person has evidence to prove their identity (Art. 3 SR 0.142.113.679)"

    def formula(person, period, parameters):
        document_types = parameters(period).acceptance_document.list
        return document_types == person("document_type", period)

# parameter variable definitions go here
