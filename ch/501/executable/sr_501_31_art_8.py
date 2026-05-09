"""SR 501.31 Art. 8 - Leitungskonferenz KSD

Generated from: ch/501/de/501.31.md

Die Leitungskonferenz KSD beraet das BABS in allen sanitaetsdienstlichen
Koordinationsbelangen und unterstuetzt es bei der Umsetzung der Koordination.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_mitglied_leitungskonferenz_ksd(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Mitglied der Leitungskonferenz KSD ist"
    reference = "SR 501.31 Art. 8 Abs. 2"


class leitungskonferenz_beraet_babs(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Leitungskonferenz KSD das BABS in sanitaetsdienstlichen Koordinationsbelangen beraet"
    reference = "SR 501.31 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        return person('ist_mitglied_leitungskonferenz_ksd', period)
