"""SR 0.101.07 Art. 9

Generated from: ch/0/de/0.101.07.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class entry_into_force_date(Variable):
    value_type = date
    label = "Entry into force date"
    entity = Universe
    definition_period = YEAR
    display = False

    def formula(person, period, parameters):
        seven_ratified_member_states_date = person('seven_ratified_member_states_date', period)
        latest_ratification_date = person('latest_ratification_date', period)

        if seven_ratified_member_states_date:
            if seven_ratified_member_states_date <= latest_ratification_date:
                entry_into_force_date = seven_ratified_member_states_date + MONTHS(2)
            else:
                entry_into_force_date = seven_ratified_member_states_date
        else:
            entry_into_force_date = latest_ratification_date + MONTHS(2)

        return entry_into_force_date
