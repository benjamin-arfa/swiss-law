"""SR 151.3 Art. 6

Generated from: ch/151/de/151.3.md

Dienstleistungen Privater: Diskriminierungsverbot.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_privater_dienstleistungsanbieter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person privat Dienstleistungen oeffentlich anbietet"
    reference = "SR 151.3 Art. 6"


class diskriminierung_wegen_behinderung_privat(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein privater Dienstleister Behinderte wegen Behinderung diskriminiert"
    reference = "SR 151.3 Art. 6"
