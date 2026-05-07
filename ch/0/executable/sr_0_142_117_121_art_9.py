"""SR 0.142.117.121 Art. 9

Generated from: ch/0/de/0.142.117.121.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person, State


@check_initialize
def return_request_duration(period, parameters):
    # The default duration for all steps of the return process is set to the defined period (typically one or more months).
    return_period = period.duration('month')
    normal_duration = return_period
    extension_max_duration = 2 * return_period
    
    return normal_duration, extension_max_duration


@check_initialize
def reimbursement_decision_deadline(period, parameters):
    # Two steps in the process can extend the duration: a longer decision period, or a longer period for the return.
    normal_duration, extension_max_duration = return_request_duration(period, parameters)
    
    # The maximum duration is determined by the extended periods.
    reimbursement_deadline_duration = min(normal_duration, extension_max_duration)
    
    return period.start + reimbursement_deadline_duration

@check_initialize    
def return_effective_date(period, parameters):
    decision_deadline = reimbursement_decision_deadline(period, parameters)
    # If the decision was made on time, return the date the person has to be returned to the state of origin.
    return_date = decision_deadline
    return return_date
