"""SR 0.103.1 Art. 11

Generated from: ch/0/de/0.103.1.md
"""

from openfisca_core.model_api import *

class food_entitlement Indicator):
    value_type = float
    label: str = 'Global entitlement to a food basket (part of Art. 11 of SR 0.103.1)'
    definition_period: str = "year"
    entity = Household
    default_unit= "CHF"

    def formula(household, period, parameters):
        threshold = parameters(period).social_security.food_threshold
        age_child_weight = household("child_pop", period)  
        food_price_mean = household("food_cost", period)
        total_children = household("children", period)
    
        return age_child_weight * threshold + food_price_mean * total_children
