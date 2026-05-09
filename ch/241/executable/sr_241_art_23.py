"""SR 241 Art. 23

Generated from: ch/de/241.md

Criminal penalties for intentional unfair competition:
imprisonment up to 3 years or monetary penalty for violations
of Art. 3, 4, 5, or 6.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class uwg_straftat_vorsaetzlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob vorsaetzlich unlauterer Wettbewerb nach Art. 3, 4, 5 oder 6 begangen wird"
    reference = "SR 241 Art. 23 Abs. 1"


class uwg_strafmass_freiheitsstrafe_max_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Freiheitsstrafe in Jahren"
    reference = "SR 241 Art. 23 Abs. 1"

    def formula(person, period, parameters):
        return person('uwg_straftat_vorsaetzlich', period) * 3


class uwg_strafantrag_berechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person einen Strafantrag stellen kann (Art. 9 und 10 berechtigt)"
    reference = "SR 241 Art. 23 Abs. 2"
