"""SR 0.142.113.729 Art. 3

Generated from: ch/0/de/0.142.113.729.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class transportation_cost_burden(Variable):
    value_type = bool
    entity = Country
    definition_period = UNIQUE_ICAL_PERIOD
    label = "Country burden for transportation costs (Art. 3 SR 0.142.113.729)"

    def formula(country, period, parameters):
        initially_requested = country("initial_request", period)
        case_art_1_3 = parameters(period).transportation_cost_burden.case_art_1_3

        if case_art_1_3:
            return initially_requested

        return not initially_requested
