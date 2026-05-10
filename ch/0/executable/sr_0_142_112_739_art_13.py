"""SR 0.142.112.739 Art. 13

Generated from: ch/0/de/0.142.112.739.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class duration_of_convention(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Duration of international social security treaty agreement (Art. 13 SR 0.142.112.739)"

    def formula(person, period, parameters):
        agreement_duration_start_year = 2023
        max_duration_years = 3

        starting_year = agreement_duration_start_year
        current_year = int(period.year)

        duration_years = min(max_duration_years, current_year - starting_year)
        return duration_years
