"""SR 138.1 Art. 7 - Mitwirkung bei der Umsetzung internationalen Rechts

Generated from: ch/138/de/138.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class umsetzung_internationalen_rechts_obliegt_kantonen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Umsetzung des internationalen Rechts obliegt den Kantonen"
    reference = "SR 138.1 Art. 7"


class kantone_verpflichtet_zur_anpassung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Kantone sind verpflichtet die erforderlichen Anpassungen rechtzeitig vorzunehmen"
    reference = "SR 138.1 Art. 7"

    def formula(self, period, parameters):
        return self('umsetzung_internationalen_rechts_obliegt_kantonen', period)
