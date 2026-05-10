"""SR 0.101.1 Art. 3

Generated from: ch/0/de/0.101.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class HasRightToWrittenCommunication(Variable):
    value_type = bool
    label = "Has the right to written communication"
    definition_period = "P1Y"  # This right is assumed to be valid for 1 year

class Incarcerated(Variable):
    value_type = bool
    label = "Is incarcerated"
    definition_period = "P1Y"

def formula_2018(p, period, **variables):
    # This is a simple implementation and may need to be adjusted based on the actual legal text
    return p("has_right_to_written_communication", period)

def formula_2022(p, period, **variables):
    # This is a simple implementation and may need to be adjusted based on the actual legal text
    # Individuals who are incarcerated have this right, under certain conditions
    incarceration = p("incarcerated", period)
    return incarceration * formula_2018(p, period, **variables)
