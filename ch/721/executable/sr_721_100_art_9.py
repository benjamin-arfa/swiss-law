"""SR 721.100 Art. 9

Generated from: ch/721/de/721.100.md

Art. 9 - Conditions for granting contributions:
1. Compensations under Art. 6 require measures that:
   a. are based on integral planning
   b. meet legal requirements
   c. show a good cost-benefit ratio
2. Financial aid under Art. 7 requires activities that:
   a. are of national significance
   b. meet legal requirements
   c. are expertly, practically, and cost-effectively executed
3. The Federal Council sets detailed conditions.

Note: This defines qualitative eligibility criteria. Modeled as boolean inputs.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class wbg_massnahme_integrale_planung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the measure is based on integral planning"
    reference = "SR 721.100 Art. 9 Abs. 1 Bst. a"


class wbg_massnahme_gesetzeskonform(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the measure meets legal requirements"
    reference = "SR 721.100 Art. 9 Abs. 1 Bst. b"


class wbg_massnahme_kosten_nutzen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the measure has a good cost-benefit ratio"
    reference = "SR 721.100 Art. 9 Abs. 1 Bst. c"


class wbg_abgeltung_berechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the project meets all conditions for federal compensation (Art. 6)"
    reference = "SR 721.100 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        planung = person('wbg_massnahme_integrale_planung', period)
        gesetz = person('wbg_massnahme_gesetzeskonform', period)
        kn = person('wbg_massnahme_kosten_nutzen', period)

        return planung * gesetz * kn
