"""SR 141.0 Art. 37 - Entlassungsgesuch und -beschluss

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kein_aufenthalt_in_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person hat keinen Aufenthalt in der Schweiz"
    reference = "SR 141.0 Art. 37 Abs. 1"


class besitzt_andere_staatsangehoerigkeit_oder_zusicherung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person besitzt eine andere Staatsangehoerigkeit oder hat eine zugesichert"
    reference = "SR 141.0 Art. 37 Abs. 1"


class anspruch_auf_entlassung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person hat Anspruch auf Entlassung aus dem Schweizer Buergerrecht"
    reference = "SR 141.0 Art. 37 Abs. 1"

    def formula(self, period, parameters):
        kein_aufenthalt = self('kein_aufenthalt_in_schweiz', period)
        andere_staat = self('besitzt_andere_staatsangehoerigkeit_oder_zusicherung', period)
        return kein_aufenthalt * andere_staat
