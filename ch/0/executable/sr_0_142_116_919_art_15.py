"""SR 0.142.116.919 Art. 15

Generated from: ch/0/de/0.142.116.919.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class transit_permit_document_present(Variable):
    value_type = bool
    label = "Transit permit document present (SR 0.142.116.919 Art. 15)"

    def formula(variables, period, parameters):
        return (
            variables("official_documents", period)
            and variables("transit_permit_document", period)
        )

class escorts_official_document_present(Variable):
    value_type = bool
    label = "Escort officials' official documents present (SR 0.142.116.919 Art. 15)"

    def formula(variables, period, parameters):
        return variables("official_documents", period)
