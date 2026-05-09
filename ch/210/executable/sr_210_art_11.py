"""SR 210 Art. 11

Generated from: ch/de/210.md

Rechtsfaehigkeit: Jeder Mensch ist rechtsfaehig und hat die gleiche
Faehigkeit, Rechte und Pflichten zu haben.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_rechtsfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person rechtsfaehig ist (Art. 11 ZGB)"
    reference = "SR 210 Art. 11"

    def formula(person, period, parameters):
        # Abs. 1: Rechtsfaehig ist jedermann.
        # Abs. 2: Alle Menschen haben die gleiche Faehigkeit, Rechte und
        # Pflichten zu haben.
        # Rechtsfaehigkeit beginnt mit der Geburt (Art. 31).
        ist_geboren = person('ist_lebend_geboren', period)
        return ist_geboren
