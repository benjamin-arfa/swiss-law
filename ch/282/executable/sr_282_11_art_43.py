"""SR 282.11 Art. 43 - Fortwirkende Anordnungen und Stundung nach Beiratschaft

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class stundung_nach_beiratschaft_dauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Dauer der Stundung nach Beendigung der Beiratschaft in Jahren"
    reference = "SR 282.11 Art. 43 Abs. 2"


class stundung_nach_beiratschaft_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Stundung nach Beiratschaft ist zulaessig (max 3 Jahre)"
    reference = "SR 282.11 Art. 43 Abs. 2"

    def formula(self, period, parameters):
        dauer = self('stundung_nach_beiratschaft_dauer_jahre', period)
        return dauer <= 3
