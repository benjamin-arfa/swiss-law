"""SR 744.211 Art. 12

Generated from: ch/744/de/744.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vehicle_company_designation_displayed(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeug trägt auf beiden Längsseiten die Bezeichnung der betriebführenden Unternehmung"
    reference = "SR 744.211 Art. 12 Abs. 1"

    def formula(person, period, parameters):
        # Both longitudinal sides must show the operating company name,
        # in full, abbreviated, or symbolic form
        left_side_marked = person('vehicle_left_side_company_marked', period)
        right_side_marked = person('vehicle_right_side_company_marked', period)
        return left_side_marked * right_side_marked


class vehicle_left_side_company_marked(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Linke Längsseite des Fahrzeugs trägt Unternehmungsbezeichnung"
    reference = "SR 744.211 Art. 12 Abs. 1"


class vehicle_right_side_company_marked(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rechte Längsseite des Fahrzeugs trägt Unternehmungsbezeichnung"
    reference = "SR 744.211 Art. 12 Abs. 1"


class vehicle_order_number_height_cm(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Höhe der Ordnungsnummer am Fahrzeug in Zentimetern"
    reference = "SR 744.211 Art. 12 Abs. 2"


class vehicle_order_number_compliant(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeug trägt aussen eine gut sichtbare Ordnungsnummer von mindestens 10 cm Höhe"
    reference = "SR 744.211 Art. 12 Abs. 2"

    def formula(person, period, parameters):
        height_cm = person('vehicle_order_number_height_cm', period)
        # Minimum height requirement: 10 cm
        height_compliant = height_cm >= 10.0
        has_order_number = person('vehicle_has_visible_order_number', period)
        return has_order_number * height_compliant


class vehicle_has_visible_order_number(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeug ist aussen mit einer gut sichtbaren Ordnungsnummer versehen"
    reference = "SR 744.211 Art. 12 Abs. 2"


class trolleybus_order_number_placement_compliant(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ordnungsnummer des Trolleybusses ist vorne und hinten angebracht"
    reference = "SR 744.211 Art. 12 Abs. 2"

    def formula(person, period, parameters):
        is_trolleybus = person('is_trolleybus', period)
        number_front = person('vehicle_order_number_at_front', period)
        number_rear = person('vehicle_order_number_at_rear', period)
        # Trolleybuses: front and rear; rule only applies when vehicle is a trolleybus
        trolleybus_compliant = number_front * number_rear
        return where(is_trolleybus, trolleybus_compliant, True)


class trailer_order_number_placement_compliant(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ordnungsnummer des Anhängers ist hinten angebracht"
    reference = "SR 744.211 Art. 12 Abs. 2"

    def formula(person, period, parameters):
        is_trailer = person('is_trailer', period)
        number_rear = person('vehicle_order_number_at_rear', period)
        # Trailers: rear only; rule only applies when vehicle is a trailer
        return where(is_trailer, number_rear, True)


class is_trolleybus(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeug ist ein Trolleybus"
    reference = "SR 744.211 Art. 12 Abs. 2"


class is_trailer(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeug ist ein Anhänger"
    reference = "SR 744.211 Art. 12 Abs. 2"


class vehicle_order_number_at_front(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ordnungsnummer ist vorne am Fahrzeug angebracht"
    reference = "SR 744.211 Art. 12 Abs. 2"


class vehicle_order_number_at_rear(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ordnungsnummer ist hinten am Fahrzeug angebracht"
    reference = "SR 744.211 Art. 12 Abs. 2"


class trolleybus_route_designation_compliant(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Im Personenverkehr eingesetzter Trolleybus trägt Streckenbezeichnung für Fahrgäste"
    reference = "SR 744.211 Art. 12 Abs. 3"

    def formula(person, period, parameters):
        is_trolleybus = person('is_trolleybus', period)
        in_passenger_service = person('vehicle_in_passenger_service', period)
        has_route_designation = person('trolleybus_has_route_designation', period)
        # Only trolleybuses in passenger service must carry route designation
        must_have_designation = is_trolleybus * in_passenger_service
        return where(must_have_designation, has_route_designation, True)


class vehicle_in_passenger_service(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeug ist im Personenverkehr eingesetzt"
    reference = "SR 744.211 Art. 12 Abs. 3"


class trolleybus_has_route_designation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Trolleybus ist mit einer Streckenbezeichnung für Fahrgäste versehen"
    reference = "SR 744.211 Art. 12 Abs. 3"


class vehicle_art12_fully_compliant(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeug erfüllt alle Kennzeichnungspflichten gemäss Art. 12"
    reference = "SR 744.211 Art. 12"

    def formula(person, period, parameters):
        company_designation = person('vehicle_company_designation_displayed', period)
        order_number = person('vehicle_order_number_compliant', period)
        trolleybus_placement = person('trolleybus_order_number_placement_compliant', period)
        trailer_placement = person('trailer_order_number_placement_compliant', period)
        route_designation = person('trolleybus_route_designation_compliant', period)
        return (
            company_designation
            * order_number
            * trolleybus_placement
            * trailer_placement
            * route_designation
        )
