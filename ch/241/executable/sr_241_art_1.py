"""SR 241 Art. 1

Generated from: ch/de/241.md

Purpose: This law ensures fair and undistorted competition
in the interest of all participants.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class uwg_zweck_lauterer_wettbewerb(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der lautere und unverfaelschte Wettbewerb gewaehrleistet wird"
    reference = "SR 241 Art. 1"

    def formula(person, period, parameters):
        return 1
