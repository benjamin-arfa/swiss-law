"""SR 0.142.305 Art. 9

Generated from: ch/0/de/0.142.305.md
"""

from openfisca_core.model_api import *
from openfisca_core.indexed_enums import SimpleEnum
from openfisca_core.parameters import param, Period


class european_convention_entry_into_force(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Entry into force of the European Convention on Social Security (Art. 9 SR 0.142.305)"

    def formula(countries, period, parameters):
        convention_entry_date = parameters(period).social_convention.european_entry_date

def has_rated_on(country, period, parameters):
        ratified_on = parameters(period).social_convention.european_rated_on[country]
        return country(year=period.date.year) in ratified_on

class country(Variable):
        use_metadata = False
        type = SimpleEnum
        possible_values = ParametersPeriod, 'social_convention', 'european_rated_on', None


class ParametersPeriod):
        def formula(self):
            return {
                country: [2024, 2025]
            
class EuropeanRatifiedOn(Variable):
        value_type = bool
        entity = Country
        definition_period = YEAR
        label = "Has European Convention been ratified"
        
def formula(country):
            return country in self.possible_values
