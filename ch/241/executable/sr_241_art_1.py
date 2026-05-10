"""SR 241 Art. 1

Generated from: ch/de/241.md

Purpose: This law ensures fair and undistorted competition
in the interest of all participants.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class uwg_zweck_lauterer_wettbewerb(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der lautere und unverfaelschte Wettbewerb gewaehrleistet wird"
    reference = "SR 241 Art. 1"

    def formula(person, period, parameters):
        return 1
