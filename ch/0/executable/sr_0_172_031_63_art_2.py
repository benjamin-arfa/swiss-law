"""SR 0.172.031.63 Art. 2

Generated from: ch/0/de/0.172.031.63.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Document


class country_document_certification(Variable):
    value_type = bool
    entity = Document
    definition_period = "forever"
    label = "Switzerland-Austria document certification (Art. 2 SR 0.172.031.63)"

    def formula(document, period, parameters):
        return False
