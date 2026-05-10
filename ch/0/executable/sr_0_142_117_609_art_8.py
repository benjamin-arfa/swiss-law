"""SR 0.142.117.609 Art. 8

Generated from: ch/0/de/0.142.117.609.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class valid_immigration_status(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Valid immigration status (Art. 8 SR 0.142.117.609)"

    def formula(person, period, parameters):
        immigration_status_verified = person("immigration_status_verified", period)
        proof_with_forged_documents = person("proof_with_forged_documents", period)
        return immigration_status_verified | proof_with_forged_documents
