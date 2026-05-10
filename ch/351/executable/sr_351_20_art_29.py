"""SR 351.20 Art. 29

Generated from: ch/351/de/351.20.md
Conditions for enforcing international court sentences in Switzerland.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class verurteilter_hat_aufenthalt_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verurteilter hat in der Schweiz seinen gewoehnlichen Aufenthalt"
    reference = "SR 351.20 Art. 29 Abs. 1 lit. a"


class tat_in_schweiz_strafbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die verurteilte Tat waere bei Begehung in der Schweiz strafbar"
    reference = "SR 351.20 Art. 29 Abs. 1 lit. b"


class verurteilter_ist_schweizer_staatsangehoeriger(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verurteilter ist schweizerischer Staatsangehoeriger"
    reference = "SR 351.20 Art. 29 Abs. 2"


class verurteilter_verlangt_vollstreckung_in_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verurteilter verlangt die Vollstreckung in der Schweiz"
    reference = "SR 351.20 Art. 29 Abs. 2"


class vollstreckung_in_schweiz_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vollstreckung des Entscheids des Internationalen Gerichts in der Schweiz ist zulaessig"
    reference = "SR 351.20 Art. 29"

    def formula(person, period):
        aufenthalt = person('verurteilter_hat_aufenthalt_schweiz', period)
        strafbar = person('tat_in_schweiz_strafbar', period)
        schweizer = person('verurteilter_ist_schweizer_staatsangehoeriger', period)
        verlangt = person('verurteilter_verlangt_vollstreckung_in_schweiz', period)

        # Abs. 1: Aufenthalt in CH + Tat waere in CH strafbar
        abs_1 = aufenthalt * strafbar

        # Abs. 2: Schweizer + verlangt es
        abs_2 = schweizer * verlangt

        return abs_1 + abs_2
