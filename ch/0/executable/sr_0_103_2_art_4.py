"""SR 0.103.2 Art. 4

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country


class echr_derivative_measures_taken(Variable):
    value_type = bool
    entity = Country
    definition_period = DAY
    label = "Article 4 derogatory measures taken (SR 0.103.2)"

    def formula(countries, period, parameters):
        # For simplicity, we assume that only one country can take derogatory measures at a time.
        derogation_declaration = parameters(period).social_security.official_ notification.official_emergency_declaration
        communication_with_other_states = parameters(period).social_security. official_notification.communication_with_countries
        non_derogable_articles = ["Article_6", "Article_7 ", "Article_8_Abs_1&2", "Article_11", "Article_15", "Article_16", "Article_18"]

        derogatory_measures_taken = (derogation_declaration and communication_with_other_states) and (not non_derogable_articles)
        return derogatory_measures_taken
