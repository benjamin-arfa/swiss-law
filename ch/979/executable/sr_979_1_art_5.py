"""SR 979.1 Art. 5

Generated from: ch/979/de/979.1.md

Art. 5 Kredite des IWF, Sonderziehungsrechte, Hinterlegungsstelle:
1. The SNB receives credits allocated to Switzerland by the IMF.
   It handles repayment and interest service.
2. The SNB handles SDR (Special Drawing Rights) operations on its own account.
3. The SNB is the depository for the IMF's Swiss franc holdings.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bw_snb_iwf_kredit_empfangen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die SNB Kredite des IWF fuer die Schweiz uebernimmt"
    reference = "SR 979.1 Art. 5 Abs. 1"


class bw_snb_szr_operationen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die SNB Operationen in Sonderziehungsrechten abwickelt"
    reference = "SR 979.1 Art. 5 Abs. 2"


class bw_snb_hinterlegungsstelle(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die SNB Hinterlegungsstelle des IWF fuer Schweizerfrankbestaende ist"
    reference = "SR 979.1 Art. 5 Abs. 3"

    def formula(person, period, parameters):
        # The SNB is always the depository (statutory role)
        return True
