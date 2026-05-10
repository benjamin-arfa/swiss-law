"""SR 0.142.117.439 Art. 1

Generated from: ch/0/de/0.142.117.439.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class recognized_nationality(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "AHV employee contribution (Art. 1 SR 0.142.117.439)"

    def formula(person, period, parameters):
        nationality_documents = parameters(period).civic_recognition.naturalisation.documents
        other_evidence = parameters(period).civic_recognition.naturalisation.evidence

        # assuming other_evidence is a list
        return person.has_attr('has_naturalised_document', nationality_documents) or any(person.has_attr(attr_name, other_evidence) for attr_name in other_evidence)
