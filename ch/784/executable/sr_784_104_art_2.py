"""SR 784.104 Art. 2

Generated from: ch/784/de/784.104.md

Nummerierungspläne und Verwaltungsvorschriften:
- BAKOM erstellt Nummerierungspläne
- Bei wichtigen Änderungen: Benachrichtigung mindestens 24 Monate vorher
  (Nummerierungspläne) bzw. 6 Monate (Verwaltungsvorschriften)
- Inhaberinnen von Nummernblöcken müssen Kunden mind. 6 Monate vorher informieren
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_wichtige_aenderung_nummerierungsplan(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine wichtige Änderung der Nummerierungspläne handelt"
    reference = "SR 784.104 Art. 2 Abs. 3"


class ist_wichtige_aenderung_verwaltungsvorschrift(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine wichtige Änderung der Verwaltungsvorschriften handelt"
    reference = "SR 784.104 Art. 2 Abs. 3"


class vorlaufzeit_benachrichtigung_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Erforderliche Vorlaufzeit in Monaten für die Benachrichtigung"
    reference = "SR 784.104 Art. 2 Abs. 3"

    def formula(person, period, parameters):
        import numpy as np
        np_aend = person('ist_wichtige_aenderung_nummerierungsplan', period)
        vv_aend = person('ist_wichtige_aenderung_verwaltungsvorschrift', period)
        min_np = parameters(period).sr_784_104.vorlaufzeit_nummerierungsplan_monate
        min_vv = parameters(period).sr_784_104.vorlaufzeit_verwaltungsvorschrift_monate

        return np.where(np_aend, min_np, np.where(vv_aend, min_vv, 0))
