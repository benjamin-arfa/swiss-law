"""SR 364.3 Art. 24

Generated from: ch/364/de/364.3.md

Besondere Bestimmungen fuer den Transport von Kindern und Frauen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class transportierte_person_ist_kind(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Transportierte Person ist ein Kind"
    reference = "SR 364.3 Art. 24 Abs. 1"


class transportierte_person_ist_frau(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Transportierte Person ist eine Frau"
    reference = "SR 364.3 Art. 24 Abs. 2"


class weibliche_begleitung_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Weibliche Begleitung ist nach Moeglichkeit erforderlich"
    reference = "SR 364.3 Art. 24 Abs. 2"

    def formula(person, period, parameters):
        return person('transportierte_person_ist_frau', period)
