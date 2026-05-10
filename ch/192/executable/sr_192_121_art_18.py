"""SR 192.121 Art. 18

Generated from: ch/192/de/192.121.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_schweizer_oder_wohnsitz_schweiz_bei_anstellung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person hat Schweizer Buergerrecht oder hatte bei Anstellung Wohnsitz in der Schweiz"
    reference = "SR 192.121 Art. 18"

class ist_mitglied_diplomatische_mission(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist Mitglied einer diplomatischen Mission, konsularischen Posten oder staendigen Mission"
    reference = "SR 192.121 Art. 18"

class untersteht_schweizer_arbeitsrecht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person untersteht dem Schweizer Arbeitsrecht (Art. 18 Abs. 2-3)"
    reference = "SR 192.121 Art. 18"

    def formula(person, period, parameters):
        ist_mitglied = person('ist_mitglied_diplomatische_mission', period)
        schweizer_wohnsitz = person('ist_schweizer_oder_wohnsitz_schweiz_bei_anstellung', period)
        return ist_mitglied * schweizer_wohnsitz
