"""SR 661.1 Art. 1

Generated from: ch/661/de/661.1.md

Art. 1 Ersatzbefreiung wegen erheblicher Behinderung (Exemption for significant disability):
1. [Repealed]
2. For exemption under Art. 4 Abs. 1 Bst. abis WPEG when receiving accident
   insurance pensions or helplessness allowances, the same minimum degree of
   invalidity or helplessness applies as for IV pensions/allowances.
3. Assessment of exemption for unfit-for-service persons follows IV administrative
   guidelines for helplessness allowances through cantonal IV offices.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class wpev_bezug_uv_rente(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the person receives accident insurance pension or helplessness allowance"
    reference = "SR 661.1 Art. 1 Abs. 2"


class wpev_iv_mindestgrad_erreicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the minimum IV invalidity/helplessness degree is met"
    reference = "SR 661.1 Art. 1 Abs. 2"


class wpev_ersatzbefreiung_behinderung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the person is exempt from the substitute levy due to significant disability"
    reference = "SR 661.1 Art. 1 Abs. 2"

    def formula(person, period, parameters):
        bezug_uv = person('wpev_bezug_uv_rente', period)
        mindestgrad = person('wpev_iv_mindestgrad_erreicht', period)
        return bezug_uv * mindestgrad
