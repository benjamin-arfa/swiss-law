"""SR 0.101.1 Art. 4

Generated from: ch/0/de/0.101.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class EntitledToFreedomOfMovement(Variable):
    value_type = bool
    entity = Person
    label = u"Entitled to freedom of movement"
    definition_period = ETERNITY

    def formula_4(self, period, countries):
        # Individuals are entitled to freedom of movement if they have been 
        # previously allowed to participate in legal proceedings or if they 
        # have been allowed to travel by the Commission or court.
        allowed_to_participate = self("previous_participation_allowed", period - 1)
        allowed_to_travel = self("previous_travel_allowed", period - 1)

        return allowed_to_participate | allowed_to_travel

    def formula_restrictions(self, period, countries):
        # Freedom of movement is restricted by factors like national and public 
        # safety, upkeeping public order, preventing crimes.
        restrictions = self("national_safety_concerns", period)
        restrictions |= self("public_order_imperative", period)
        restrictions |= self("crime_prevention", period)

        return restrictions
