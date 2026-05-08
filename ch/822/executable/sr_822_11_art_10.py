"""SR 822.11 Art. 10

Generated from: ch/822/de/822.11.md

Art. 10: Tages- und Abendarbeit
- Abs. 1: Tagesarbeit = 6-20 Uhr; Abendarbeit = 20-23 Uhr; bewilligungsfrei
- Abs. 2: Betriebliche Tages-/Abendarbeit kann zwischen 5 und 24 Uhr
  verschoben werden (max. 17 Stunden Zeitraum)
- Abs. 3: Tages-/Abendarbeit des einzelnen AN muss inkl. Pausen und
  Ueberzeit innerhalb von 14 Stunden liegen
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class arg_tagesarbeit_beginn_uhr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    default_value = 6
    label = "Beginn der betrieblichen Tagesarbeit (Stunde, Standard: 6 Uhr)"
    reference = "SR 822.11 Art. 10 Abs. 1-2"


class arg_abendarbeit_ende_uhr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    default_value = 23
    label = "Ende der betrieblichen Abendarbeit (Stunde, Standard: 23 Uhr)"
    reference = "SR 822.11 Art. 10 Abs. 1-2"


class arg_betriebliche_tagesabendarbeit_zeitraum(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Betrieblicher Tages-/Abendarbeit-Zeitraum in Stunden"
    reference = "SR 822.11 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        beginn = person('arg_tagesarbeit_beginn_uhr', period)
        ende = person('arg_abendarbeit_ende_uhr', period)
        return ende - beginn


class arg_betriebliche_tagesabendarbeit_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Betriebliche Tages-/Abendarbeit-Regelung ist zulaessig (max. 17h Zeitraum, 5-24 Uhr)"
    reference = "SR 822.11 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        beginn = person('arg_tagesarbeit_beginn_uhr', period)
        ende = person('arg_abendarbeit_ende_uhr', period)
        zeitraum = person('arg_betriebliche_tagesabendarbeit_zeitraum', period)
        return (beginn >= 5) * (ende <= 24) * (zeitraum <= 17)


class arg_taegliche_arbeitszeit_stunden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Taegliche Arbeitszeit inkl. Pausen und Ueberzeit in Stunden"
    reference = "SR 822.11 Art. 10 Abs. 3"


class arg_taegliche_arbeitszeit_innerhalb_14h(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Taegliche Arbeitszeit inkl. Pausen und Ueberzeit liegt innerhalb von 14 Stunden"
    reference = "SR 822.11 Art. 10 Abs. 3"

    def formula(person, period, parameters):
        arbeitszeit = person('arg_taegliche_arbeitszeit_stunden', period)
        return arbeitszeit <= 14.0
