"""SR 501.31 Art. 11 - Geschaeftsstelle KSD

Generated from: ch/501/de/501.31.md

Das BABS fuehrt die Geschaeftsstelle KSD.
Die Geschaeftsstelle KSD fuehrt das Sekretariat der Leitungskonferenz KSD,
des SANKO und der Fachgruppen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class geschaeftsstelle_ksd_durch_babs(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das BABS die Geschaeftsstelle KSD fuehrt"
    reference = "SR 501.31 Art. 11 Abs. 1"

    def formula(person, period, parameters):
        return True


class geschaeftsstelle_fuehrt_sekretariat(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Geschaeftsstelle KSD das Sekretariat der Leitungskonferenz KSD, des SANKO und der Fachgruppen fuehrt"
    reference = "SR 501.31 Art. 11 Abs. 2"

    def formula(person, period, parameters):
        return True
