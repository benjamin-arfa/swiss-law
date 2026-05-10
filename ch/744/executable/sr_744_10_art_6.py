"""SR 744.10 Art. 6

Generated from: ch/744/de/744.10.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class number_of_vehicles(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Number of vehicles operated by the undertaking (per vehicle registration document)"
    reference = "SR 744.10 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        return person('number_of_vehicles', period)


class total_vehicle_weight_kg(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Total gross weight (kg) of all vehicles operated, per vehicle registration document"
    reference = "SR 744.10 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        return person('total_vehicle_weight_kg', period)


class equity_and_reserves(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Sum of equity capital and reserves of the undertaking (CHF)"
    reference = "SR 744.10 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        return person('equity_and_reserves', period)


class minimum_required_capital(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Minimum required equity and reserves based on number of vehicles and their total weight (CHF), as set by the Federal Council under SR 744.10 Art. 6 Abs. 2"
    reference = "SR 744.10 Art. 6 Abs. 1-2"

    def formula(person, period, parameters):
        n_vehicles = person('number_of_vehicles', period)
        total_weight_kg = person('total_vehicle_weight_kg', period)
        # Base amounts are fixed by the Federal Council (Bundesrat) per Art. 6 Abs. 2.
        # These placeholder values must be replaced with the amounts from the implementing ordinance.
        base_amount_per_vehicle = 9000.0   # CHF per vehicle (Grundbetrag)
        base_amount_per_tonne = 500.0      # CHF per tonne of total gross weight
        total_weight_tonnes = total_weight_kg / 1000.0
        return (n_vehicles * base_amount_per_vehicle) + (total_weight_tonnes * base_amount_per_tonne)


class financial_capacity_guaranteed(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the undertaking's financial capacity is guaranteed under SR 744.10 Art. 6: equity and reserves meet the minimum amount determined by number of vehicles and their total weight"
    reference = "SR 744.10 Art. 6"

    def formula(person, period, parameters):
        equity = person('equity_and_reserves', period)
        minimum = person('minimum_required_capital', period)
        return equity >= minimum
