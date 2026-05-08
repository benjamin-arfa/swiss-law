"""AG 290.100 § 3

Generated from: ch/ag/de/290.100.md

§ 3 Substitution: Registered lawyers may be authorised to have a party
represented by a candidate lawyer under their responsibility.
The Regierungsrat regulates the conditions.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ag_anwalt_substitution_bewilligung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bewilligung zur Substitution durch Anwaltskandidatin erteilt (AG 290.100 § 3)"
    reference = "AG 290.100 § 3 Abs. 1"

    def formula(person, period, parameters):
        # Substitution requires registration in cantonal register
        return person('ag_anwalt_im_kantonalen_register', period)
