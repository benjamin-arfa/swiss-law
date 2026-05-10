"""SR 418.0 Art. 3

Generated from: ch/418/de/418.0.md

Voraussetzungen fuer die Anerkennung von Schweizerschulen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# --- Input variables (Anerkennungsvoraussetzungen) ---

class hat_unterrichtsbewilligung_gastland(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Besitzt Unterrichtsbewilligung des Gastlandes"
    reference = "SR 418.0 Art. 3 Abs. 1 Bst. a"


class gewaehr_langfristiger_bestand(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bietet angemessen Gewaehr fuer langfristigen Bestand"
    reference = "SR 418.0 Art. 3 Abs. 1 Bst. b"


class gemeinnuetziger_charakter(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat gemeinnuetzigen Charakter"
    reference = "SR 418.0 Art. 3 Abs. 1 Bst. c"


class schulgeldbefreiung_fuer_beduerftige(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erlaesst Auslandschweizern das Schulgeld bei Beduerfigkeit"
    reference = "SR 418.0 Art. 3 Abs. 1 Bst. d"


class politisch_religioes_neutral(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bietet Gewaehr fuer politisch und religioes neutrale Bildung"
    reference = "SR 418.0 Art. 3 Abs. 1 Bst. e"


class angemessener_minimalbestand_schueler(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Weist angemessenen Minimalbestand an Schuelerinnen und Schuelern auf"
    reference = "SR 418.0 Art. 3 Abs. 1 Bst. f"


class unterricht_in_landessprache(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vermittelt Unterricht zu angemessenem Teil in einer Landessprache"
    reference = "SR 418.0 Art. 3 Abs. 1 Bst. g"


class fuehrt_kindergarten_und_primarstufe(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fuehrt Kindergarten und Primarstufe sowie Sekundarstufe I (oder plant)"
    reference = "SR 418.0 Art. 3 Abs. 1 Bst. h"


class unterricht_durch_ch_lehrberechtigung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unterricht mehrheitlich durch Personen mit schweizerischer Lehrberechtigung"
    reference = "SR 418.0 Art. 3 Abs. 1 Bst. i"


class lehrprogramm_uebertrittskonform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Lehrprogramm ermoeglicht Uebertritt in CH oder Gastland"
    reference = "SR 418.0 Art. 3 Abs. 1 Bst. j"


class hat_patronatskanton(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat Patronatsverhaeltnis mit einem Kanton"
    reference = "SR 418.0 Art. 3 Abs. 1 Bst. k"


class schulsystem_begutachtet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schulsystem vom Patronatskanton begutachtet"
    reference = "SR 418.0 Art. 3 Abs. 1 Bst. l"


class statuten_gesetzeskonform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Statuten in Einklang mit dem Gesetz"
    reference = "SR 418.0 Art. 3 Abs. 1 Bst. m"


class schweizerische_traegerschaft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schweizerische Traegerschaft mit Fuehrungsgremium mehrheitlich CH-Staatsangehoerige"
    reference = "SR 418.0 Art. 3 Abs. 1 Bst. n"


class schulleitung_mit_ch_lehrberechtigung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schulleitung mit schweizerischer Lehrberechtigung"
    reference = "SR 418.0 Art. 3 Abs. 1 Bst. o"


class aufnahme_ch_kinder_gewaehrt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gewaehrt allen CH-Kindern Aufnahme"
    reference = "SR 418.0 Art. 3 Abs. 1 Bst. p"


# --- Computed variables ---

class schweizerschule_anerkennungsvoraussetzungen_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Alle Voraussetzungen fuer Anerkennung als Schweizerschule erfuellt"
    reference = "SR 418.0 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        return (
            person('hat_unterrichtsbewilligung_gastland', period) *
            person('gewaehr_langfristiger_bestand', period) *
            person('gemeinnuetziger_charakter', period) *
            person('schulgeldbefreiung_fuer_beduerftige', period) *
            person('politisch_religioes_neutral', period) *
            person('angemessener_minimalbestand_schueler', period) *
            person('unterricht_in_landessprache', period) *
            person('fuehrt_kindergarten_und_primarstufe', period) *
            person('unterricht_durch_ch_lehrberechtigung', period) *
            person('lehrprogramm_uebertrittskonform', period) *
            person('hat_patronatskanton', period) *
            person('schulsystem_begutachtet', period) *
            person('statuten_gesetzeskonform', period) *
            person('schweizerische_traegerschaft', period) *
            person('schulleitung_mit_ch_lehrberechtigung', period) *
            person('aufnahme_ch_kinder_gewaehrt', period)
        )
