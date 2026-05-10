"""SR 0.142.116.919 Art. 4

Generated from: ch/0/de/0.142.116.919.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class foreign_national_responsibility_condition(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "Treaty-partner foreign national responsibility condition (SR 0.142.116.919 Art. 4)"

    def formula(person, period, parameters):
        days_in_switzerland = person("days_in_switzerland", period)
        valid_visa_before_leave = person("valid_visa_before_leave", period)
        return (days_in_switzerland <= parameters(period).social_security.mandatory_insurance.maximum_days_in_switzerland) or (valid_visa_before_leave and days_in_switzerland > parameters(period).social_security.foreign_national_responsibility_visa_valid_before_leave)
