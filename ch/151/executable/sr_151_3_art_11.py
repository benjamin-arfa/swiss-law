"""SR 151.3 Art. 11

Generated from: ch/151/de/151.3.md

Verhaeltnismaessigkeit: Entschaedigung bei Diskriminierung hoechstens CHF 5000.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class max_entschaedigung_diskriminierung_behig(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Entschaedigung bei Diskriminierung nach BehiG Art. 8 Abs. 3 (CHF 5000)"
    reference = "SR 151.3 Art. 11 Abs. 2"

    def formula(person, period, parameters):
        return 5000.0
