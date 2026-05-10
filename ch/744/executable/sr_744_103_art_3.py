"""SR 744.103 Art. 3

Generated from: ch/744/de/744.103.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class equity_and_reserves(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Eigenkapital und Reserven des Unternehmens (CHF)"
    reference = "SR 744.103 Art. 3"


class num_vehicles_over_35t(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Fahrzeuge über 3,5 Tonnen (Güterverkehr)"
    reference = "SR 744.103 Art. 3 Abs. 1"


class num_vehicles_25_to_35t(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Fahrzeuge mit Gesamtgewicht über 2,5 bis 3,5 Tonnen"
    reference = "SR 744.103 Art. 3 Abs. 1 Bst. c"


class num_passenger_vehicles(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Fahrzeuge im Personenverkehr"
    reference = "SR 744.103 Art. 3 Abs. 3"


class is_goods_transport_company(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen ist im Güterverkehr tätig"
    reference = "SR 744.103 Art. 3 Abs. 1"


class is_passenger_transport_company(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen ist im Personenverkehr tätig"
    reference = "SR 744.103 Art. 3 Abs. 3"


class has_valid_bank_guarantee(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gültige Bankgarantie vorhanden, die finanzielle Leistungsfähigkeit für Dauer der Zulassungsbewilligung sicherstellt"
    reference = "SR 744.103 Art. 3 Abs. 5"


class required_financial_capacity_sr_744_103_art3(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Mindestbetrag Eigenkapital und Reserven gemäss SR 744.103 Art. 3 (CHF)"
    reference = "SR 744.103 Art. 3"

    def formula(person, period, parameters):
        n_heavy = person('num_vehicles_over_35t', period)
        n_medium = person('num_vehicles_25_to_35t', period)
        n_passenger = person('num_passenger_vehicles', period)
        is_goods = person('is_goods_transport_company', period)
        is_passenger = person('is_passenger_transport_company', period)

        # Art. 3 Abs. 1: Güterverkehr mit mindestens einem Fahrzeug über 3,5 t
        # 9000 für erstes schweres Fahrzeug + 5000 je weiteres schweres + 900 je mittleres
        goods_with_heavy = (
            9000.0
            + max_(n_heavy - 1, 0) * 5000.0
            + n_medium * 900.0
        )

        # Art. 3 Abs. 2: Güterverkehr ausschliesslich mit Fahrzeugen 2,5–3,5 t
        # 1800 für erstes + 900 je weiteres
        goods_medium_only = (
            1800.0
            + max_(n_medium - 1, 0) * 900.0
        )

        # Art. 3 Abs. 3: Personenverkehr
        # 9000 für erstes + 5000 je weiteres
        passenger_required = (
            9000.0
            + max_(n_passenger - 1, 0) * 5000.0
        )

        # Art. 3 Abs. 4: Gemischter Betrieb (Personen- und Güterverkehr)
        # 9000 für das erste Fahrzeug (beliebige Kategorie)
        # Weitere Fahrzeuge: schwere Güter 5000 (Abs. 1b), mittlere Güter 900 (Abs. 1c), Personen 5000 (Abs. 3)
        mixed_first_heavy = (
            9000.0
            + max_(n_heavy - 1, 0) * 5000.0
            + n_medium * 900.0
            + n_passenger * 5000.0
        )
        mixed_first_medium = (
            9000.0
            + max_(n_medium - 1, 0) * 900.0
            + n_passenger * 5000.0
        )
        mixed_required = where(
            n_heavy >= 1,
            mixed_first_heavy,
            where(n_medium >= 1, mixed_first_medium, passenger_required)
        )

        # Art. 3 Abs. 1 vs. Abs. 2 für reine Güterverkehrsunternehmen
        goods_required = where(n_heavy >= 1, goods_with_heavy, goods_medium_only)

        is_mixed = is_goods * is_passenger
        is_goods_only = is_goods * ~is_passenger
        is_passenger_only = ~is_goods * is_passenger

        return where(
            is_mixed,
            mixed_required,
            where(
                is_goods_only,
                goods_required,
                where(is_passenger_only, passenger_required, 0.0)
            )
        )


class is_financially_capable_sr_744_103_art3(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Finanzielle Leistungsfähigkeit gemäss SR 744.103 Art. 3"
    reference = "SR 744.103 Art. 3"

    def formula(person, period, parameters):
        equity = person('equity_and_reserves', period)
        required = person('required_financial_capacity_sr_744_103_art3', period)
        bank_guarantee = person('has_valid_bank_guarantee', period)

        # Art. 3 Abs. 5: Bankgarantie kann fehlende Eigenmittel ersetzen
        meets_equity_threshold = equity >= required
        return meets_equity_threshold + bank_guarantee * ~meets_equity_threshold
