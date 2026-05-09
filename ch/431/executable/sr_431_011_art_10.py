"""SR 431.011 Art. 10

Generated from: ch/431/de/431.011.md

Datenschutz und Datensicherheit - Verweis auf DSG und DSV fuer Personendaten
und Informationssicherheitsverordnung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class bearbeitet_personendaten_statistik(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bearbeitet Personendaten im Rahmen der Bundesstatistik"
    reference = "SR 431.011 Art. 10 Abs. 1"


class datenschutzgesetz_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Datenschutzgesetz (DSG) ist auf die Datenbearbeitung anwendbar"
    reference = "SR 431.011 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        return person('bearbeitet_personendaten_statistik', period)


class bearbeitet_daten_juristischer_personen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bearbeitet Daten juristischer Personen im Rahmen der Bundesstatistik"
    reference = "SR 431.011 Art. 10 Abs. 2"


class dsv_sinngemäss_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "DSV ist sinngemäss auf Daten juristischer Personen anwendbar"
    reference = "SR 431.011 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        return person('bearbeitet_daten_juristischer_personen', period)
