"""AG 290.100 § 18

Generated from: ch/ag/de/290.100.md

§ 18 Unerlaubte Ausuebung des Anwaltsberufs: Practising activities reserved
for lawyers without fulfilling BGFA requirements is punishable by a fine of
up to CHF 20,000. Exception: gratuitous assistance per § 2 Abs. 3.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ag_unerlaubte_berufsausuebung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Unerlaubte Ausuebung des Anwaltsberufs (AG 290.100 § 18)"
    reference = "AG 290.100 § 18 Abs. 1"


class ag_unerlaubte_berufsausuebung_busse(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Busse wegen unerlaubter Berufsausuebung in CHF (AG 290.100 § 18)"
    reference = "AG 290.100 § 18 Abs. 1"

    def formula(person, period, parameters):
        unerlaubt = person('ag_unerlaubte_berufsausuebung', period)
        # Max fine CHF 20'000
        return unerlaubt * 20000
