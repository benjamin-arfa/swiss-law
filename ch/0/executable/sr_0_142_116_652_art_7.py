"""SR 0.142.116.652 Art. 7

Generated from: ch/0/de/0.142.116.652.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class visa_processing_time(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Visa processing time (Art. 7 SR 0.142.116.652)"

    def formula(person, period, parameters):
        processing_time = 0
        urgency_level = parameters(period).visa.urgency_level
        if urgency_level == 3:
            processing_time = 5
        elif urgency_level == 2:
            processing_time = 30
        elif urgency_level == 1:
            processing_time = 3
        return processing_time
