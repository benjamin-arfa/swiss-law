"""SR 210 Art. 14

Generated from: ch/de/210.md

Volljaehrigkeit: Volljaehrig ist, wer das 18. Lebensjahr zurueckgelegt hat.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class alter(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Alter der Person in Jahren"
    reference = "SR 210 Art. 14"


class ist_volljaehrig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person volljaehrig ist (18 Jahre, Art. 14 ZGB)"
    reference = "SR 210 Art. 14"

    def formula(person, period, parameters):
        alter_person = person('alter', period)
        volljaehrigkeitsalter = parameters(period).zgb.volljaehrigkeitsalter
        return alter_person >= volljaehrigkeitsalter
