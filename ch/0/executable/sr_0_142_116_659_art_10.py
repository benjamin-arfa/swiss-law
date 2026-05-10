"""SR 0.142.116.659 Art. 10

Generated from: ch/0/de/0.142.116.659.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class proof_of_circumstances(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Proof of circumstances for re-admission (Art. 10 SR 0.142.116.659)"

    def formula(person, period, parameters):
        has_valid_documents = (person("passport_status", period) == True) | (
            person("visa_status", period) == True)
        has_certificate_from_annex_3 = (person("annex_3_certificate", period) == True)
        has_certificate_from_annex_4 = (person("annex_4_certificate", period) == True)

        return (has_valid_documents | has_certificate_from_annex_3 | has_certificate_from_annex_4)
