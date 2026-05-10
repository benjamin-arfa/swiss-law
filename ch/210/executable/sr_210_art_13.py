"""SR 210 Art. 13

Generated from: ch/de/210.md

Voraussetzungen der Handlungsfaehigkeit: Die Handlungsfaehigkeit besitzt,
wer volljaehrig und urteilsfaehig ist.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class erfuellt_voraussetzungen_handlungsfaehigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Voraussetzungen der Handlungsfaehigkeit erfuellt sind (Art. 13 ZGB)"
    reference = "SR 210 Art. 13"

    def formula(person, period, parameters):
        # Die Handlungsfaehigkeit besitzt, wer volljaehrig und
        # urteilsfaehig ist.
        ist_volljaehrig = person('ist_volljaehrig', period)
        ist_urteilsfaehig = person('ist_urteilsfaehig', period)
        return ist_volljaehrig * ist_urteilsfaehig
