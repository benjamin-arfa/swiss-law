"""SR 0.106 Art. 5

Generated from: ch/0/de/0.106.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Definition of the Committee of Social Rights Member entity
class Committee_of_Social_Rights_Member(electorate_group.Entity):
    pass


#  The election variable: A Set of elected candidates.
class elected_member(Variable):
    value_type = Set
    possible_values = Committee_of_Social_Rights_Member
    entity = electorate_group
    label = "Elected member of the European Committee of Social Rights"

    def formula(electorate, period, parameters):
        num_nominations = parameters(period).election_rules.committee_of_social_rights.num_nominations
        elected_members = electorate("nominated_member", period)
        elected_set = set(elected_members[:num_nominations])
        return elected_set


# Variable for the current term of elected members.
class term_length(Variable):
    value_type = int
    entity = electorate_group
    definition_period = YEAR
    label = "Term length of a member of the European Committee of Social Rights"

    def formula(electorate, period, parameters):
        fixed_term_length = parameters(period).election_rules.committee_of_social_rights.fixed_term_length
        flexible_term_length = parameters(period).election_rules.committee_of_social_rights.flexible_term_length
        num_elections = electorate.members("committee_of_social_rights_election_history", period)[:, "election_number"]
        last_election_index = num_elections.argmax()
        last_election_rules = parameters(period).last("election_rules", last_election_index)
        return last_election_rules.term_length if last_election_rules.term_length != -1 else fixed_term_length


# Variable for the election frequency
class election_frequency(Variable):
    value_type = int
    entity = electorate_group
    definition_period = YEAR
    label = "Election frequency of the European Committee of Social Rights"

    def formula(electorate, period, parameters):
        num_years_between_elections = min(6, 4) # min between possible min or max lengths
        num_initial_elections = electorate.members("committee_of_social_rights_election_history", period)[:, "election_number"]
        num_last_election = num_initial_elections.max()
        return num_years_between_elections
