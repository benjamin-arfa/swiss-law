"""SR 837.21 Art. 4 - Vermoegensschwelle: Vorsorgeguthaben (Asset threshold: pension assets)

Pension assets from occupational pensions (BVG) are included in net assets
for the threshold calculation only to the extent they exceed 26 times the
general living expenses per Art. 9(1)(a)(1) UeLG.

Generated from: ch/837/de/837.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class uelv_vorsorgeguthaben_bvg(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Vorsorgeguthaben aus beruflicher Vorsorge in CHF (Art. 4 UeLV)"
    reference = "SR 837.21 Art. 4"


class uelv_allgemeiner_lebensbedarf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Allgemeiner Lebensbedarf nach Art. 9 Abs. 1 Bst. a Ziff. 1 UeLG in CHF"
    reference = "SR 837.21 Art. 4"


class uelv_vorsorgeguthaben_anrechenbar(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anrechenbares Vorsorgeguthaben fuer Vermoegensschwelle in CHF (Art. 4 UeLV)"
    reference = "SR 837.21 Art. 4"

    def formula(person, period, parameters):
        guthaben = person('uelv_vorsorgeguthaben_bvg', period)
        lebensbedarf = person('uelv_allgemeiner_lebensbedarf', period)
        freibetrag = 26 * lebensbedarf
        return max_(guthaben - freibetrag, 0)
