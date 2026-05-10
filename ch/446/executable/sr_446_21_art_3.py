"""SR 446.21 Art. 3

Generated from: ch/446/de/446.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alle_taetigkeitsarten_vertreten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Alle Arten der Taetigkeiten nach Art. 5 Bst. a JSFVG sind vertreten"
    reference = "SR 446.21 Art. 3 Abs. 1 Bst. a"


class jede_taetigkeitsart_mehrheitlich_vertreten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Jede Art Taetigkeit ist durch die Mehrheit ihrer Akteurinnen vertreten"
    reference = "SR 446.21 Art. 3 Abs. 1 Bst. b"


class sprachregionen_angemessen_vertreten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sprachregionen sind angemessen vertreten"
    reference = "SR 446.21 Art. 3 Abs. 1 Bst. c"


class branchenorganisation_repraesentativ_jsfvv(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Branchenorganisation gilt als repraesentativ zusammengesetzt nach JSFVV"
    reference = "SR 446.21 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        taetigkeiten = person('alle_taetigkeitsarten_vertreten', period)
        mehrheit = person('jede_taetigkeitsart_mehrheitlich_vertreten', period)
        sprachen = person('sprachregionen_angemessen_vertreten', period)
        return taetigkeiten * mehrheit * sprachen
