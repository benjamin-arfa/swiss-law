"""SR 232.21 Art. 35

Generated from: ch/232/de/232.21.md

Art. 35 regulates the transitional right to continue using coats of arms
(Weiterbenuetzungsrecht) after the WSchG came into force.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class wappen_gebrauch_nach_bisherigem_recht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Wappen wurde nach bisherigem Recht gebraucht"
    reference = "SR 232.21 Art. 35 Abs. 1"


class wappen_gebrauch_seit_30_jahren(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Schweizerkreuz oder verwechselbares Zeichen wurde seit mindestens 30 Jahren ununterbrochen und unangefochten verwendet"
    reference = "SR 232.21 Art. 35 Abs. 3 lit. a"


class schutzwuerdiges_interesse_weiterbenuetzung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Es besteht ein schutzwuerdiges Interesse an der Weiterbenuetzung"
    reference = "SR 232.21 Art. 35 Abs. 3 lit. b"


class weiterbenuetzungsrecht_wappen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Weiterbenuetzungsrecht fuer Schweizerwappen nach Art. 35 WSchG"
    reference = "SR 232.21 Art. 35"

    def formula(person, period, parameters):
        # Abs. 3: besondere Umstaende muessen vorliegen
        seit_30_jahren = person('wappen_gebrauch_seit_30_jahren', period)
        interesse = person('schutzwuerdiges_interesse_weiterbenuetzung', period)
        return seit_30_jahren * interesse
