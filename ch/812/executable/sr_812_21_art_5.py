"""SR 812.21 Art. 5

Generated from: ch/812/de/812.21.md

Art. 5: Bewilligungspflicht - Manufacturing license requirement for medicines.
Anyone manufacturing medicines or adding medicines to animal feed needs
an institute license.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class hmg_stellt_arzneimittel_her(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person stellt Arzneimittel her"
    reference = "SR 812.21 Art. 5 Abs. 1 Bst. a"


class hmg_mischt_arzneimittel_futtermitteln_bei(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person mischt Arzneimittel Futtermitteln bei"
    reference = "SR 812.21 Art. 5 Abs. 1 Bst. b"


class hmg_herstellungsbewilligung_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bewilligung des Instituts für Herstellung erforderlich"
    reference = "SR 812.21 Art. 5"

    def formula(person, period, parameters):
        herstellt = person('hmg_stellt_arzneimittel_her', period)
        beimischt = person('hmg_mischt_arzneimittel_futtermitteln_bei', period)
        return herstellt + beimischt > 0
