"""SR 0.103.2 Art. 31

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import CommitteeMember


class committee_nationality_unique(Variable):
    value_type = bool
    entity = CommitteeMember
    definition_period = PERPETUAL
    label = "Unique nationalities in committee membership (SR 0.103.2 Art. 31)"

    def formula(members, period, parameters):
        unique_nationalities = set(member("nationality", period) for member in members)
        return len(unique_nationalities) == len(members)
