"""SR 128.1 Art. 9

Generated from: ch/128/de/128.1.md

Bewilligung und Verzeichnung von Ausnahmen: If an administrative unit
cannot comply with a binding directive, it needs an exception permit
from the issuing authority.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kann_vorgabe_nicht_erfuellen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Verwaltungseinheit eine verbindliche Vorgabe nicht erfuellen kann"
    reference = "SR 128.1 Art. 9 Abs. 1"


class ausnahmebewilligung_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Ausnahmebewilligung erforderlich ist"
    reference = "SR 128.1 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        return person('kann_vorgabe_nicht_erfuellen', period)
