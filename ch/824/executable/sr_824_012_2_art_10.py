"""SR 824.012.2 Art. 10

Generated from: ch/824/de/824.012.2.md

Verpflegung: Daily meal compensation when the deployment site cannot
provide meals. Breakfast CHF 4, lunch CHF 9, dinner CHF 7.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class zdv_wbf_einsatzbetrieb_verpflegt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Einsatzbetrieb die zivildienstleistende Person verpflegen kann"
    reference = "SR 824.012.2 Art. 10 Abs. 1"
    default_value = True


class zdv_wbf_verpflegungsentschaedigung_pro_tag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Verpflegungsentschaedigung pro anrechenbaren Tag (CHF)"
    reference = "SR 824.012.2 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        import numpy as np
        verpflegt = person('zdv_wbf_einsatzbetrieb_verpflegt', period)
        p = parameters(period).sr_824_012_2

        # Morgenessen 4 + Mittagessen 9 + Nachtessen 7 = 20
        tagesansatz = (
            p.verpflegung_morgenessen +
            p.verpflegung_mittagessen +
            p.verpflegung_nachtessen
        )
        return np.where(verpflegt, 0, tagesansatz)
