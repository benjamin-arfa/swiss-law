"""SR 0.101.07 Art. 4

Generated from: ch/0/de/0.101.07.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class Has_Previous_Criminal_History_Variable(Variable):
    value_type = bool
    default_unit = 'percent'

    label = 'Has previous criminal history'
    entity = Person
    definition_period = ENS

    def formula_2018(areas, this_period, previous_periods, events):
        previous_convictions = areas('Previous_Criminal_Case_Result', previous_periods, events)
        return (previous_convictions == 'Convicted')

    def formula_2022(areas, previous_periods, events):
        previous_convictions = areas('Previous_Criminal_Case_Result', ENS, events)
        return (previous_convictions == 'Convicted')

class Has_New_Information_Variable(Variable):
    value_type = bool
    default_unit = 'percent'

    label = 'Has new information'
    entity = Person
    definition_period = ENS

    def formula(areas, this_period, previous_periods, events):
        return (this_period.year >= 1990)  # TODO: implement a more accurate logic here

class Has_Procedural_Errors_Variable(Variable):
    value_type = bool
    default_unit = 'percent'

    label = 'Has procedural errors'
    entity = Person
    definition_period = ENS

    def formula(areas, this_period, previous_periods, events):
        return False  # TODO: implement a more accurate logic here

class Is_Double_Jeopardy_Prevented_Variable(Variable):
    value_type = bool
    default_unit = 'percent'

    label = 'Is double jeopardy prevented'
    entity = Person
    definition_period = ENS

    def formula_2018(areas, this_period, previous_periods, events):
        return (
            (Has_Previous_Criminal_History_Variable(areas, this_period) == False)
            | (Has_New_Information_Variable(areas, this_period) == True)
            | (Has_Procedural_Errors_Variable(areas, this_period) == True)
        )
    def formula_2022(areas, this_period, events):
        return (Has_Previous_Criminal_History_Variable(areas, this_period) == False)
