"""SR 420.1 Art. 5

Generated from: ch/420/de/420.1.md

Nichtkommerzielle Forschungsstaetten ausserhalb des Hochschulbereichs - Voraussetzungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_nicht_forschungsorgan_art_4(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Institution ist kein Forschungsorgan nach Artikel 4"
    reference = "SR 420.1 Art. 5"


class zweck_ist_forschungstaetigkeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zweck der Institution ist Forschungstaetigkeit"
    reference = "SR 420.1 Art. 5"


class traeger_erlangen_keine_geldwerten_vorteile(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Traeger und Eigner erlangen durch Forschungstaetigkeit keine geldwerten Vorteile"
    reference = "SR 420.1 Art. 5 Bst. a"


class forschungsniveau_vergleichbar_mit_hochschulen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Niveau und Qualitaet der Forschung sind mit Hochschulforschungsstaetten vergleichbar"
    reference = "SR 420.1 Art. 5 Bst. b"


class ist_nichtkommerzielle_forschungsstaette(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist eine nichtkommerzielle Forschungsstaette ausserhalb des Hochschulbereichs"
    reference = "SR 420.1 Art. 5"

    def formula(person, period, parameters):
        return (
            person('ist_nicht_forschungsorgan_art_4', period) *
            person('zweck_ist_forschungstaetigkeit', period) *
            person('traeger_erlangen_keine_geldwerten_vorteile', period) *
            person('forschungsniveau_vergleichbar_mit_hochschulen', period)
        )
