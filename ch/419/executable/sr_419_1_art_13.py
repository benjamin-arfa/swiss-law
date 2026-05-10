"""SR 419.1 Art. 13

Generated from: ch/419/de/419.1.md

Grundkompetenzen Erwachsener - Definition.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lesen_schreiben_muendlich_landessprache(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verfuegt ueber Lesen, Schreiben und muendliche Ausdruck in Landessprache"
    reference = "SR 419.1 Art. 13 Abs. 1 Bst. a"


class grundkenntnisse_mathematik(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verfuegt ueber Grundkenntnisse der Mathematik"
    reference = "SR 419.1 Art. 13 Abs. 1 Bst. b"


class ikt_anwendung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kann Informations- und Kommunikationstechnologien anwenden"
    reference = "SR 419.1 Art. 13 Abs. 1 Bst. c"


class verfuegt_ueber_grundkompetenzen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verfuegt ueber alle Grundkompetenzen Erwachsener"
    reference = "SR 419.1 Art. 13 Abs. 1"

    def formula(person, period, parameters):
        return (
            person('lesen_schreiben_muendlich_landessprache', period) *
            person('grundkenntnisse_mathematik', period) *
            person('ikt_anwendung', period)
        )
