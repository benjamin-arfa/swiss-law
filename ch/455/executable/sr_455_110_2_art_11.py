"""SR 455.110.2 Art. 11

Generated from: ch/455/de/455.110.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class elektrotreiber_stromstoss_dauer_sekunden(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximale Dauer eines Stromstosses des Elektrotreibers in Sekunden"
    reference = "SR 455.110.2 Art. 11 Abs. 1"


class tier_ist_schwein_oder_rind(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tier ist ein gesundes, unverletztes und gehfaehiges Schwein oder Rind"
    reference = "SR 455.110.2 Art. 11 Abs. 2"


class elektrotreiber_stromstoss_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Stromstossdauer des Elektrotreibers konform (max 1 Sekunde) nach Art. 11 Abs. 1 SR 455.110.2"
    reference = "SR 455.110.2 Art. 11 Abs. 1"

    def formula(person, period, parameters):
        return person('elektrotreiber_stromstoss_dauer_sekunden', period) <= 1.0


class elektrotreiber_einsatz_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Einsatz des Elektrotreibers ist zulaessig nach Art. 11 SR 455.110.2"
    reference = "SR 455.110.2 Art. 11"

    def formula(person, period, parameters):
        stromstoss_ok = person('elektrotreiber_stromstoss_konform', period)
        richtiges_tier = person('tier_ist_schwein_oder_rind', period)
        return stromstoss_ok * richtiges_tier
