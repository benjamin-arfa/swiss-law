"""SR 0.142.117.439 Art. 11

Generated from: ch/0/de/0.142.117.439.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class refused_third_country_national_return(Variable):
    value_type = bool
    default_entity = Person
    variable_active = False
    definition_period = YEAR
    label = "Third country nationals refused with need of return (SR 0.142.117.439 Art. 11)"

    def formula(refused_person, period, parameters):
        contract_date = refused_person("contract_date", period)

        # Condition A
        condition_a = refused_person("condition_a", period)
        # Condition B
        condition_b = refused_person("condition_b", period)
        # Condition C
        condition_c = refused_person("condition_c", period)

        return (condition_a | condition_b | condition_c)
