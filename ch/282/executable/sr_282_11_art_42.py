"""SR 282.11 Art. 42 - Beendigung der Beiratschaft

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class beiratschaft_frist_abgelaufen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Frist fuer die Beiratschaft ist abgelaufen"
    reference = "SR 282.11 Art. 42 Abs. 1"


class finanzielles_gleichgewicht_gewaehrleistet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Wiederherstellung des finanziellen Gleichgewichts erscheint gewaehrleistet"
    reference = "SR 282.11 Art. 42 Abs. 2"


class beiratschaft_faellt_dahin(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Beiratschaft faellt dahin oder wird aufgehoben"
    reference = "SR 282.11 Art. 42"

    def formula(self, period, parameters):
        abgelaufen = self('beiratschaft_frist_abgelaufen', period)
        gleichgewicht = self('finanzielles_gleichgewicht_gewaehrleistet', period)
        return abgelaufen + gleichgewicht > 0
