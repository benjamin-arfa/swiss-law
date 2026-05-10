"""SR 364.3 Art. 17

Generated from: ch/364/de/364.3.md

Transportprotokoll: Erforderlich bei Transport laenger als 4 Stunden
oder besonderen Vorkommnissen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class transportdauer_stunden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Dauer des Transports in Stunden"
    reference = "SR 364.3 Art. 17"


class besondere_vorkommnisse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Besondere Vorkommnisse waehrend des Transports"
    reference = "SR 364.3 Art. 17"


class transportprotokoll_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Transportprotokoll ist zu erstellen"
    reference = "SR 364.3 Art. 17"

    def formula(person, period, parameters):
        dauer = person('transportdauer_stunden', period)
        vorkommnisse = person('besondere_vorkommnisse', period)
        return (dauer > 4) + vorkommnisse
