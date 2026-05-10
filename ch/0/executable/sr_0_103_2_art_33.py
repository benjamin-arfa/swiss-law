"""SR 0.103.2 Art. 33

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class committee_seat_status(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY  # UN committee work might involve daily decisions
    label = "Status of a UN committee seat (SR 0.103.2 Art. 33)"

    def formula(person, period, parameters):
        is_committee_member = person("is_un_committee_member", period)
        is_securities_committee_member = person("is_security_committee_member", period)

        # Scenario 1: unanimous decision to not perform duties
        unanimous_abstention = (  # assume there are other members in the committee
            person("unanimous_abstention_decision", period)
        )

        # Scenario 2: death or resignation
        death_or_resigned = person("is_death_or_resigned", period)

        # Combine the conditions
        committee_seat_is_vacant = (
            is_committee_member
            & is_securities_committee_member
        ) & (
            unanimous_abstention
            | death_or_resigned
        )

        return committee_seat_is_vacant
