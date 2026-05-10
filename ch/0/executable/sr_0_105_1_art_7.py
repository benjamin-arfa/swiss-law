"""SR 0.105.1 Art. 7

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class election_quorum(Variable):
    value_type = bool
    entity = None
    definition_period = YEAR
    label = "Election quorum reached (Art. 7 para. 1)"

    def formula_justification(parameters):
        quorum = parameters(period).election.quorum
        return True if parameters(period).election.number_of_contracting_parties >= quorum else False

class election_date(Variable):
    value_type = bool
    entity = None
    definition_period = YEAR
    label = "Election date check (Art. 7 para. 1)"

    def formula_justification(parameters):
        election_date = parameters(period).election.election_date
        return True if election_date <= parameters(period).election.current_date else False

class elected_members(Variable):
    value_type = float
    entity = None
    definition_period = YEAR
    label = "Number of elected members (Art. 7 para. 1)"

    def formula_justification(parameters):
        number_of_members = parameters(period).election.number_of_members
        return number_of_members
