"""SR 934.21 Art. 5a

Generated from: ch/934/de/934.21.md

Art. 5a Rekapitalisierung:
1. The Confederation ensures adequate equity endowment when converting
   existing armament operations into corporations.
2. The Federal Council determines the manner, timing, and extent of the
   required recapitalization. The resulting burden is capitalized in the
   Confederation's balance sheet and depreciated over several years
   through the income statement.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bgrb_rekapitalisierung_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Rekapitalisierung bei der Ueberfuehrung erforderlich ist"
    reference = "SR 934.21 Art. 5a Abs. 1"

    def formula(person, period, parameters):
        return person('bgrb_betrieb_ueberfuehrt', period)


class bgrb_rekapitalisierung_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hoehe der Rekapitalisierung in CHF"
    reference = "SR 934.21 Art. 5a Abs. 2"


class bgrb_abschreibung_erfolgsrechnung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Belastung ueber mehrere Jahre in der Erfolgsrechnung abgeschrieben wird"
    reference = "SR 934.21 Art. 5a Abs. 2"

    def formula(person, period, parameters):
        betrag = person('bgrb_rekapitalisierung_betrag', period)
        return betrag > 0
