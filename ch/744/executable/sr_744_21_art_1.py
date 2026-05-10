"""SR 744.21 Art. 1

Generated from: ch/744/de/744.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class is_public_transport_company(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist das Unternehmen ein Unternehmen des öffentlichen Verkehrs"
    reference = "SR 744.21 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        return person('uses_trolleybus_vehicles', period)


class uses_trolleybus_vehicles(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verwendet das Unternehmen Trolleybusfahrzeuge"
    reference = "SR 744.21 Art. 1 Abs. 1"


class subject_to_trolleybus_law(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Untersteht das Unternehmen dem Trolleybusgesetz (SR 744.21)"
    reference = "SR 744.21 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        is_public_transport = person('is_public_transport_company', period)
        uses_trolleybuses = person('uses_trolleybus_vehicles', period)
        interstate_override = person('interstate_agreement_overrides_trolleybus_law', period)
        return is_public_transport * uses_trolleybuses * not_(interstate_override)


class vehicle_draws_energy_from_overhead_line(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Entnimmt das Fahrzeug die elektrische Energie aus einer Fahrleitung"
    reference = "SR 744.21 Art. 1 Abs. 2"


class vehicle_travels_on_public_roads(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verkehrt das Fahrzeug auf öffentlichen Strassen"
    reference = "SR 744.21 Art. 1 Abs. 2"


class vehicle_not_bound_to_rails(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist das Fahrzeug nicht an Schienen gebunden"
    reference = "SR 744.21 Art. 1 Abs. 2"


class is_trolleybus(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist das Fahrzeug ein Trolleybus im Sinne von SR 744.21"
    reference = "SR 744.21 Art. 1 Abs. 2"

    def formula(person, period, parameters):
        motor_driven = person('vehicle_draws_energy_from_overhead_line', period)
        public_roads = person('vehicle_travels_on_public_roads', period)
        no_rails = person('vehicle_not_bound_to_rails', period)
        return motor_driven * public_roads * no_rails


class interstate_agreement_overrides_trolleybus_law(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gilt eine abweichende zwischenstaatliche Vereinbarung für Trolleybusfahrzeuge"
    reference = "SR 744.21 Art. 1 Abs. 3"
