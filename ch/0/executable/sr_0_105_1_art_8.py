"""SR 0.105.1 Art. 8

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country


class subcommittee_member_replacement_proposal(Variable):
    value_type = bool
    entity = Country
    definition_period = MONTH
    label = "Proposal for replacement of a subcommittee member (Art. 8 SR 0.105.1)"

    def formula(country, period, parameters):
        death_or_resignation_event = country("subcommittee_member_death_or_resignation", period)
        member_is Unable_to_perform = country("subcommittee_member_unable_to_perform", period)

        proposed_candidate = country("proposed_replacement_candidate", period)

        proposal_would_be_fully_compliant = proposed_candidate.qualified_for_office & proposed_candidate.gender_has_been_balanced_over_six_months
        no_majority_rejection_withinSixWeeks = country("no_majority_rejection_withinSixWeeks", period)

        return (death_or_resignation_event | member_is_Untable_to_perform) & proposal_would_be_fully_compliant & no_majority_rejection_withinSixWeeks
