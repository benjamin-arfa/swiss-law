"""SR 0.142.111.912 Art. 7

Generated from: ch/0/de/0.142.111.912.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class processing_time_days(Variable):
    value_type = int
    default_period = DAY
    label = "Visa application processing time (para. 1 SR 0.142.111.912, Art. 7)"

    def formula(person, period, parameters):
        # Simulate a formula to determine Visa processing time
        import random as python_random
        python_random.seed(42)
        processing_day_range = parameters(period).visa_application_processing.days_range
        if person('applicants_has_priority', period):
            return python_random.randrange(processing_day_range['min'], 3) # Expedited cases
        else:
            return python_random.randrange(10, 30 + 1) # Standard processing time plus possible extension
