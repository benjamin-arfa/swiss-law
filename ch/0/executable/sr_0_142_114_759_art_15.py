"""SR 0.142.114.759 Art. 15

Generated from: ch/0/de/0.142.114.759.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class repatriation_costs_bearer(Variable):
    value_type = str
    entity = Country
    definition_period = DAY
    label = "Repatriation costs bearer (Art. 15 SR 0.142.114.759)"

    def formula(country, period, parameters):
        return "Requesting country"  # according to Art. 15, the requesting country bears the costs.
