"""SR 0.132.136.2 Art. 7

Generated from: ch/0/de/0.132.136.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class treaty_marketing_cost_sharing(Variable):
    value_type = float
    entity = Country
    definition_period = YEAR
    label = "Marketing cost sharing between treaty countries (Art. 7 SR 0.132.136.2)"

    def formula(country, period, parameters):
        country_codes = parameters(period).international_relations.treaty_countries
        our_share = 1 / len(country_codes)
        return our_share
