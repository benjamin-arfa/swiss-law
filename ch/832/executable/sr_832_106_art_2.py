"""SR 832.106 Art. 2

Generated from: ch/832/de/832.106.md

Maximum premium differentials between regions within the same canton:
- Between Region 1 and Region 2: max 15%
- Between Region 2 and Region 3: max 10%

Applies to ordinary insurance with accident coverage (ordentliche Versicherung
mit Unfalldeckung).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR


class kvg_praemie_region_1(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "KVG-Prämie in Region 1 (CHF)"
    reference = "SR 832.106 Art. 2"


class kvg_praemie_region_2(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "KVG-Prämie in Region 2 (CHF)"
    reference = "SR 832.106 Art. 2"


class kvg_praemie_region_3(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "KVG-Prämie in Region 3 (CHF)"
    reference = "SR 832.106 Art. 2"


class kvg_praemie_regionale_differenz_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Sind die regionalen Prämienabstufungen innerhalb der gesetzlichen Grenzen?"
    reference = "SR 832.106 Art. 2"

    def formula_2016(person, period, parameters):
        import numpy as np

        praemie_r1 = person('kvg_praemie_region_1', period)
        praemie_r2 = person('kvg_praemie_region_2', period)
        praemie_r3 = person('kvg_praemie_region_3', period)

        p = parameters(period).sr832_106
        max_diff_r1_r2 = p.max_differenz_region_1_2
        max_diff_r2_r3 = p.max_differenz_region_2_3

        # Check Region 1 vs Region 2 differential
        diff_r1_r2 = np.where(
            praemie_r2 > 0,
            np.abs(praemie_r1 - praemie_r2) / praemie_r2,
            0.0
        )

        # Check Region 2 vs Region 3 differential
        diff_r2_r3 = np.where(
            praemie_r3 > 0,
            np.abs(praemie_r2 - praemie_r3) / praemie_r3,
            0.0
        )

        return (diff_r1_r2 <= max_diff_r1_r2) * (diff_r2_r3 <= max_diff_r2_r3)
