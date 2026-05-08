"""SR 823.113 Art. 3

Generated from: ch/823/de/823.113.md

Vermittlungsprovision zu Lasten von Stellensuchenden:
- Höchstens 5% des ersten Brutto-Jahreslohnes
- Bei Zusammenarbeit mehrerer Vermittler: keine Kumulierung (Ausnahme Art. 4 Abs. 4)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class erster_brutto_jahreslohn(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Erster Brutto-Jahreslohn aus der vermittelten Stelle"
    reference = "SR 823.113 Art. 3 Abs. 1"


class vermittlungsprovision_stellensuchende(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Vermittlungsprovision zu Lasten von Stellensuchenden"
    reference = "SR 823.113 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        import numpy as np
        lohn = person('erster_brutto_jahreslohn', period)
        max_satz = parameters(period).sr_823_113.vermittlungsprovision_max_prozent
        return lohn * max_satz
