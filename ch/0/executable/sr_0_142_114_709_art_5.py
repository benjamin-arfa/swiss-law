"""SR 0.142.114.709 Art. 5

Generated from: ch/0/de/0.142.114.709.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class additional_documents_to_consider(Variable):
    value_type = bool
    default_value = False
    label = "Consider additional documents for nationality (Art. 5 SR 0.142.114.709)"

    def formula(Scenario, period, parameters):
        additional_documents = Scenario("additional_documents", period)
        return additional_documents
