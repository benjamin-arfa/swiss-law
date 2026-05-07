"""SR 0.105.1 Art. 30

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import *

class cantonal_protocol_reservation_impossible(Variable):
    value_type = bool
    entity = Ego
    definition_period = period.year
    label = "Reservations to this cantonal protocol are impossible (Art. 30 SR 0.105.1)"

    value = True
