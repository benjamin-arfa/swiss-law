"""SR 0.101.094 Art. 6

Generated from: ch/0/de/0.101.094.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class composition_of_chambers(Variable):
    value_type = float
    label = "Composition of chambers"
    entity = Person
    definition_period = "P1Y"
    default_value = 0  # initial default value

    def formula(person, period, parameters):
        # adjust for Single Judge
        if single_judge(person, period):
            return 1
        # adjust for Committee
        elif committee(person, period):
            return 3
        # adjust for Chamber
        elif chamber(person, period):
            return 7
        # adjust for Grand Chamber
        elif grand_chamber(person, period):
            return 17
        else:
            raise exceptions.VirtualFunctionError("Invalid chamber composition")

    def formula_simplify(other_variables):
        # adjust for article 6, point 2 (possible adjustments)
        if parameters(period="last").article_6_point_2:
            return 5  # five judges per chamber
