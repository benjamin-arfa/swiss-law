"""SR 141.01 Art. 10

Generated from: ch/141/de/141.01.md

Eheliche Gemeinschaft: Setzt formelles Bestehen einer Ehe und
tatsaechliche Lebensgemeinschaft voraus. Muss bei Gesuchstellung
und Einbuergerung bestehen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ehe_formell_bestehend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob formell eine Ehe besteht"
    reference = "SR 141.01 Art. 10 Abs. 1"


class tatsaechliche_lebensgemeinschaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine tatsaechliche Lebensgemeinschaft mit gemeinsamem Willen zu stabiler Ehe besteht"
    reference = "SR 141.01 Art. 10 Abs. 1"


class eheliche_gemeinschaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine eheliche Gemeinschaft im Sinne von Art. 10 BueV vorliegt"
    reference = "SR 141.01 Art. 10"

    def formula(person, period, parameters):
        formell = person('ehe_formell_bestehend', period)
        lebensgemeinschaft = person('tatsaechliche_lebensgemeinschaft', period)
        return formell * lebensgemeinschaft
