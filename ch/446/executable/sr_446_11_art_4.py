"""SR 446.11 Art. 4

Generated from: ch/446/de/446.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class tatsaechliche_kosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Tatsaechliche Kosten durch statutarische Taetigkeiten oder Projektdurchfuehrung"
    reference = "SR 446.11 Art. 4 Abs. 1"


class ausserordentliche_investitionen(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Ausgaben fuer ausserordentliche Investitionen"
    reference = "SR 446.11 Art. 4 Abs. 2"


class selbstverschuldete_kosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Selbstverschuldete Kosten (Abfindungen, Bussen, Schuldentilgung)"
    reference = "SR 446.11 Art. 4 Abs. 2"


class anrechenbare_ausgaben_kjfv(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anrechenbare Ausgaben nach Art. 13 KJFG"
    reference = "SR 446.11 Art. 4"

    def formula(person, period, parameters):
        kosten = person('tatsaechliche_kosten', period)
        investitionen = person('ausserordentliche_investitionen', period)
        selbstverschuldet = person('selbstverschuldete_kosten', period)
        return max_(kosten - investitionen - selbstverschuldet, 0)
