"""SR 641.811 Art. 13 - Massgebendes Gewicht (Relevant weight)

The tax is based on the maximum permissible gross weight from the vehicle
registration. Maximum relevant weight is capped at 40 tonnes (Abs. 8).
For semi-trailer combinations: tractor empty weight + trailer gross weight.
For other combinations: sum of gross weights.

Generated from: ch/641/de/641.811.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class svav_fahrzeugausweis_gesamtgewicht_kg(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hoechstzulaessiges Gesamtgewicht gemaess Fahrzeugausweis in kg (Art. 13 Abs. 1 SVAV)"
    reference = "SR 641.811 Art. 13 Abs. 1"


class svav_ist_sattelfahrzeug(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Fahrzeug ist Sattelschlepper-Sattelanhaenger Kombination (Art. 13 Abs. 3 SVAV)"
    reference = "SR 641.811 Art. 13 Abs. 3"


class svav_sattelschlepper_leergewicht_kg(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Leergewicht des Sattelschleppers in kg (Art. 13 Abs. 3 SVAV)"
    reference = "SR 641.811 Art. 13 Abs. 3"


class svav_sattelanhaenger_gesamtgewicht_kg(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamtgewicht des Sattelanhaengers in kg (Art. 13 Abs. 3 SVAV)"
    reference = "SR 641.811 Art. 13 Abs. 3"


class svav_anhaenger_gesamtgewicht_kg(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamtgewicht des Anhaengers in kg (Art. 13 Abs. 4 SVAV)"
    reference = "SR 641.811 Art. 13 Abs. 4"


class svav_betriebsgewicht_kg(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hoechstzulaessiges Betriebsgewicht in kg (Art. 13 Abs. 7 SVAV)"
    reference = "SR 641.811 Art. 13 Abs. 7"


class svav_massgebendes_gewicht_kg(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Massgebendes Gewicht fuer Abgabeberechnung in kg (Art. 13 SVAV)"
    reference = "SR 641.811 Art. 13"

    def formula(person, period, parameters):
        ausweis_gw = person('svav_fahrzeugausweis_gesamtgewicht_kg', period)
        ist_sattel = person('svav_ist_sattelfahrzeug', period)
        sattel_leer = person('svav_sattelschlepper_leergewicht_kg', period)
        sattel_anh_gw = person('svav_sattelanhaenger_gesamtgewicht_kg', period)
        anh_gw = person('svav_anhaenger_gesamtgewicht_kg', period)
        betrieb_gw = person('svav_betriebsgewicht_kg', period)

        # Abs. 3: Semi-trailer combo = tractor empty + trailer gross
        sattel_gewicht = sattel_leer + sattel_anh_gw

        # Abs. 4: Other combos = sum of gross weights
        kombi_gewicht = ausweis_gw + anh_gw

        # Choose based on vehicle type
        basis_gewicht = ist_sattel * sattel_gewicht + (1 - ist_sattel) * kombi_gewicht

        # Use ausweis weight if no combo
        hat_kombi = (anh_gw > 0) + ist_sattel
        gewicht = hat_kombi * basis_gewicht + (1 - hat_kombi) * ausweis_gw

        # Abs. 7: Cap at operating weight if lower
        hat_betrieb = betrieb_gw > 0
        gewicht = hat_betrieb * min_(gewicht, betrieb_gw) + (1 - hat_betrieb) * gewicht

        # Abs. 8: Maximum 40 tonnes
        return min_(gewicht, 40000)
