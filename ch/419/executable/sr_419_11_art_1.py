"""SR 419.11 Art. 1

Generated from: ch/419/de/419.11.md

Organisationen der Weiterbildung - Zusaetzliche Anforderungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class befasst_sich_mehrheitlich_mit_weiterbildung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Organisation befasst sich mehrheitlich mit Fragen der Weiterbildung"
    reference = "SR 419.11 Art. 1 Abs. 1 Bst. a"


class erbringt_uebergeordnete_leistungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Organisation erbringt uebergeordnete Leistungen fuer die Weiterbildung"
    reference = "SR 419.11 Art. 1 Abs. 1 Bst. b"


class taetig_in_de_fr_it_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Taetig in deutscher, franzoesischer und italienischer Schweiz"
    reference = "SR 419.11 Art. 1 Abs. 2"


class ueberregionale_auswirkungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Aktivitaet hat ueberregionale Auswirkungen in mehreren Sprachregionen"
    reference = "SR 419.11 Art. 1 Abs. 2"


class ist_gesamtschweizerisch_taetig_webiv(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Organisation ist gesamtschweizerisch taetig im Sinne der WeBiV"
    reference = "SR 419.11 Art. 1 Abs. 2"

    def formula(person, period, parameters):
        return (
            person('taetig_in_de_fr_it_schweiz', period) *
            person('ueberregionale_auswirkungen', period)
        )


class erfuellt_anforderungen_webiv_art_1(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erfuellt alle Anforderungen nach WeBiV Art. 1"
    reference = "SR 419.11 Art. 1"

    def formula(person, period, parameters):
        return (
            person('befasst_sich_mehrheitlich_mit_weiterbildung', period) *
            person('erbringt_uebergeordnete_leistungen', period) *
            person('ist_gesamtschweizerisch_taetig_webiv', period)
        )
