"""SR 210 Art. 34

Generated from: ch/de/210.md

Anzeichen des Todes: Der Tod einer Person kann, auch wenn niemand die
Leiche gesehen hat, als erwiesen betrachtet werden, sobald die Person unter
Umstaenden verschwunden ist, die ihren Tod als sicher erscheinen lassen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_unter_todesumstaenden_verschwunden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person unter Umstaenden verschwunden ist, die den Tod als sicher erscheinen lassen"
    reference = "SR 210 Art. 34"


class ist_leiche_gesehen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Leiche der Person gesehen wurde"
    reference = "SR 210 Art. 34"


class kann_tod_als_erwiesen_gelten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Tod als erwiesen betrachtet werden kann (Art. 34 ZGB)"
    reference = "SR 210 Art. 34"

    def formula(person, period, parameters):
        # Tod kann als erwiesen gelten, auch ohne Leiche, wenn
        # Umstaende den Tod als sicher erscheinen lassen
        leiche_gesehen = person('ist_leiche_gesehen', period)
        unter_todesumstaenden = person('ist_unter_todesumstaenden_verschwunden', period)
        return leiche_gesehen + unter_todesumstaenden > 0
