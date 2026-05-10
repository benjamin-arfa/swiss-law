"""SR 235.1 Art. 17

Generated from: ch/235/de/235.1.md

Rechtsgrundlagen: Voraussetzungen fuer Bearbeitung von Personendaten
durch Bundesorgane.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_gesetzliche_grundlage_vorhanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesetzliche Grundlage fuer die Bearbeitung von Personendaten durch Bundesorgan besteht"
    reference = "SR 235.1 Art. 17 Abs. 1"


class dsg_gesetz_formell_sieht_vor(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesetz im formellen Sinn sieht Bearbeitung besonders schuetzenswerter Daten ausdruecklich vor"
    reference = "SR 235.1 Art. 17 Abs. 2"


class dsg_aufgabe_unentbehrlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bearbeitung ist fuer klar umschriebene gesetzliche Aufgabe unentbehrlich"
    reference = "SR 235.1 Art. 17 Abs. 2 lit. a"


class dsg_bundesrat_bewilligung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bundesrat hat Bearbeitung im Einzelfall bewilligt"
    reference = "SR 235.1 Art. 17 Abs. 2 lit. b"


class dsg_bundesorgan_darf_bearbeiten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bundesorgan darf Personendaten bearbeiten"
    reference = "SR 235.1 Art. 17"

    def formula(person, period, parameters):
        gesetzl = person('dsg_gesetzliche_grundlage_vorhanden', period)
        besonders = person('dsg_besonders_schuetzenswerte_daten', period)
        formell = person('dsg_gesetz_formell_sieht_vor', period)
        unentbehrlich = person('dsg_aufgabe_unentbehrlich', period)
        br_bewilligung = person('dsg_bundesrat_bewilligung', period)
        einwilligung = person('dsg_einwilligung_des_verletzten', period)
        zugaenglich = person('dsg_daten_allgemein_zugaenglich_gemacht', period)

        # Abs. 1: Gesetzliche Grundlage erforderlich
        # Abs. 2: Fuer besonders schuetzenswerte Daten zusaetzlich:
        # formelles Gesetz ODER unentbehrlich ODER BR-Bewilligung ODER Einwilligung/zugaenglich
        normal = gesetzl * not_(besonders)
        besonders_ok = gesetzl * besonders * (
            formell + unentbehrlich + br_bewilligung + einwilligung + zugaenglich > 0
        )
        return normal + besonders_ok > 0
