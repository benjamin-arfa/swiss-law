"""SR 170.512 Art. 14

Generated from: ch/170/de/170.512.md

Sprachen der veröffentlichten Texte: Gleichzeitig in DE, FR, IT.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class erlass_ist_bundesgesetz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Text ist ein Erlass (Art. 14 Abs. 1 PublG)"
    reference = "SR 170.512, Art. 14 Abs. 1"


class erlass_in_drei_amtssprachen_verbindlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die drei Sprachfassungen des Erlasses sind in gleicher Weise verbindlich (Art. 14 Abs. 1 PublG)"
    reference = "SR 170.512, Art. 14 Abs. 1"

    def formula(person, period, parameters):
        return person('erlass_ist_bundesgesetz', period)
