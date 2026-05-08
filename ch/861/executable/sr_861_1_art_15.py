"""SR 861.1 Art. 15

Generated from: ch/861/de/861.1.md

Art. 15 Abs. 3: Late submission penalty for financial aid documentation:
- Up to 1 month late: reduction by 1/5
- Each additional month: additional 1/5 reduction
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class kbfhv_verspaetung_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Verspätung der Unterlageneinreichung in Monaten"
    reference = "SR 861.1 Art. 15 Abs. 3"
    default_value = 0


class kbfhv_finanzhilfe_brutto(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Brutto-Finanzhilfe vor allfälliger Kürzung (CHF)"
    reference = "SR 861.1 Art. 15 Abs. 3"


class kbfhv_finanzhilfe_nach_kuerzung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Finanzhilfe nach allfälliger Kürzung wegen Verspätung (CHF)"
    reference = "SR 861.1 Art. 15 Abs. 3"

    def formula(person, period, parameters):
        brutto = person('kbfhv_finanzhilfe_brutto', period)
        verspaetung = person('kbfhv_verspaetung_monate', period)

        # Each month late: 1/5 reduction, so 5 months = 100% reduction
        kuerzung_anteil = min_(verspaetung * 0.2, 1.0)
        return brutto * (1 - kuerzung_anteil)
