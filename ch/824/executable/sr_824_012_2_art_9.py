"""SR 824.012.2 Art. 9

Generated from: ch/824/de/824.012.2.md

Notwendige besondere Arbeitskleider und Schuhe: Compensation for special
work clothing. CHF 60 per 26 service days, max CHF 240 per deployment.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class zdv_wbf_besondere_arbeitskleider_noetig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob im Einsatz besondere Arbeitskleider oder Schuhe notwendig sind"
    reference = "SR 824.012.2 Art. 9"
    default_value = False


class zdv_wbf_anrechenbare_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl anrechenbare Tage im Einsatz"
    reference = "SR 824.012.2 Art. 9"
    default_value = 0


class zdv_wbf_verguetung_arbeitskleider(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Verguetung fuer besondere Arbeitskleider und Schuhe (CHF)"
    reference = "SR 824.012.2 Art. 9"

    def formula(person, period, parameters):
        import numpy as np
        noetig = person('zdv_wbf_besondere_arbeitskleider_noetig', period)
        tage = person('zdv_wbf_anrechenbare_tage', period)

        p = parameters(period).sr_824_012_2
        betrag_pro_26_tage = p.arbeitskleider_betrag_pro_26_tage
        max_betrag = p.arbeitskleider_max_pro_einsatz

        # CHF 60 pro 26 anrechenbare Tage
        perioden = (tage / 26).astype(int)
        verguetung = perioden * betrag_pro_26_tage
        verguetung = np.minimum(verguetung, max_betrag)

        return np.where(noetig, verguetung, 0)
