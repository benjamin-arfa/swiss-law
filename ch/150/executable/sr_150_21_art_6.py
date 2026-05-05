"""SR 150.21 Art. 6

Generated from: ch/150/de/150.21.md

Einwilligung der gesuchten Person: Muss schriftlich oder in anderer
nachweisbarer Form erteilt werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class einwilligung_schriftlich_oder_nachweisbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Einwilligung schriftlich oder in nachweisbarer Form erteilt wurde"
    reference = "SR 150.21 Art. 6"
