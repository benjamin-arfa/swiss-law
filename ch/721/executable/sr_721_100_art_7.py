"""SR 721.100 Art. 7

Generated from: ch/721/de/721.100.md

Art. 7 - Financial aid for training, research, and public information:
1. The Confederation may provide financial aid for:
   a. further training of specialists
   b. research and development of flood protection fundamentals and measures
   c. public information
2. Recipients may include: training institutes, national professional
   associations, cantons, public-law bodies, plant operators.
3. Financial aid is at most 45% of eligible costs, based on federal interest
   and recipient's financing capacity.
4. May also be set as lump sums based on pre-estimated costs.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class wbg_anrechenbare_kosten_finanzhilfe(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Eligible costs for training, research, or public information (CHF)"
    reference = "SR 721.100 Art. 7 Abs. 3"


class wbg_finanzhilfe_satz(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Applied financial aid rate (0 to max 0.45), based on federal interest and financing capacity"
    reference = "SR 721.100 Art. 7 Abs. 3"


class wbg_finanzhilfe(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Financial aid amount for training/research/information (CHF)"
    reference = "SR 721.100 Art. 7 Abs. 3"

    def formula(person, period, parameters):
        kosten = person('wbg_anrechenbare_kosten_finanzhilfe', period)
        satz = person('wbg_finanzhilfe_satz', period)
        max_satz = parameters(period).sr_721_100.finanzhilfe_max_satz

        # Cap the rate at the legal maximum
        effektiver_satz = min_(satz, max_satz)

        return kosten * effektiver_satz
