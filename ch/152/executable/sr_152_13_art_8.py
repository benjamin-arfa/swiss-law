"""SR 152.13 Art. 8 - Verlaengerung der Schutzfrist (Extension of Protection Period)

Generated from: ch/152/de/152.13.md

The Administrative Commission can extend the protection period if there
is an overriding legitimate public or private interest against access.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ueberwiegendes_schutzinteresse_bvger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein ueberwiegendes schutzwuerdiges Interesse gegen Einsichtnahme besteht"
    reference = "SR 152.13 Art. 8 Abs. 1"


class schutzfrist_verlaengert_bvger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Schutzfrist durch die Verwaltungskommission verlaengert wurde"
    reference = "SR 152.13 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        return person('ueberwiegendes_schutzinteresse_bvger', period)
