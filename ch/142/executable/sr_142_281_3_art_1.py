"""SR 142.281.3 Art. 1

Generated from: ch/142/de/142.281.3.md

Bereiche, anrechenbare Flaechen und Bereichspreise fuer Baubeitraege
des Bundes an Einrichtungen fuer den Vollzug auslaenderrechtlicher
Zwangsmassnahmen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input: number of detention places
class anzahl_haftplaetze(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Haftplaetze der Einrichtung"
    reference = "SR 142.281.3 Art. 1"


# Area per detention place per category (in m2)
class bereich_sicherheit_flaeche(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anrechenbare Flaeche Bereich Sicherheit pro Haftplatz (m2)"
    reference = "SR 142.281.3 Art. 1"
    default_value = 1.7


class bereich_verwaltung_flaeche(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anrechenbare Flaeche Bereich Verwaltung pro Haftplatz (m2)"
    reference = "SR 142.281.3 Art. 1"
    default_value = 1.9


class bereich_migrationsbehoerden_flaeche(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anrechenbare Flaeche Bereich Migrationsbehoerden pro Haftplatz (m2, bis 1.6)"
    reference = "SR 142.281.3 Art. 1"
    default_value = 1.6


class bereich_personal_flaeche(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anrechenbare Flaeche Bereich Personal pro Haftplatz (m2)"
    reference = "SR 142.281.3 Art. 1"
    default_value = 1.6


class bereich_insassenwesen_flaeche(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anrechenbare Flaeche Bereich Insassenwesen pro Haftplatz (m2)"
    reference = "SR 142.281.3 Art. 1"
    default_value = 7.4


class bereich_aufnahme_austritt_flaeche(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anrechenbare Flaeche Bereich Aufnahme/Austritt pro Haftplatz (m2)"
    reference = "SR 142.281.3 Art. 1"
    default_value = 2.1


class bereich_transport_flaeche(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anrechenbare Flaeche Bereich Transport pro Haftplatz (m2, bis 1.1)"
    reference = "SR 142.281.3 Art. 1"
    default_value = 1.1


class bereich_wohnen_flaeche(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anrechenbare Flaeche Bereich Wohnen pro Haftplatz (m2)"
    reference = "SR 142.281.3 Art. 1"
    default_value = 16.4


class bereich_beschaeftigung_flaeche(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anrechenbare Flaeche Bereich Beschaeftigung pro Haftplatz (m2)"
    reference = "SR 142.281.3 Art. 1"
    default_value = 8.6


class bereich_hauswirtschaft_flaeche(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anrechenbare Flaeche Bereich Hauswirtschaft pro Haftplatz (m2)"
    reference = "SR 142.281.3 Art. 1"
    default_value = 5.7


# Area prices per m2 per category (CHF, index 1 Oct 2010)
BEREICHSPREISE = {
    'sicherheit': 5300,
    'verwaltung': 5300,
    'migrationsbehoerden': 5300,
    'personal': 5100,
    'insassenwesen': 5100,
    'aufnahme_austritt': 5100,
    'transport': 5100,
    'wohnen': 6700,
    'beschaeftigung': 3600,
    'hauswirtschaft': 6700,
}


class gesamtflaeche_pro_haftplatz(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamtflaeche pro Haftplatz (bis 48.1 m2)"
    reference = "SR 142.281.3 Art. 1"

    def formula(person, period, parameters):
        return (
            person('bereich_sicherheit_flaeche', period)
            + person('bereich_verwaltung_flaeche', period)
            + person('bereich_migrationsbehoerden_flaeche', period)
            + person('bereich_personal_flaeche', period)
            + person('bereich_insassenwesen_flaeche', period)
            + person('bereich_aufnahme_austritt_flaeche', period)
            + person('bereich_transport_flaeche', period)
            + person('bereich_wohnen_flaeche', period)
            + person('bereich_beschaeftigung_flaeche', period)
            + person('bereich_hauswirtschaft_flaeche', period)
        )
