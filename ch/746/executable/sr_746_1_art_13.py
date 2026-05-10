"""SR 746.1 Art. 13

Generated from: ch/746/de/746.1.md

Transportpflicht fuer Dritte.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class rohrleitungsunternehmung_transportpflicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rohrleitungsunternehmung ist verpflichtet, Transporte fuer Dritte zu uebernehmen"
    reference = "SR 746.1 Art. 13 Abs. 1"

    def formula(person, period, parameters):
        # Art. 13 Abs. 1: Die Unternehmung ist verpflichtet, vertraglich
        # Transporte fuer Dritte zu uebernehmen, wenn sie technisch moeglich
        # und wirtschaftlich zumutbar sind, und wenn der Dritte eine
        # angemessene Gegenleistung anbietet.
        unterliegt_rlg = person('unterliegt_rohrleitungsgesetz_voll', period)
        transport_technisch_moeglich = person('rohrleitung_transport_technisch_moeglich', period)
        transport_wirtschaftlich_zumutbar = person('rohrleitung_transport_wirtschaftlich_zumutbar', period)
        angemessene_gegenleistung = person('rohrleitung_angemessene_gegenleistung', period)
        return (unterliegt_rlg
                * transport_technisch_moeglich
                * transport_wirtschaftlich_zumutbar
                * angemessene_gegenleistung)


class rohrleitung_transport_technisch_moeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Transport fuer Dritte ist technisch moeglich"
    reference = "SR 746.1 Art. 13 Abs. 1"


class rohrleitung_transport_wirtschaftlich_zumutbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Transport fuer Dritte ist wirtschaftlich zumutbar"
    reference = "SR 746.1 Art. 13 Abs. 1"


class rohrleitung_angemessene_gegenleistung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Dritter bietet angemessene Gegenleistung fuer den Transport"
    reference = "SR 746.1 Art. 13 Abs. 1"
