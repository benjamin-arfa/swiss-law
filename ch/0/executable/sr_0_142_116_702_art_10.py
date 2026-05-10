"""SR 0.142.116.702 Art. 10

Generated from: ch/0/de/0.142.116.702.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class international_agreement_status(Variable):
    value_type = bool
    scope = Country
    label = "International agreement status (SR 0.142.116.702 Art. 10)"

    def formula(countries, period, parameters):
        # implementation of the notification logic is missing in the article, 
        # we simplify this for the sake of argumentation
        return countries("has_sent_notification", period) and countries("has_received_notification", period)
