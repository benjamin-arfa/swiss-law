"""SR 150.2 Art. 6

Generated from: ch/150/de/150.2.md

Suche im Netzwerk: Die Koordinationsstelle loest eine Suche aus, wenn
Anhaltspunkte bestehen, dass sich die gesuchte Person in einem
Freiheitsentzug befindet.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class anhaltspunkte_freiheitsentzug(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Anhaltspunkte bestehen, dass sich die Person in einem Freiheitsentzug befindet"
    reference = "SR 150.2 Art. 6 Abs. 1"


class netzwerksuche_wird_ausgeloest(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Suche im Netzwerk ausgeloest wird"
    reference = "SR 150.2 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        return person('anhaltspunkte_freiheitsentzug', period)
