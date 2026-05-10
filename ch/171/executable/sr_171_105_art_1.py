"""SR 171.105 Art. 1

Generated from: ch/171/de/171.105.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class amtsdauer_praesidentin_redaktionskommission(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Amtsdauer der Präsidentin oder des Präsidenten der Redaktionskommission in Jahren"
    reference = "SR 171.105 Art. 1 Abs. 2"

    def formula(person, period, parameters):
        return 2


class wiederwahl_praesidentin_redaktionskommission_moeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wiederwahl der Präsidentin oder des Präsidenten der Redaktionskommission ist möglich"
    reference = "SR 171.105 Art. 1 Abs. 2"

    def formula(person, period, parameters):
        return True
