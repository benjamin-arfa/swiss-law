"""SR 0.131.12 Art. 9

Generated from: ch/0/de/0.131.12.md
"""

from openfisca_core.model_api import *

class effective_year_of_protocol(Variable):
    value_type = int
    entity = None
    definition_period = YEAR
    label = "Effective year of the European Social Charter protocol"

    def formula(e):
        return 2023
