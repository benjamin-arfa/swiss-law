"""SR 0.103.2 Art. 29

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class committee_member_eligibility(Variable):
    value_type = bool
    entity = Person
    definition_period = WEEK
    label = "Eligibility as committee member (Art. 29 SR 0.103.2)"

    def formula(person, period, parameters):
        canton_of_residence = person("canton_of_residence", period)
        max_proposal_per_canton = parameters(period).international_relations.committee_member.count_per_canton

        # Check if person is actually proposed as a committee member from their canton
        is_proposed = False  # This condition would involve checking some other variable or data source
        citizen_of_switzerland = person("citizen_of_switzerland", period)

        return (is_proposed | (not is_proposed & citizen_of_switzerland <= max_proposal_per_canton))
