"""SR 0.102 Art. 13

Generated from: ch/0/de/0.102.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class is_local_body_insured(Variable):
    value_type = bool
    entity = Municipality
    definition_period = YEAR
    label = "Local body insurability (Art. 13 of the Swiss constitution)"

    def formula(local_body, period, parameters):
        municipality_types_selected = parameters(period).legal.constitution.charta_selected_municipality_types

        # The function should return True if the condition is met
        # In this case, the condition is complex and involves nested conditions
        return local_body in municipality_types_selected
