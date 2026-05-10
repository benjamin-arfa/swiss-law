"""SR 272.2 Art. 3

Generated from: ch/272/de/272.2.md

Ton- und Bilduebertragungssysteme: Anforderungen an Datenschutz und
Datensicherheit. Server muessen sich in der Schweiz oder einem
EU-Mitgliedstaat befinden. Verschluesselung ist obligatorisch.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class server_standort_schweiz_oder_eu(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob sich die Server in der Schweiz oder einem EU-Mitgliedstaat befinden"
    reference = "SR 272.2 Art. 3 Abs. 1 Bst. a"


class uebertragung_verschluesselt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Uebertragung waehrend des gesamten Vorgangs verschluesselt erfolgt"
    reference = "SR 272.2 Art. 3 Abs. 1 Bst. b"


class system_sicherheit_aktuell(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das System sicherheitstechnisch auf dem neusten Stand ist"
    reference = "SR 272.2 Art. 3 Abs. 1 Bst. c"


class aufnahme_funktionen_geschuetzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Aufnahme-/Uebertragungsfunktionen den Verfahrensbeteiligten nicht zugaenglich sind"
    reference = "SR 272.2 Art. 3 Abs. 1 Bst. d"


class anbieterin_sitz_schweiz_eu(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die private Anbieterin ihren Sitz in der Schweiz oder einem EU-Staat hat"
    reference = "SR 272.2 Art. 3 Abs. 2"


class daten_gegen_unbefugten_zugriff_geschuetzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Daten gegen unbefugte Einsichtnahme, Veraenderung usw. geschuetzt sind"
    reference = "SR 272.2 Art. 3 Abs. 2 Bst. a"


class daten_nach_verhandlung_vernichtet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Daten unmittelbar nach der Prozesshandlung vernichtet werden"
    reference = "SR 272.2 Art. 3 Abs. 2 Bst. b"


class system_erfuellt_anforderungen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Ton- und Bilduebertragungssystem alle Anforderungen erfuellt"
    reference = "SR 272.2 Art. 3"

    def formula(person, period, parameters):
        return (
            person('server_standort_schweiz_oder_eu', period)
            * person('uebertragung_verschluesselt', period)
            * person('system_sicherheit_aktuell', period)
            * person('aufnahme_funktionen_geschuetzt', period)
        )
