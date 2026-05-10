"""SR 531.211.36 Art. 5

Generated from: ch/531/de/531.211.36.md
Delivery and use of stockpile goods:
- Only deliver quantities customers need for actual demand
- Rabies vaccine from stockpile may only be used for post-exposure or
  occupational pre-exposure prophylaxis
- Heilmittel division may revoke release if obligations not met
- Holder may refuse delivery if customer is insolvent
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class stockpile_vaccine_usage_permitted(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Whether use of stockpile rabies vaccine is permitted for the given purpose"
    reference = "SR 531.211.36 Art. 5"

    def formula(person, period, parameters):
        post_exposure = person("is_post_exposure_prophylaxis", period)
        occupational_pre_exposure = person("is_occupational_pre_exposure_prophylaxis", period)
        return post_exposure + occupational_pre_exposure


class stockpile_delivery_refusal_permitted(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Whether stockpile holder may refuse delivery to customer"
    reference = "SR 531.211.36 Art. 5 Abs. 4"

    def formula(person, period, parameters):
        customer_insolvent = person("customer_is_insolvent", period)
        return customer_insolvent
