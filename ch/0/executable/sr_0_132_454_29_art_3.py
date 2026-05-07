"""SR 0.132.454.29 Art. 3

Generated from: ch/0/de/0.132.454.29.md
"""

We won't need a variable in this case as the information in the article is more about the cost-sharing arrangement than creating a calculation within the model.

However to be precise we could model a Variable that computes the amount each government needs to pay with some other external Variable providing the total costs. This is not what the article seems to point at with the intention, we will model it the way one would model it with the intention.

Here is an example of how we could model this. Consider `border_stone_construction_total_costs` would be the external Variable in this example as there will be no one formula available from this piece of Legislation.

from openfisca_core.model_api import *

# Government
class government_entity(Entities):
    entity_class = entities.Entity
    role = entities.Role(
        country='Switzerland'
    )

# Define entities
class Government(government_entity):

    def formula(countries, period, parameters):
        # This will probably be the one from the Swiss Government.
        return 1


class border_stone_construction_total_costs(Variable):
    value_type = float
    entity = Government
    definition_period = YEAR


class border_stone_construction_costs_ch(Variable):
    value_type = float
    entity = Government
    definition_period = YEAR

    def formula(government, period, parameters):
        return (government("border_stone_construction_total_costs", period)) * 0.5


class border_stone_construction_costs_foreign(Variable):
    value_type = float
    entity = Government
    definition_period = YEAR

    def formula(government, period, parameters):
        return (government("border_stone_construction_total_costs", period)) * 0.5

This modelling would be very good for calculating the Costs for the border construction that Switzerland would need to cover if some external Variable had the information on the total costs needed for the border construction. Since the total cost cannot be known in advance in model building we would model it this way.
