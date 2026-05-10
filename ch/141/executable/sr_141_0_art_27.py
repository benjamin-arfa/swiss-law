"""SR 141.0 Art. 27 - Wiedereinbuergerung nach Verwirkung, Entlassung und Verlust

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class jahre_seit_verlust_buergerrecht(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Jahre seit Verlust des Schweizer Buergerrechts"
    reference = "SR 141.0 Art. 27 Abs. 1"


class aufenthalt_schweiz_seit_3_jahren(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person hat seit 3 Jahren Aufenthalt in der Schweiz"
    reference = "SR 141.0 Art. 27 Abs. 2"


class kann_wiedereinbuergerung_beantragen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person kann eine Wiedereinbuergerung beantragen"
    reference = "SR 141.0 Art. 27"

    def formula(self, period, parameters):
        jahre = self('jahre_seit_verlust_buergerrecht', period)
        aufenthalt_3j = self('aufenthalt_schweiz_seit_3_jahren', period)

        # Abs. 1: Innerhalb von 10 Jahren
        innerhalb_frist = jahre <= 10

        # Abs. 2: Nach Ablauf der Frist, wenn 3 Jahre Aufenthalt
        nach_frist = (jahre > 10) * aufenthalt_3j

        return innerhalb_frist + nach_frist > 0
