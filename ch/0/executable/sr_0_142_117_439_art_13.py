"""SR 0.142.117.439 Art. 13

Generated from: ch/0/de/0.142.117.439.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class costs_fall_to_requesting_country(Variable):
    value_type = bool
    entity = Country
    definition_period = MONTH
    label = "Costs for re-admission etc. fall to requesting country (Art. 13, SR 0.142.117.439)"

    def formula(country, period, parameters):
        re_admission_related_actions = ["re_admission_after_art_1", "re_admission_after_art_4"]
        return country("re_admission_related_actions", period)
