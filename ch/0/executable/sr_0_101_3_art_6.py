"""SR 0.101.3 Art. 6

Generated from: ch/0/de/0.101.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR

from openfisca_country_laws import Variable, parameters

class ExistingObligations(Variable):
    value_type = complex
    entity = 'country'
    label = VariableTranslation('Existing Obligations')
    definition_period = 'P1Y'

    def formula(country, period, parameters):
        # Assuming the parameter obligations is a list of tuples containing the party and the obligation
        return parameters(period).obligations
