"""SR 0.142.116.659 Art. 9

Generated from: ch/0/de/0.142.116.659.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class citizenship_proven(Variable):
    value_type = bool
    entity = Person
    definition_period = ON
    label = "Citizenship successfully proven (Art. 9 SR 0.142.116.659)"

    def formula(person, period, parameters):
        try:
            # Check if the citizenship is listed amongst the valid documents
            presented_document = person("presented_document", period)
            valid_documents = person("valid_documents", period)
            expired_documents = person("expired_documents", period)

            # If valid documents are provided, citizenship is proven
            if presented_document in valid_documents:
                return True

            # If valid documents are not provided but expired ones are, citizenship is proven if the document type is in Annex A
            elif presented_document in expired_documents and person("annex_a", period):
                return True

        except ValueError:
            # If no documents are provided, a detailed verification or investigation will be triggered
            # This results in citizenship not being proven immediately
            return False
