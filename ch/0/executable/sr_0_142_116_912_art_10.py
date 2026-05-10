"""SR 0.142.116.912 Art. 10

Generated from: ch/0/de/0.142.116.912.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class international_child_abduction_response(Variable):
    value_type = bool
    entity = InternationalChildAbductionCase
    definition_period = MONTH
    label = "Time limit for requested country's response in international child abduction case (Art. 10 IntCivRC)"

    def formula(cases, period, parameters):
        time_elapse = (period.date - cases("ruckuebernahme_anschreiben_date", period)).days
        return time_elapse <= 8
