"""SR 0.103.3 Art. 26

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

@reference('SR 0.103.3', source_url='https://www.admin.ch/opc/fr/classified-compilation/20181233/index.html#art_26')
class committee_selection_criterion(Variable):
    value_type = str
    entity = Committee
    definition_period = YEAR
    label = "Criterion for committee member selection (SR 0.103.3, Art. 26)"

    def formula(committee, period, parameters):
        # Assume parameters would be used to determine the selection method,
        # a list of members, their affiliations, or other relevant information.
        return parameters(period).committee.selection.criterion


class committee_member_replacement_trigger(Variable):
    value_type = bool
    entity = Committee
    definition_period = MONTH
    label = "Does a committee member need to be replaced? (SR 0.103.3, Art. 26, Para. 5)"

    def formula(committee, period, parameters):
        # Assume parameters would be used for triggering member replacement.
        member_death = parameters(period).committee.member.death
        member_resignation = parameters(period).committee.member.resignation
        return (member_death | member_resignation)


class committee_member_new_application(Variable):
    value_type = bool
    entity = Committee
    definition_period = MONTH
    label = "Can a new committee member be elected or recommended? (SR 0.103.3, Art. 26, Para. 5)"

    def formula(committee, period, parameters):
        # Assume parameters would be used to determine eligibility.
        selection_criterion = parameters(period).committee.selection.criterion
        is_new_member_period = committee('committee_period', period).is_new_member

        return (not is_new_member_period) & (selection_criterion == 'new')
