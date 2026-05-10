"""SR 824.012.2 Art. 11

Generated from: ch/824/de/824.012.2.md

Taeglicher Arbeitsweg: Mileage compensation for use of private vehicle
for the daily commute. CHF 0.65 per kilometre.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class zdv_wbf_privat_km_pro_tag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Unumgaengliche Kilometer mit Privatfahrzeug pro Tag (Arbeitsweg)"
    reference = "SR 824.012.2 Art. 11"
    default_value = 0.0


class zdv_wbf_kilometerentschaedigung_pro_tag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kilometerentschaedigung fuer taeglichen Arbeitsweg (CHF pro Tag)"
    reference = "SR 824.012.2 Art. 11"

    def formula(person, period, parameters):
        km = person('zdv_wbf_privat_km_pro_tag', period)
        p = parameters(period).sr_824_012_2
        return km * p.kilometerentschaedigung_ansatz
