"""SR 446.11 Art. 1

Generated from: ch/446/de/446.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_deutschsprachige_kantone(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl deutschsprachige Kantone in denen die Organisation taetig ist"
    reference = "SR 446.11 Art. 1 Bst. a"


class anzahl_franzoesischsprachige_kantone(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl franzoesischsprachige Kantone in denen die Organisation taetig ist"
    reference = "SR 446.11 Art. 1 Bst. a"


class taetig_italienischsprachige_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Taetigkeit in der italienischsprachigen Schweiz"
    reference = "SR 446.11 Art. 1 Bst. a"


class taetig_raetoromanische_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Taetigkeit in der raetoromanischen Schweiz"
    reference = "SR 446.11 Art. 1 Bst. a"


class taetigkeit_auf_sprachregionaler_ebene(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Taetigkeit auf sprachregionaler Ebene (Art. 5 Bst. c Ziff. 1 KJFG)"
    reference = "SR 446.11 Art. 1 Bst. a"

    def formula(person, period, parameters):
        de_kantone = person('anzahl_deutschsprachige_kantone', period)
        fr_kantone = person('anzahl_franzoesischsprachige_kantone', period)
        it = person('taetig_italienischsprachige_schweiz', period)
        rm = person('taetig_raetoromanische_schweiz', period)
        return (de_kantone >= 10) + (fr_kantone >= 3) + it + rm >= 1
