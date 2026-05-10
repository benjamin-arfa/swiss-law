"""SR 0.142.117.149 Art. 7

Generated from: ch/0/de/0.142.117.149.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class transit_status(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Status of transit through Switzerland (Article 7 SR 0.142.117.149)"

    def formula(person, period, parameters):
        # Assume the following events make the individual a transit case:
        # - The individual is from a third country and has an expulsion order from another country
        # - The individual is transiting to their destination country
        from_third_country = (person("nationality", period) == "third_country")
        has_expulsion_order = parameters(period).immigration.expulsion_orders.exists_person(person, period)
        transiting_to_destination = parameters(period).transit.transiting_to_destination.exists_person(person, period)

        # The logic can be either AND or OR or a combination of both.
        # For simplicity, let's assume we are interested in cases where at least one condition is false:
        return ~from_third_country | ~has_expulsion_order & ~transiting_to_destination
