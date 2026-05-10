"""SR 0.103.2 Art. 25

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class electoral_rights(Variable):
    value_type = bool
    entity = Person
    definition_period = PERIOD
    label = "Electoral rights under the Federal Constitution (Art. 25, SR 0.103.2)"

    def formula(person, period, parameters):
        no_discrimination = not person(...)  # assuming a variable for Article 2 criteria
        can_participate_public_affairs = person(...).any()  # assuming a variable for the possibility to participate in public affairs
        can_vote = person(...).any()  # assuming a variable for suffrage
        can_access_offices = person(...).any()  # assuming a variable for access to public offices

        return (no_discrimination & can_participate_public_affairs & can_vote & can_access_offices)
