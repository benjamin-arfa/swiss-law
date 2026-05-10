"""SR 0.142.116.902 Art. 2

Generated from: ch/0/de/0.142.116.902.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class state_national_visa_exemption(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Visa exemption for state nationals (Art. 2 [Source])"

    def formula(person, period, parameters):
        stay_in_switzerland_days = person("stay_in_switzerland_days", period)
        has_valid_resident_permit = person("has_valid_resident_permit", period)

        is_short_term_visitor = (stay_in_switzerland_days <= 90)
        return is_short_term_visitor | has_valid_resident_permit
