"""SR 0.131.1 Art. 9

Generated from: ch/0/de/0.131.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class convention_in_force(Variable):
    value_type = bool
    definition_period = MONTH
    label = "Entry into force of the convention (Art. 9 SR 0.131.1)"

    def formula(person, period, parameters):
        ratifications = parameters(period).social_security.convention.ratifications
        bordering_states = parameters(period).social_security.convention.bordering_states
        month = period.start

        def count_ratifications(date):
            return sum(1 for state, ratification_date in ratifications.items() if ratification_date <= date)

        return count_ratifications(month) >= 4 and len(filter(lambda state, bordering_states = bordering_states: state in bordering_states, ratifications.keys())) >= 2
