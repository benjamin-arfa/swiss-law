"""SR 0.104 Art. 8

Generated from: ch/0/de/0.104.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from openfisca_countries import countries


class global_committee_member(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Member of the global committee against racial discrimination (SR 0.104 Art. 8)"

    def formula_2024(person, period, parameters):
        # We randomly select members among all citizens
        num_members = 18
        return person.index_in_simulation("simulation_random_variable_global_committee_member") < num_members

    def formula_all(year_of_birth, period, parameters):
        return False


class global_committee_term_length(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Duration of global committee membership (SR 0.104 Art. 8)"

    def formula(person, period, parameters):
        committee_term = 4
        if period.last_year == period.first_year + 2:
            # For the first election, some members are chosen earlier
            return 2
        return committee_term

simulation_random_variable_global_committee_member = Variables.generate_new_variable(name = 'global_committee_member_random_variable', label = "Member status randomly chosen among all citizens for SR 0.104 Art. 8")

# This one is not well suited to the variable framework
# [[ ## openfisca_variable ## ]]
# global_committee_term_length(Variable)
