"""SR 0.103.3 Art. 32

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class committee_participation_status(Variable):
    value_type = bool
    entity = Organization
    definition_period = YEARS
    label = "Committee participation status (Art. 32 SR 0.103.3)"

    def formula(organization, period, parameters):
        is_participating = parameters(period).international_agreements.s0_103_3.participating_states.contains(organization)
        return is_participating
