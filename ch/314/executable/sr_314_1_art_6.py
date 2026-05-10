"""SR 314.1 Art. 6

Generated from: ch/314/de/314.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bedenkfrist_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Bedenkfrist fuer die Bezahlung der Ordnungsbusse (30 Tage)"
    reference = "SR 314.1 Art. 6 Abs. 1"
    default_value = 30


class busse_sofort_bezahlt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die beschuldigte Person hat die Busse sofort bezahlt"
    reference = "SR 314.1 Art. 6 Abs. 2"


class busse_innerhalb_frist_bezahlt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die beschuldigte Person hat die Busse innerhalb der Bedenkfrist bezahlt"
    reference = "SR 314.1 Art. 6 Abs. 3"


class ordentliches_strafverfahren_wegen_nichtzahlung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es wird ein ordentliches Strafverfahren durchgefuehrt wegen Nichtzahlung"
    reference = "SR 314.1 Art. 6 Abs. 4"

    def formula(person, period, parameters):
        sofort = person('busse_sofort_bezahlt', period)
        frist = person('busse_innerhalb_frist_bezahlt', period)
        return not_(sofort) * not_(frist)
