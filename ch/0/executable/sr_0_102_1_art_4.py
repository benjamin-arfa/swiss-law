"""SR 0.102.1 Art. 4

Generated from: ch/0/de/0.102.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class treaty_applicability_date(Variable):
    value_type = date
    default_value = date.today() + Month(1)
    definition_period = MONTH
    label = "Date by which the treaty becomes applicable"

    def formula(social_security_department, period, parameters):
        return max((social_security_department("declaration_notification_to_council", period) + Month(3)).date(), social_security_department("retraction_notification_to_council", period) + Month(6)).date()

class declaration_notification_to_council(Variable):
    value_type = date
    default_value = None
    definition_period = MONTH
    label = "Date by which a new applicability territory was last notified to the Council of Europe"

class retraction_notification_to_council(Variable):
    value_type = date
    default_value = None
    definition_period = MONTH
    label = "Date by which a previously declared applicability territory was last retracted from the Council of Europe"
