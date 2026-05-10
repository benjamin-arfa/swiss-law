"""SR 131.216.1 Art. 2

Generated from: ch/131/de/131.216.1.md

Territorial composition: The canton comprises the seven municipalities
Sarnen, Kerns, Sachseln, Alpnach, Giswil, Lungern and Engelberg.
Sarnen is the capital of the canton and seat of the cantonal authorities.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class gemeinde_in_obwalden(Variable):
    value_type = Enum
    possible_values = [
        'sarnen',
        'kerns',
        'sachseln',
        'alpnach',
        'giswil',
        'lungern',
        'engelberg',
        'andere'
    ]
    default_value = 'andere'
    entity_key = 'person'
    definition_period = YEAR
    label = "Die Gemeinde in Obwalden, in der sich die Person befindet"
    reference = "SR 131.216.1 Art. 2"


class in_obwalden_gemeinde(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob sich die Person in einer der sieben Obwaldner Gemeinden befindet"
    reference = "SR 131.216.1 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        gemeinde = person('gemeinde_in_obwalden', period)
        return gemeinde != 'andere'


class in_sarnen_hauptort(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob sich die Person in Sarnen, dem Hauptort des Kantons, befindet"
    reference = "SR 131.216.1 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        gemeinde = person('gemeinde_in_obwalden', period)
        return gemeinde == 'sarnen'


class zugang_zu_kantonsbehörden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Zugang zu den Kantonsbehörden in Sarnen hat"
    reference = "SR 131.216.1 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        return person('in_sarnen_hauptort', period)