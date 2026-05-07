"""SR 0.105 Art. 16

Generated from: ch/0/de/0.105.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Institution


class human_rights_treatment(Variable):
    value_type = bool
    entity = Institution
    definition_period = YEAR
    label = "Compliance with Article 16 SR 0.105 Federal Law, no cruel, inhuman or degrading treatment"

    def formula(Institution, period, parameters):
        state_actor = Institution("is_state_actor", period)
        event_type = Institution("human_rights_event_type", period)
        punished = Institution("punished", period)

        return state_actor & event_type.is_any(['cruel', 'inhuman', 'degrading']) & punished


class human_rights_event_type(Enum):
    cruel = 'cruel'
    inhuman = 'inhuman'
    degrading = 'degrading'
