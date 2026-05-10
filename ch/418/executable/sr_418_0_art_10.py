"""SR 418.0 Art. 10

Generated from: ch/418/de/418.0.md

Art, Umfang und Bemessung der Finanzhilfen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# --- Input variables ---

class gesamtbestand_schueler(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Gesamtbestand an Schuelerinnen und Schuelern sowie Lernenden"
    reference = "SR 418.0 Art. 10 Abs. 2 Bst. a"


class anzahl_schueler_ch_staatsangehoerigkeit(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Schueler mit Schweizer Staatsangehoerigkeit"
    reference = "SR 418.0 Art. 10 Abs. 2 Bst. b"


class anzahl_lehrpersonen_ch_lehrberechtigung_vze(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anzahl Personen mit CH-Lehrberechtigung in Vollzeitaequivalenten"
    reference = "SR 418.0 Art. 10 Abs. 2 Bst. c"


class anzahl_unterrichtssprachen_ch_landessprachen(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Unterrichtssprachen die CH-Landessprachen und nicht Gastlandsprachen sind"
    reference = "SR 418.0 Art. 10 Abs. 2 Bst. d"


class gastland_schreibt_einheimische_lehrpersonen_vor(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gastland schreibt Anstellung einheimischer Lehrpersonen vor"
    reference = "SR 418.0 Art. 10 Abs. 4 Bst. a"


class paedagogische_gruende_fuer_nicht_ch_lehrpersonen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ueberzeugende paedagogische Gruende fuer Einsatz nicht-CH-Lehrpersonen"
    reference = "SR 418.0 Art. 10 Abs. 4 Bst. b"


# --- Computed variables ---

class beitraege_fuer_nicht_ch_lehrpersonen_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Beitraege fuer Lehrpersonen ohne CH-Lehrberechtigung zulaessig"
    reference = "SR 418.0 Art. 10 Abs. 4"

    def formula(person, period, parameters):
        gastland = person('gastland_schreibt_einheimische_lehrpersonen_vor', period)
        paedagogisch = person('paedagogische_gruende_fuer_nicht_ch_lehrpersonen', period)
        return gastland + paedagogisch
