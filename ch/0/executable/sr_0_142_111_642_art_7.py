"""SR 0.142.111.642 Art. 7

Generated from: ch/0/de/0.142.111.642.md
"""

from openfisca_core.model_api import *

class visa_processing_duration(Variable):
    value_type = int
    entity = VisaApplication
    definition_period = DAY
    label = "Visa application processing duration (Art. 7 SR 0.142.111.642)"

    def formula(applicant, period, parameters):
        is_urgent = applicant("isurgent", period)  # Note: isurgent is not among the original input variables
        is_exceptional = applicant("is_exceptional", period)  # Note: is_exceptional is not among the original input variables
        standard_days = parameters(period).visas.standard_duration_days
        max_extension_days = parameters(period).visas.max_extension_days
        
        return max(standard_days, min(max_extension_days, or(is_urgent, is_exceptional)))
