"""SR 822.11 Art. 12

Generated from: ch/822/de/822.11.md

Art. 12: Ueberzeitarbeit
- Abs. 1: Hoechstarbeitszeit darf ausnahmsweise ueberschritten werden
  (Dringlichkeit, Inventar, Betriebsstoerungen)
- Abs. 2: Ueberzeit max. 2 Stunden/Tag; Jahreshoechstgrenze:
  a. 170 Stunden bei 45h-Woche
  b. 140 Stunden bei 50h-Woche
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class arg_ueberzeit_stunden_tag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Ueberzeitarbeit pro Tag in Stunden"
    reference = "SR 822.11 Art. 12 Abs. 2"


class arg_ueberzeit_stunden_jahr(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Ueberzeitarbeit im Kalenderjahr in Stunden"
    reference = "SR 822.11 Art. 12 Abs. 2"


class arg_ueberzeit_jahreshoechstgrenze(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahreshoechstgrenze fuer Ueberzeitarbeit (170h oder 140h)"
    reference = "SR 822.11 Art. 12 Abs. 2"

    def formula(person, period, parameters):
        hoechstarbeitszeit = person('arg_woechentliche_hoechstarbeitszeit', period.first_month)
        # 170h for 45h-week workers; 140h for 50h-week workers
        return where(hoechstarbeitszeit <= 45.0, 170.0, 140.0)


class arg_ueberzeit_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ueberzeitarbeit liegt innerhalb der gesetzlichen Grenzen"
    reference = "SR 822.11 Art. 12 Abs. 2"

    def formula(person, period, parameters):
        stunden_jahr = person('arg_ueberzeit_stunden_jahr', period)
        grenze = person('arg_ueberzeit_jahreshoechstgrenze', period)
        return stunden_jahr <= grenze
