"""SR 744.10 Art. 3

Generated from: ch/744/de/744.10.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class commercially_transports_passengers_large_vehicle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gewerbsmässige Personenbeförderung mit Fahrzeugen für mehr als 8 Personen (Art. 3 Abs. 1bis lit. a)"
    reference = "SR 744.10 Art. 3 Abs. 1bis lit. a"

    def formula(person, period, parameters):
        offers_public_transport = person('offers_public_or_group_passenger_transport', period)
        large_vehicle = person('vehicle_capacity_over_8_passengers', period)
        return offers_public_transport * large_vehicle


class commercially_transports_goods_heavy_vehicle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gewerbsmässige Güterbeförderung mit Fahrzeugen über 2,5 Tonnen Gesamtgewicht (Art. 3 Abs. 1bis lit. b)"
    reference = "SR 744.10 Art. 3 Abs. 1bis lit. b"

    def formula(person, period, parameters):
        commercial_goods = person('commercial_goods_transport', period)
        heavy_vehicle = person('vehicle_total_weight_exceeds_2_5_tonnes', period)
        return commercial_goods * heavy_vehicle


class subject_to_road_transport_license_requirement(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unterliegt grundsätzlich der Zulassungspflicht als Strassentransportunternehmen (Art. 3 Abs. 1bis)"
    reference = "SR 744.10 Art. 3 Abs. 1bis"

    def formula(person, period, parameters):
        passenger = person('commercially_transports_passengers_large_vehicle', period)
        goods = person('commercially_transports_goods_heavy_vehicle', period)
        return passenger | goods


class exempt_transports_only_own_employees(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Befördert mit Motorfahrzeugen ausschliesslich eigene Angestellte (Art. 3 Abs. 1ter lit. a)"
    reference = "SR 744.10 Art. 3 Abs. 1ter lit. a"

    def formula(person, period, parameters):
        return person('transports_exclusively_own_employees', period)


class exempt_transports_goods_for_own_services(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Befördert Güter ausschliesslich zur Erbringung eigener weitergehender Dienstleistungen (Art. 3 Abs. 1ter lit. b)"
    reference = "SR 744.10 Art. 3 Abs. 1ter lit. b"

    def formula(person, period, parameters):
        return person('transports_goods_exclusively_for_own_services_beyond_transport', period)


class exempt_uses_only_light_vans_domestic(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gewerbsmässige Güterbeförderung ausschliesslich mit Lieferwagen 2,5–3,5 t nur in der Schweiz (Art. 3 Abs. 1ter lit. c)"
    reference = "SR 744.10 Art. 3 Abs. 1ter lit. c"

    def formula(person, period, parameters):
        commercial_goods = person('commercial_goods_transport', period)
        weight_over_2_5t = person('vehicle_total_weight_exceeds_2_5_tonnes', period)
        weight_at_most_3_5t = person('vehicle_total_weight_at_most_3_5_tonnes', period)
        exclusively_switzerland = person('operates_exclusively_in_switzerland', period)
        return commercial_goods * weight_over_2_5t * weight_at_most_3_5t * exclusively_switzerland


class exempt_uses_only_slow_vehicles(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verwendet ausschliesslich Fahrzeuge mit zulässiger Höchstgeschwindigkeit von 40 km/h (Art. 3 Abs. 1ter lit. d)"
    reference = "SR 744.10 Art. 3 Abs. 1ter lit. d"

    def formula(person, period, parameters):
        return person('vehicles_max_permitted_speed_40kmh', period)


class exempt_from_road_transport_license(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Von der Zulassungspflicht befreit (Art. 3 Abs. 1ter)"
    reference = "SR 744.10 Art. 3 Abs. 1ter"

    def formula(person, period, parameters):
        a = person('exempt_transports_only_own_employees', period)
        b = person('exempt_transports_goods_for_own_services', period)
        c = person('exempt_uses_only_light_vans_domestic', period)
        d = person('exempt_uses_only_slow_vehicles', period)
        return a | b | c | d


class requires_road_transport_license(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Benötigt eine Zulassungsbewilligung als Strassentransportunternehmen (Art. 3 SR 744.10)"
    reference = "SR 744.10 Art. 3"

    def formula(person, period, parameters):
        subject = person('subject_to_road_transport_license_requirement', period)
        exempt = person('exempt_from_road_transport_license', period)
        return subject * ~exempt


class road_transport_license_validity_years(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Gültigkeitsdauer der Zulassungsbewilligung in Jahren (Art. 3 Abs. 2)"
    reference = "SR 744.10 Art. 3 Abs. 2"

    def formula(person, period, parameters):
        has_license = person('requires_road_transport_license', period)
        return has_license * 5


class must_carry_certified_license_copy(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Muss beglaubigte Kopie der Zulassungsbewilligung auf jedem Fahrzeug mitführen (Art. 3 Abs. 3)"
    reference = "SR 744.10 Art. 3 Abs. 3"

    def formula(person, period, parameters):
        return person('requires_road_transport_license', period)
