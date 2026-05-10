"""SR 0.131.13 Art. 21

Generated from: ch/0/de/0.131.13.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class european_convention_terminated(Variable):
    value_type = bool
    entity = Union
    definition_period = MONTH
    label = "European Convention terminated (Art. 21, SR 0.131.13)"

    def formula(union, period, parameters):
        notice_served = union("european_convention_notice_served", period)
        notice_start_date = union("european_convention_notice_start_date", period)
        notice_period = parameters(period).organizations.european_convention.notice_period
        termination_date = notice_start_date + notice_period
        return (period.first_month_in_period >= termination_date).astype(int)
