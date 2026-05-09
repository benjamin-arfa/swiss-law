"""SR 831.30 Art. 7

Generated from: ch/831/de/831.30.md

Art. 7: Ausschluss kantonaler Einschraenkungen - Exclusion of cantonal
restrictions.

The entitlement to supplementary benefits may not be made dependent on:
- a specific duration of residence in the canton, or
- the possession of civil rights (buergerliche Ehren und Rechte).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class el_kanton_verlangt_wohndauer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Kanton verlangt eine bestimmte Wohn-/Aufenthaltsdauer als EL-Voraussetzung"
    reference = "SR 831.30 Art. 7"


class el_kanton_verlangt_buergerrechte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Kanton verlangt Besitz der buergerlichen Ehren und Rechte als EL-Voraussetzung"
    reference = "SR 831.30 Art. 7"


class el_kantonale_einschraenkung_unzulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Kantonale EL-Einschraenkung ist unzulaessig (Art. 7 ELG)"
    reference = "SR 831.30 Art. 7"

    def formula(person, period, parameters):
        wohndauer = person('el_kanton_verlangt_wohndauer', period)
        buergerrechte = person('el_kanton_verlangt_buergerrechte', period)
        return wohndauer + buergerrechte > 0
