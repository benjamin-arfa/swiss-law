"""SR 432.21 Art. 3

Generated from: ch/432/de/432.21.md

Sammelauftrag - Kriterien fuer zu sammelnde Informationen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class erscheint_in_der_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Information erscheint in der Schweiz"
    reference = "SR 432.21 Art. 3 Abs. 1 Bst. a"


class bezieht_sich_auf_schweiz_oder_schweizer(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bezieht sich auf die Schweiz oder auf Personen mit schweizerischem Buergerrecht oder Wohnsitz"
    reference = "SR 432.21 Art. 3 Abs. 1 Bst. b"


class von_schweizerischen_autoren_geschaffen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Von schweizerischen oder mit der Schweiz verbundenen Autoren geschaffen oder mitgestaltet"
    reference = "SR 432.21 Art. 3 Abs. 1 Bst. c"


class faellt_unter_sammelauftrag(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Information faellt unter den Sammelauftrag der Nationalbibliothek"
    reference = "SR 432.21 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        return (
            person('erscheint_in_der_schweiz', period) +
            person('bezieht_sich_auf_schweiz_oder_schweizer', period) +
            person('von_schweizerischen_autoren_geschaffen', period)
        )
