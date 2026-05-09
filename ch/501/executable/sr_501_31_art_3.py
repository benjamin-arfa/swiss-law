"""SR 501.31 Art. 3 - Leitung des KSD

Generated from: ch/501/de/501.31.md

Die Leitung des KSD obliegt dem Bundesamt fuer Bevoelkerungsschutz (BABS).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ksd_leitung_durch_babs(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Leitung des KSD dem BABS obliegt"
    reference = "SR 501.31 Art. 3"

    def formula(person, period, parameters):
        return True
