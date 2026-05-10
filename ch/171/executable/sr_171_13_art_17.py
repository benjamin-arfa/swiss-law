"""SR 171.13 Art. 17

Generated from: ch/171/de/171.13.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class amtsdauer_staendige_kommission_mitglieder(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Amtsdauer der Mitglieder der ständigen Kommissionen in Jahren"
    reference = "SR 171.13 Art. 17 Abs. 1"

    def formula(person, period, parameters):
        return 4


class amtsdauer_kommission_praesidium(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Amtsdauer der Präsidenten und Vizepräsidenten der ständigen Kommissionen in Jahren"
    reference = "SR 171.13 Art. 17 Abs. 2"

    def formula(person, period, parameters):
        return 2


class wiederwahl_kommission_praesidium_moeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Direkte Wiederwahl in dasselbe Amt des Kommissionspräsidiums ist nicht möglich"
    reference = "SR 171.13 Art. 17 Abs. 2"

    def formula(person, period, parameters):
        return False
