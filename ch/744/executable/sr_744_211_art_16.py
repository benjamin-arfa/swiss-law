"""SR 744.211 Art. 16

Generated from: ch/744/de/744.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class trolleybus_motorfahrzeugverkehr_vorschriften_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gelten für den Trolleybus-Strassenverkehr die Vorschriften der Bundesgesetzgebung über den Motorfahrzeugverkehr?"
    reference = "SR 744.211 Art. 16 Abs. 1"

    def formula(person, period, parameters):
        # Art. 16 Abs. 1: Für den Verkehr der Trolleybusse auf der Strasse gelten
        # die Vorschriften der Bundesgesetzgebung über den Motorfahrzeugverkehr.
        # This applies unconditionally to all trolleybus street traffic.
        return True


class trolleybus_maximale_fahrgeschwindigkeit_festgesetzt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wurde für den Trolleybus eine maximale Fahrgeschwindigkeit durch das Bundesamt festgesetzt?"
    reference = "SR 744.211 Art. 16 Abs. 2"

    def formula(person, period, parameters):
        # Art. 16 Abs. 2: Das Bundesamt kann maximale Fahrgeschwindigkeiten festsetzen,
        # wenn die Bauart der Fahrzeuge oder besondere Verhältnisse es rechtfertigen.
        besondere_bauart = person('trolleybus_besondere_bauart', period)
        besondere_verhaeltnisse = person('trolleybus_besondere_verhaeltnisse', period)
        return besondere_bauart + besondere_verhaeltnisse


class trolleybus_besondere_bauart(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Weist der Trolleybus eine besondere Bauart auf, die eine abweichende Höchstgeschwindigkeit rechtfertigt?"
    reference = "SR 744.211 Art. 16 Abs. 2"


class trolleybus_besondere_verhaeltnisse(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Liegen besondere Verhältnisse vor, die eine abweichende Höchstgeschwindigkeit für den Trolleybus rechtfertigen?"
    reference = "SR 744.211 Art. 16 Abs. 2"


class trolleybus_maximale_fahrgeschwindigkeit_kmh(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Vom Bundesamt festgesetzte maximale Fahrgeschwindigkeit für den Trolleybus (km/h)"
    reference = "SR 744.211 Art. 16 Abs. 2"

    def formula(person, period, parameters):
        # Only applies when a special speed limit has been set by the Federal Office.
        # Otherwise defaults to 0.0 (no special limit set; general rules apply).
        festgesetzt = person('trolleybus_maximale_fahrgeschwindigkeit_festgesetzt', period)
        return where(festgesetzt, person('trolleybus_festgesetzte_geschwindigkeit_wert', period), 0.0)


class trolleybus_festgesetzte_geschwindigkeit_wert(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Konkreter Geschwindigkeitswert (km/h), den das Bundesamt für den Trolleybus festgesetzt hat"
    reference = "SR 744.211 Art. 16 Abs. 2"
