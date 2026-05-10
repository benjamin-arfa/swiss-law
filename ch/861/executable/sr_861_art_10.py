"""SR 861 Art. 10

Generated from: ch/de/861.md

Referendum, validity duration and entry into force. The law is subject
to optional referendum. Multiple extensions of validity period,
most recently to 31 December 2026.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class kbfhg_fakultatives_referendum(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das KBFHG dem fakultativen Referendum untersteht"
    reference = "SR 861 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        return True


class kbfhg_urspruengliche_geltungsdauer_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Urspruengliche Geltungsdauer des KBFHG in Jahren"
    reference = "SR 861 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        return 8


class kbfhg_geltungsdauer_verlaengert_bis_2026(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Geltungsdauer des KBFHG bis zum 31. Dezember 2026 verlaengert wurde"
    reference = "SR 861 Art. 10 Abs. 8"

    def formula(person, period, parameters):
        return True
