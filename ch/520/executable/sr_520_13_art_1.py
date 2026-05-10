"""SR 520.13 Art. 1

Generated from: ch/520/de/520.13.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_mit_wetterdaten_beauftragt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Ist die Stelle mit der Beschaffung, Auswertung und Verbreitung von Wetterdaten beauftragt"
    reference = "SR 520.13 Art. 1"

    def formula(person, period, parameters):
        return person('ist_zivile_stelle_wetterdienst', period) + person('ist_militaerische_stelle_wetterdienst', period)


class ist_zivile_stelle_wetterdienst(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Ist eine zivile Stelle des Bundes im Wetterdienst"
    reference = "SR 520.13 Art. 1"


class ist_militaerische_stelle_wetterdienst(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Ist eine militaerische Stelle des Bundes im Wetterdienst"
    reference = "SR 520.13 Art. 1"


class zusammenarbeitspflicht_wetterdienst(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Pflicht zur Zusammenarbeit im Wetterdienst"
    reference = "SR 520.13 Art. 1"

    def formula(person, period, parameters):
        return person('ist_mit_wetterdaten_beauftragt', period)
