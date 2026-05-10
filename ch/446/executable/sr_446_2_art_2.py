"""SR 446.2 Art. 2

Generated from: ch/446/de/446.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_akteurin_film_videospiele(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Akteurin in den Bereichen Film und Videospiele im Rahmen wirtschaftlicher Taetigkeit"
    reference = "SR 446.2 Art. 2 Abs. 1 Bst. a"


class ist_anbieterin_plattformdienst(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Anbieterin von Plattformdiensten im Rahmen wirtschaftlicher Taetigkeit"
    reference = "SR 446.2 Art. 2 Abs. 1 Bst. b"


class ist_anbieterin_geldspiele(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Anbieterin von Geldspielen (Geldspielgesetz SR 935.51)"
    reference = "SR 446.2 Art. 2 Abs. 2"


class jsfvg_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "JSFVG ist auf die Person anwendbar"
    reference = "SR 446.2 Art. 2"

    def formula(person, period, parameters):
        akteurin = person('ist_akteurin_film_videospiele', period)
        plattform = person('ist_anbieterin_plattformdienst', period)
        geldspiele = person('ist_anbieterin_geldspiele', period)
        return (akteurin + plattform >= 1) * not_(geldspiele)
