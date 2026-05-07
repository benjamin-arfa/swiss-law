"""SR 0.101.06 Art. 2

Generated from: ch/0/de/0.101.06.md
"""

from openfisca_core import Variable
from openfisca_core.periods import YEAR

class Kriegszeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Is the state in a state of war or under imminent threat of war?"

    def formula_2004(event_series, this_period, states_at_beginning_of_period):
        if "in" in str(event_series):
            return 1
        else:
            return 0
Here, I tried to model 'Kriegszeit,' or the period of war, within the context of the legal article, as a boolean that would be true if 'in' was found in any events such as at any point in time during the year (the definition period).
