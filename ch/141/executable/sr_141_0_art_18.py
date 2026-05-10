"""SR 141.0 Art. 18 - Kantonale und kommunale Aufenthaltsdauer

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kantonale_mindestaufenthaltsdauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Kantonale Mindestaufenthaltsdauer in Jahren (zwischen 2 und 5)"
    reference = "SR 141.0 Art. 18 Abs. 1"


class aufenthaltsdauer_im_kanton_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Tatsaechliche Aufenthaltsdauer im Kanton in Jahren"
    reference = "SR 141.0 Art. 18 Abs. 1"


class kantonale_aufenthaltsdauer_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die kantonale Mindestaufenthaltsdauer ist erfuellt"
    reference = "SR 141.0 Art. 18 Abs. 1"

    def formula(self, period, parameters):
        mindest = self('kantonale_mindestaufenthaltsdauer_jahre', period)
        tatsaechlich = self('aufenthaltsdauer_im_kanton_jahre', period)
        return tatsaechlich >= mindest
