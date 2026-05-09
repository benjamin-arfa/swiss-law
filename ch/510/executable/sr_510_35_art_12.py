"""SR 510.35 Art. 12 - Strafbestimmungen

Generated from: ch/510/de/510.35.md

Widerhandlungen gegen diese Verordnung werden nach Massgabe von Art. 107
des Militaerstrafgesetzes geahndet. Vorbehalten bleibt die Ahndung gemaess
Strafgesetzbuch.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class widerhandlung_gegen_seuchenpolizei_vo(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Widerhandlung gegen die Verordnung ueber seuchenpolizeiliche Massnahmen der Armee vorliegt"
    reference = "SR 510.35 Art. 12 Abs. 1"


class strafbar_nach_milstg_107(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person nach Art. 107 MStG (Ungehorsam gegen militaerische Massnahmen) strafbar ist"
    reference = "SR 510.35 Art. 12 Abs. 1"

    def formula(person, period, parameters):
        return person('widerhandlung_gegen_seuchenpolizei_vo', period)
