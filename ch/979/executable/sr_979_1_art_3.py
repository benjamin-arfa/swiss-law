"""SR 979.1 Art. 3

Generated from: ch/979/de/979.1.md

Art. 3 Beitragsleistungen:
1. Financing of Swiss contributions to IBRD, IDA, and IFC is governed by
   Art. 9 of the Federal Act on International Development Cooperation (SR 974.0).
2. The Swiss National Bank provides the financial services related to
   IMF membership. It receives repayments, interest, and indemnities.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bw_beitragsleistung_ibrd_ida_ifc(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Beitragsleistung an IBRD, IDA oder IFC erfolgt"
    reference = "SR 979.1 Art. 3 Abs. 1"


class bw_snb_finanzielle_leistung_iwf(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Schweizerische Nationalbank finanzielle Leistungen fuer den IWF erbringt"
    reference = "SR 979.1 Art. 3 Abs. 2"
