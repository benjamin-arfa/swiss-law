"""SR 414.110.21 Art. 4

Generated from: ch/414/de/414.110.21.md

Waehlbarkeit in die ETH-Beschwerdekommission:
1. Als Mitglied waehlbar ist, wer nicht aelter als 65 ist.
2. Praesident, Vizepraesident und mind. ein weiteres Mitglied muessen
   rechtskundig sein.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vethbk_alter(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Alter der Person in Jahren"
    reference = "SR 414.110.21 Art. 4 Abs. 1"


class vethbk_ist_rechtskundig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person rechtskundig ist"
    reference = "SR 414.110.21 Art. 4 Abs. 2"


class vethbk_ist_waehlbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person als Mitglied der ETH-Beschwerdekommission waehlbar ist"
    reference = "SR 414.110.21 Art. 4"

    def formula(person, period, parameters):
        alter = person('vethbk_alter', period)
        altersgrenze = parameters(period).sr_414_110_21.altersgrenze
        return alter <= altersgrenze
