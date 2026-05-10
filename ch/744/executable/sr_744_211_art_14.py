"""SR 744.211 Art. 14

Generated from: ch/744/de/744.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class trolleybus_kontrolle_nummer_serie_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeugkontrolle enthält Nummer und Seriebezeichnung (Art. 14 lit. a)"
    reference = "SR 744.211 Art. 14 lit. a"


class trolleybus_kontrolle_ersteller_inbetriebsetzung_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeugkontrolle enthält Namen der Ersteller und Datum der Inbetriebsetzung (Art. 14 lit. b)"
    reference = "SR 744.211 Art. 14 lit. b"


class trolleybus_kontrolle_verwendung_fahrleistungen_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeugkontrolle enthält Art der Verwendung und Fahrleistungen (Art. 14 lit. c)"
    reference = "SR 744.211 Art. 14 lit. c"


class trolleybus_kontrolle_revisionen_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeugkontrolle enthält Datum, Umfang und Ergebnisse der Fahrzeugrevisionen (Art. 14 lit. d)"
    reference = "SR 744.211 Art. 14 lit. d"


class trolleybus_kontrolle_bremsproben_druckproben_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeugkontrolle enthält Datum und Ergebnisse der Bremsproben sowie Druckproben der Luftbehälter (Art. 14 lit. e)"
    reference = "SR 744.211 Art. 14 lit. e"


class trolleybus_kontrolle_reparaturen_aenderungen_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeugkontrolle enthält wichtige Reparaturen, Änderungen und Teileersatz mit Datum (Art. 14 lit. f)"
    reference = "SR 744.211 Art. 14 lit. f"


class trolleybus_kontrolle_ausserordentliche_vorkommnisse_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeugkontrolle enthält ausserordentliche Vorkommnisse (Art. 14 lit. g)"
    reference = "SR 744.211 Art. 14 lit. g"


class trolleybus_fahrzeugkontrolle_pflicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pflicht zur Führung einer Fahrzeugkontrolle für jeden Trolleybus und Anhänger"
    reference = "SR 744.211 Art. 14"

    def formula(person, period, parameters):
        # Unconditional obligation for the undertaking operating trolleybuses or trailers
        return True


class trolleybus_fahrzeugkontrolle_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeugkontrolle erfüllt alle Anforderungen gemäss Art. 14 lit. a–g"
    reference = "SR 744.211 Art. 14"

    def formula(person, period, parameters):
        pflicht = person('trolleybus_fahrzeugkontrolle_pflicht', period)

        lit_a = person('trolleybus_kontrolle_nummer_serie_vorhanden', period)
        lit_b = person('trolleybus_kontrolle_ersteller_inbetriebsetzung_vorhanden', period)
        lit_c = person('trolleybus_kontrolle_verwendung_fahrleistungen_vorhanden', period)
        lit_d = person('trolleybus_kontrolle_revisionen_vorhanden', period)
        lit_e = person('trolleybus_kontrolle_bremsproben_druckproben_vorhanden', period)
        lit_f = person('trolleybus_kontrolle_reparaturen_aenderungen_vorhanden', period)
        lit_g = person('trolleybus_kontrolle_ausserordentliche_vorkommnisse_vorhanden', period)

        alle_eintraege = lit_a * lit_b * lit_c * lit_d * lit_e * lit_f * lit_g

        return pflicht * alle_eintraege
