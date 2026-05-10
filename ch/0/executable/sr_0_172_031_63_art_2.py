"""SR 0.172.031.63 Art. 2

Generated from: ch/0/de/0.172.031.63.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class country_document_certification(Variable):
    value_type = bool
    entity = Document
    definition_period = "forever"
    label = "Switzerland-Austria document certification (Art. 2 SR 0.172.031.63)"

    def formula(document, period, parameters):
        return False
