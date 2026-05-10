"""SR 0.105 Art. 17

Generated from: ch/0/de/0.105.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class committee_member_term(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Term length of committee member (SR 0.105, Art. 17)"

    def formula(person, period, parameters):
        last_election = person("last_election", period)
        current_year = period.year
        if last_election:
            return 2 if (current_year - last_election) < 3 else 4
        else:
            return 0  # if no last election, the person is not a committee member

# The term length is influenced by the election process, but this example does not model the election itself.

class committee_member_replaced(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether a committee member was replaced (SR 0.105, Art. 17)"

    def formula(person, period, parameters):
        last_replacement = person("last_replacement", period)
        current_year = period.year
        if last_replacement:
            return 1 if (current_year - last_replacement) < current_year else 0
        else:
            return 0  # if no last replacement, the person is not affected
