"""SR 0.142.116.702 Art. 7

Generated from: ch/0/de/0.142.116.702.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class agreement_change_effective_date(Variable):
    value_type = Date
    entity = Partnership
    label = "Effective date of an amendment to the agreement (Art. 7 SR 0.142.116.702)"
    definition_period = DAY

    def formula(partnership, period, parameters):
        internal_procedure_completed_party1 = parameters(period).agreements.ahv_implementation_process.\
            partner1_completed_on
        internal_procedure_completed_party2 = parameters(period).agreements.ahv_implementation_process.\
            partner2_completed_on

        # Determine the second notification date, which is the effective date of the change.
        # This is an implicit assumption in the given legal text.
        second_notification_date = max(internal_procedure_completed_party1, internal_procedure_completed_party2)
        return second_notification_date
