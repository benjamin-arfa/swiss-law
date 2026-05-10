"""SR 312.1 Art. 34

Generated from: ch/312/de/312.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class unterbringung_droht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Droht dem Jugendlichen eine Unterbringung"
    reference = "SR 312.1 Art. 34 Abs. 1 lit. a"


class busse_ueber_1000(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Droht eine Busse von mehr als 1000 Franken"
    reference = "SR 312.1 Art. 34 Abs. 1 lit. b"


class freiheitsentzug_ueber_3_monate(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Droht ein Freiheitsentzug von mehr als 3 Monaten"
    reference = "SR 312.1 Art. 34 Abs. 1 lit. c"


class jugendgericht_zustaendig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist das Jugendgericht als erste Instanz zustaendig"
    reference = "SR 312.1 Art. 34 Abs. 1"

    def formula(person, period, parameters):
        unterbringung = person('unterbringung_droht', period)
        busse = person('busse_ueber_1000', period)
        freiheitsentzug = person('freiheitsentzug_ueber_3_monate', period)
        return unterbringung + busse + freiheitsentzug > 0
