"""SR 0.101.093 Art. 5

Generated from: ch/0/de/0.101.093.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR

class Article5Variable(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH

    def formula(self, period, _):
        # Assuming we have an 'has_convention' variable
        return self.variable(
            'boolean', 'has convention',
            person('has_convention', period)
        )

To implement the logic of the variable, we would need to define a parameter in the YAML file. However, since the article does not provide any numerical values or thresholds, we will simply leave the parameter empty for now.
