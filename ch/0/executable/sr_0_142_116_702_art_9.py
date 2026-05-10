"""SR 0.142.116.702 Art. 9

Generated from: ch/0/de/0.142.116.702.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class agreement_effective_date_swiss(Variable):
    value_type = date
    entity = Country
    definition_period = LEGISLATIVE_YEAR
    label = "Effective date of SR 0.142.116.702 agreement in Switzerland (Art. 9)"

    def formula(country, period, parameters):
        last_notification_swiss = country("notification_last_dispatch_date_swiss", period)
        return (last_notification_swiss + TIMEDAYS(30))
