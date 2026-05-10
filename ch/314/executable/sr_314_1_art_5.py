"""SR 314.1 Art. 5

Generated from: ch/314/de/314.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_ordnungsbussen(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl gleichzeitig verwirkter Ordnungsbussentatbestaende"
    reference = "SR 314.1 Art. 5"


class einzelbussen_summe(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Summe der einzelnen Bussenbetraege (Gesamtbusse bei Konkurrenz)"
    reference = "SR 314.1 Art. 5 Abs. 1"


class ordentliches_strafverfahren_wegen_gesamtbusse(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Gesamtbusse uebersteigt 600 Franken, daher ordentliches Strafverfahren"
    reference = "SR 314.1 Art. 5 Abs. 2"

    def formula(person, period, parameters):
        gesamtbusse = person('einzelbussen_summe', period)
        return gesamtbusse > 600
