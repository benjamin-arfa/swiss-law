"""SR 732.1 Art. 12

Generated from: ch/732/de/732.1.md

Rahmenbewilligung: Wer eine Kernanlage bauen oder betreiben will,
braucht eine Rahmenbewilligung des Bundesrates. Kein Rechtsanspruch.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class will_kernanlage_bauen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person eine Kernanlage bauen will"
    reference = "SR 732.1 Art. 12 Abs. 1"


class will_kernanlage_betreiben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person eine Kernanlage betreiben will"
    reference = "SR 732.1 Art. 12 Abs. 1"


class rahmenbewilligung_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Rahmenbewilligung des Bundesrates erforderlich ist"
    reference = "SR 732.1 Art. 12"

    def formula(person, period, parameters):
        bauen = person('will_kernanlage_bauen', period)
        betreiben = person('will_kernanlage_betreiben', period)

        return bauen + betreiben > 0
