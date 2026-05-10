"""SR 170.32 Art. 7

Generated from: ch/170/de/170.32.md

Rückgriff des Bundes auf den Beamten bei Vorsatz oder grober Fahrlässigkeit.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class beamter_hat_vorsaetzlich_gehandelt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Beamte hat den Schaden vorsätzlich verschuldet (Art. 7 VG)"
    reference = "SR 170.32, Art. 7"


class beamter_hat_grobfahrlaessig_gehandelt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Beamte hat den Schaden grobfahrlässig verschuldet (Art. 7 VG)"
    reference = "SR 170.32, Art. 7"


class bund_hat_ersatz_geleistet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bund hat dem Geschädigten Ersatz geleistet (Art. 7 VG)"
    reference = "SR 170.32, Art. 7"


class bund_hat_rueckgriff_auf_beamten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Dem Bund steht der Rückgriff auf den Beamten zu (Art. 7 VG)"
    reference = "SR 170.32, Art. 7"

    def formula(person, period, parameters):
        ersatz_geleistet = person('bund_hat_ersatz_geleistet', period)
        vorsatz = person('beamter_hat_vorsaetzlich_gehandelt', period)
        grob_fahrlaessig = person('beamter_hat_grobfahrlaessig_gehandelt', period)
        return ersatz_geleistet * (vorsatz + grob_fahrlaessig > 0)
