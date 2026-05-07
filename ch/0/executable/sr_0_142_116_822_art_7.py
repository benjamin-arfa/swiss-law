"""SR 0.142.116.822 Art. 7

Generated from: ch/0/de/0.142.116.822.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class visa_processing_time(Variable):
    value_type = bool
    entity = Person
    definition_period = PERIOD('business-day', start='2024-01-01', end='+1 year')
    label = "Visa application processing time exceeded (Art. 7 SR 0.142.116.822)"

    def formula(person, period, parameters):
        # assuming 'application_date' attribute to check processing time elapsed since submission
        application_date = person("application_date", period)
        decision_made_date = person("decision_made_date", period)
        business_days = parameters(period).demographic.business_days_in_a_year

        standard_days = 10
        extended_days = 30
        reduced_days = 3

        exceeded_standard_time = (period.end_date - application_date).days / business_days > standard_days

        exceeds_extended_time = (period.end_date - application_date).days / business_days > extended_days

        exceeds_reduced_time = (period.end_date - application_date).days / business_days > (business_days - 3)

        return exceeded_standard_time & !(exceeds_extended_time | exceeds_reduced_time)
