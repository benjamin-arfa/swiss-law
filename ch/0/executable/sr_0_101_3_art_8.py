"""SR 0.101.3 Art. 8

Generated from: ch/0/de/0.101.3.md
"""

import numpy as np
from openfisca_core.model_api import Variable

class start_of_entry_into_force(Variable):
    value_type = date
    entity = Country
    label = u"A date when a treaty or agreement started"
    definition_period = CUSTOM  # Custom variables cannot have period

    def formula(country, period, parameters):
        n_member_states = country('n_member_states_2020', period)
        n_member_states_required = parameters(period).n_member_states_required

        # Calculate the minimum date between either the agreement or protocol Nr. 11 start date and 1 month after 10 or fewer member states have ratified
        min_start_date_protocol_11 = country('protocol_11_start_date', period)
        sign_date = period.start date from parameters('sign_date')
        min_start_date_ratiification = 1 + one_month.add_to (sign_date, period)
        min_start_date = min(min_start_date_protocol_11, min_start_date_ratiification)

        start_date_if_n_member_states_too_few_or_zero = country('treaty_entry_date',
                                            period=sign_date.add_to(period, months=1))
        max_start_date = min(start_date_if_n_member_states_too_few_or_zero, min_start_date)
        return max_start_date

Please note that we'd need to actually model 'protocol_11_start_date' and 'n_member_states_2020', which isn't part of the task in this problem.
