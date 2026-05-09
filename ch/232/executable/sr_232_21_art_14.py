"""SR 232.21 Art. 14

Generated from: ch/232/de/232.21.md

Art. 14 establishes the registration prohibition for signs whose use
is impermissible under Art. 8-13.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class gebrauch_unzulaessig_art_8_bis_13(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gebrauch des Zeichens ist nach Art. 8-13 WSchG unzulaessig"
    reference = "SR 232.21 Art. 14 Abs. 1"


class eintragungsverbot_zeichen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Das Zeichen darf nicht als Marke, Design, Firma etc. eingetragen werden"
    reference = "SR 232.21 Art. 14 Abs. 1"

    def formula(person, period, parameters):
        unzulaessig = person('gebrauch_unzulaessig_art_8_bis_13', period)
        weiterben = person('hat_weiterbenuetzungsrecht_art_35', period)
        # Abs. 1: Eintragungsverbot wenn Gebrauch unzulaessig
        # Abs. 3: Ausnahme bei Weiterbenuetzungsrecht nach Art. 35
        return unzulaessig * (1 - weiterben)
