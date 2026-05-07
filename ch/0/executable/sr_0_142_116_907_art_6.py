"""SR 0.142.116.907 Art. 6

Generated from: ch/0/de/0.142.116.907.md
"""

from openfisca_core.model_api import *

class annual_stagiaires_limit(Variable):
    value_type = int
    entity = None
    definition_period = YEAR
    label = "Annual Stagiaires Limit (Article 6 SR 0.142.116.907)"

    def formula(_variables, period, parameters):
        return 100
