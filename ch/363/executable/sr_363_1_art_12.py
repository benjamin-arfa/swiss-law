"""SR 363.1 Art. 12

Generated from: ch/363/de/363.1.md

Meldung von Loeschungsereignissen: Frist 30 Tage nach Eintritt des
Loeschungsereignisses.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class loeschungsereignis_eingetreten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesetzliche Voraussetzung fuer die Loeschung eines DNA-Profils ist eingetreten"
    reference = "SR 363.1 Art. 12 Abs. 1"


class tage_seit_loeschungsereignis(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Tage seit Eintritt des fuer die Loeschung massgeblichen Ereignisses"
    reference = "SR 363.1 Art. 12 Abs. 2"


class loeschungsmeldung_faellig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Meldung des Loeschungsereignisses an fedpol ist faellig (innert 30 Tagen)"
    reference = "SR 363.1 Art. 12 Abs. 2"

    def formula(person, period, parameters):
        eingetreten = person('loeschungsereignis_eingetreten', period)
        tage = person('tage_seit_loeschungsereignis', period)
        return eingetreten * (tage <= 30)
