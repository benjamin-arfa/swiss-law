"""SR 837.21 Art. 11 - Pauschale fuer Nebenkosten (Ancillary costs flat rate)

For persons living in their own property, ancillary costs are recognized
exclusively as a flat rate of CHF 3480 per year (as of 2025).
Also applies to persons with usufruct or right of residence.

Generated from: ch/837/de/837.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class uelv_bewohnt_eigene_liegenschaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person bewohnt eigene Liegenschaft (Art. 11 Abs. 1 UeLV)"
    reference = "SR 837.21 Art. 11 Abs. 1"


class uelv_hat_nutzniessung_oder_wohnrecht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person hat Nutzniessung oder Wohnrecht an bewohnter Liegenschaft (Art. 11 Abs. 2 UeLV)"
    reference = "SR 837.21 Art. 11 Abs. 2"


class uelv_nebenkosten_pauschale(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Pauschale fuer Nebenkosten in CHF pro Jahr (Art. 11 Abs. 3 UeLV)"
    reference = "SR 837.21 Art. 11 Abs. 3"

    def formula(person, period, parameters):
        eigene = person('uelv_bewohnt_eigene_liegenschaft', period)
        nutzniessung = person('uelv_hat_nutzniessung_oder_wohnrecht', period)
        berechtigt = eigene + nutzniessung
        # CHF 3480 per year (as of 01.01.2025)
        return berechtigt * 3480
