"""SR 0.101.06 Art. 3

Generated from: ch/0/de/0.101.06.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class start_protocol_period(Variable):
    value_type = bool
    label = "Start of the Protocol period"
    entity = Person
    definition_period = "P1Y"
    default_init = False

    def formula(person, period, parameters):
        # This is the start of the protocol, so we assume it's False initially
        return parameters(period).start_protocol_period * (not person(2024, period), period.duration)

    def formula_simplified_expression(person, period, parameters):
        return f"{parameters(period).start_protocol_period} AND {not person(2024, period)}"
