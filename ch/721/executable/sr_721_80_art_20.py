"""SR 721.80 Art. 20

Generated from: ch/721/de/721.80.md

Art. 20 - Federal acquisition of private water rights:
1. When the Confederation acquires water power from a public water body
   from a riparian owner (Art. 2(2)), it must compensate the canton for
   the special tax/levy on produced electricity (Art. 18).
2. Additionally, the Confederation pays the canton CHF 11/year per kW
   of installed gross capacity as tax compensation; Art. 14 applies analogously.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class wrg_privatrecht_steuerkompensation(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Tax compensation for federal acquisition of private water rights (CHF/year)"
    reference = "SR 721.80 Art. 20 Abs. 2"

    def formula(person, period, parameters):
        bruttoleistung = person('wrg_bruttoleistung_kw', period)
        satz = parameters(period).sr_721_80.steuerausfall_entschaedigung_pro_kw

        # Same rate as Art. 14
        return bruttoleistung * satz
