"""SR 314.1 Art. 10

Generated from: ch/314/de/314.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class wohnsitz_in_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die beschuldigte Person hat Wohnsitz in der Schweiz"
    reference = "SR 314.1 Art. 10"


class hinterlegungspflicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pflicht zur Hinterlegung oder Sicherheitsleistung (kein Wohnsitz in der Schweiz und keine Sofortzahlung)"
    reference = "SR 314.1 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        wohnsitz = person('wohnsitz_in_schweiz', period)
        sofort = person('busse_sofort_bezahlt', period)
        return not_(wohnsitz) * not_(sofort)
