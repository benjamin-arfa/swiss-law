"""SR 732.1 Art. 9

Generated from: ch/732/de/732.1.md

Wiederaufarbeitung: Abgebrannte Brennelemente sind als radioaktive
Abfaelle zu entsorgen. Sie duerfen nicht wiederaufgearbeitet oder
zur Wiederaufarbeitung ausgefuehrt werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class sind_abgebrannte_brennelemente(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um abgebrannte Brennelemente handelt"
    reference = "SR 732.1 Art. 9 Abs. 1"


class dient_forschungszwecken(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Wiederaufarbeitung Forschungszwecken dient"
    reference = "SR 732.1 Art. 9 Abs. 2"


class wiederaufarbeitung_verboten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Wiederaufarbeitung verboten ist"
    reference = "SR 732.1 Art. 9"

    def formula(person, period, parameters):
        brennelemente = person('sind_abgebrannte_brennelemente', period)
        forschung = person('dient_forschungszwecken', period)

        # Grundsaetzlich verboten, Ausnahme fuer Forschungszwecke
        return brennelemente * (1 - forschung)
