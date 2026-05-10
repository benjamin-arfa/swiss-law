"""SR 0.105.1 Art. 17

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class torture_prevention_mechanism_implemented(Variable):
    value_type = float
    entity = Nation
    definition_period = MONTH
    label = "Months since torture prevention mechanism was implemented (SR 0.105.1 Art. 17)"

    def formula(national_government, period, parameters):
        entry_into_force_date = national_government("protocol_entry_into_force_date", period)
        implementation_mechanism_date = national_government(
            "implementation_mechanism_established_date", period
        )
        return (
            period.date - implementation_mechanism_date
        )  # Return a duration, though this will need the period as a duration
