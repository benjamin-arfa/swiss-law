"""SR 432.219 Art. 2

Generated from: ch/432/de/432.219.md

Gebuehrenfreiheit - bestimmte Dienstleistungen der Nationalbibliothek sind gebuehrenfrei.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_ausleihe_werk(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Dienstleistung ist eine Ausleihe von Werken"
    reference = "SR 432.219 Art. 2 Bst. a"


class ist_oeffentliche_fuehrung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Dienstleistung ist eine oeffentliche Fuehrung der Nationalbibliothek"
    reference = "SR 432.219 Art. 2 Bst. b"


class ist_benutzung_literaturarchiv(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Dienstleistung ist die Benutzung des Literaturarchivs oder der Nationalphonothek"
    reference = "SR 432.219 Art. 2 Bst. c"


class ist_benutzung_pc_arbeitsplatz(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Dienstleistung ist die Benutzung allgemein zugaenglicher PC-Arbeitsplaetze"
    reference = "SR 432.219 Art. 2 Bst. d"


class ist_benutzung_lesesaal(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Dienstleistung ist die Benutzung der Lesesaele und aufliegender Periodika"
    reference = "SR 432.219 Art. 2 Bst. e"


class ist_dokumentationsauftrag(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Dienstleistung ist ein Dokumentations- oder Forschungsauftrag nach Art. 8 NBibG"
    reference = "SR 432.219 Art. 2 Bst. f"


class dienstleistung_gebuehrenfrei(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Dienstleistung der Nationalbibliothek ist gebuehrenfrei"
    reference = "SR 432.219 Art. 2"

    def formula(person, period, parameters):
        return (
            person('ist_ausleihe_werk', period) +
            person('ist_oeffentliche_fuehrung', period) +
            person('ist_benutzung_literaturarchiv', period) +
            person('ist_benutzung_pc_arbeitsplatz', period) +
            person('ist_benutzung_lesesaal', period) +
            person('ist_dokumentationsauftrag', period)
        ) > 0
