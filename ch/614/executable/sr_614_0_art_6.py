"""SR 614.0 Art. 6

Generated from: ch/614/de/614.0.md

Art. 6: Einzelne Kontrollaufgaben - Die EFK hat insbesondere folgende Aufgaben:
Überprüfung des Finanzhaushalts, Staatsrechnung, Kreditkontrolle, interne
Kontrollsysteme, Zahlungsanweisungen, Verwaltungsrevision, Monopolpreise,
EDV-Sicherheit und internationale Kontrollmandate.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class efk_prueft_finanzhaushalt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK überprüft den gesamten Finanzhaushalt auf allen Stufen des "
        "Vollzugs des Voranschlags (Art. 6 lit. a)"
    )
    reference = "SR 614.0 Art. 6 lit. a"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_prueft_staatsrechnung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "EFK überprüft die Erstellung der Staatsrechnung (Art. 6 lit. b)"
    reference = "SR 614.0 Art. 6 lit. b"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_prueft_kreditkontrolle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK achtet auf Kreditkontrolle und prüft Bewirtschaftung der "
        "Verpflichtungskredite (Art. 6 lit. c)"
    )
    reference = "SR 614.0 Art. 6 lit. c"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_prueft_interne_kontrollsysteme(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "EFK überprüft die internen Kontrollsysteme (Art. 6 lit. d)"
    reference = "SR 614.0 Art. 6 lit. d"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_prueft_zahlungsanweisungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK überprüft durch Stichproben die von den Verwaltungseinheiten "
        "ausgestellten Zahlungsanweisungen (Art. 6 lit. e)"
    )
    reference = "SR 614.0 Art. 6 lit. e"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_besorgt_revision_verwaltungseinheiten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK besorgt die Revision der Verwaltungseinheiten, einschliesslich "
        "Buchhaltungen und Bestände (Art. 6 lit. f)"
    )
    reference = "SR 614.0 Art. 6 lit. f"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_prueft_monopolpreise(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK prüft im Rahmen des Einkaufswesens des Bundes, ob Monopolpreise "
        "angemessen sind (Art. 6 lit. g)"
    )
    reference = "SR 614.0 Art. 6 lit. g"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_prueft_edv_sicherheit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK prüft, ob EDV-Anwendungen in Bereichen des Finanzgebarens die "
        "erforderliche Sicherheit und Funktionalität aufweisen (Art. 6 lit. h)"
    )
    reference = "SR 614.0 Art. 6 lit. h"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_kontrollmandate_international(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK nimmt Kontrollmandate bei internationalen Organisationen "
        "wahr (Art. 6 lit. i)"
    )
    reference = "SR 614.0 Art. 6 lit. i"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_prueft_finanzausgleich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK prüft die Berechnungen des Ressourcen- und Lastenausgleichs "
        "nach dem FiLaG (Art. 6 lit. j)"
    )
    reference = "SR 614.0 Art. 6 lit. j"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)
