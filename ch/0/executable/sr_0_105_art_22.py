"""SR 0.105 Art. 22

Generated from: ch/0/de/0.105.md
"""

from openfisca_core.model_api import *

class complaint_eligibility(Variable):
    value_type = bool
    label = "Eligibility to submit a complaint under Article 22 SR 0.105"

    def formula(person, period, parameters):
        is_victim = person('has_suffered_human_rghts_violation', period)
        has_exhausted_local_recourse = person('has_exhausted_local_recourse', period)
        is_not_involved_in_another_international_proceeding = person('is_not_involved_in_another_international_proceeding', period)

        return is_victim * has_exhausted_local_recourse * is_not_involved_in_another_international_proceeding
