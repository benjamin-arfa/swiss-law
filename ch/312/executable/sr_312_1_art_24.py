"""SR 312.1 Art. 24

Generated from: ch/312/de/312.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class freiheitsentzug_ueber_1_monat_droht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Droht dem Jugendlichen ein Freiheitsentzug von mehr als einem Monat"
    reference = "SR 312.1 Art. 24 lit. a"


class haft_ueber_24_stunden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat die Untersuchungs- oder Sicherheitshaft mehr als 24 Stunden gedauert"
    reference = "SR 312.1 Art. 24 lit. c"


class notwendige_verteidigung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Muss der Jugendliche verteidigt werden (notwendige Verteidigung)"
    reference = "SR 312.1 Art. 24"

    def formula(person, period, parameters):
        freiheitsentzug = person('freiheitsentzug_ueber_1_monat_droht', period)
        unterbringung = person('unterbringung_droht', period)
        haft = person('haft_ueber_24_stunden', period)
        # Also conditions b, d, e exist but are qualitative assessments
        return freiheitsentzug + unterbringung + haft > 0
