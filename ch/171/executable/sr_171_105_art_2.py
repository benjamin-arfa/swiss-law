"""SR 171.105 Art. 2

Generated from: ch/171/de/171.105.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_nationalraete_pro_subkommission(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Mitglieder des Nationalrates pro Subkommission der Redaktionskommission"
    reference = "SR 171.105 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        return 2


class anzahl_staenderaete_pro_subkommission(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Mitglieder des Ständerates pro Subkommission der Redaktionskommission"
    reference = "SR 171.105 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        return 2


class anzahl_stellvertreter_pro_subkommission(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Stellvertreterinnen oder Stellvertreter pro Subkommission"
    reference = "SR 171.105 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        return 2


class amtsdauer_praesidentin_subkommission(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Amtsdauer der Präsidentin oder des Präsidenten der Subkommission in Jahren"
    reference = "SR 171.105 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        return 2
