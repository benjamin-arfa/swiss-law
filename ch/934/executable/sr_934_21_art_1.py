"""SR 934.21 Art. 1

Generated from: ch/934/de/934.21.md

Art. 1 Ruestungsunternehmen:
1. To ensure army equipment (where not cantonal responsibility), the
   Confederation may operate armament enterprises, establish private-law
   corporations, or hold shares in them.
2. The Federal Council is authorized to establish corporations in the name
   of the Confederation, acquire and dispose of shares. It regulates the details.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bgrb_ruestungsunternehmen_betrieben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Bund Ruestungsunternehmen betreibt"
    reference = "SR 934.21 Art. 1 Abs. 1"


class bgrb_beteiligung_an_ag(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Bund Beteiligungen an privatrechtlichen Aktiengesellschaften haelt"
    reference = "SR 934.21 Art. 1 Abs. 1"
