"""SR 366.1 Art. 11

Generated from: ch/366/de/366.1.md

Bedingungen des Informationsaustauschs: Zweckbindung und Zustimmungserfordernis.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class daten_weitergabe_an_nicht_polizei(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Daten sollen an Stellen weitergegeben werden, die keine Strafverfolgungsbehoerden sind"
    reference = "SR 366.1 Art. 11 Abs. 3 Bst. a"


class nzb_zustimmung_erteilt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "NZB hat die ausdrueckliche Zustimmung im Einzelfall erteilt"
    reference = "SR 366.1 Art. 11 Abs. 3 Bst. a"


class daten_weitergabe_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Weitergabe von Daten an nicht-polizeiliche Stellen ist zulaessig"
    reference = "SR 366.1 Art. 11 Abs. 3 Bst. a"

    def formula(person, period, parameters):
        an_nicht_polizei = person('daten_weitergabe_an_nicht_polizei', period)
        zustimmung = person('nzb_zustimmung_erteilt', period)
        return an_nicht_polizei * zustimmung


class person_ist_asylsuchend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist Asylsuchend, anerkannter Fluechtling oder schutzbeduerftigt"
    reference = "SR 366.1 Art. 11 Abs. 5"


class daten_an_heimatstaat(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Daten sollen an den Heimat- oder Herkunftsstaat bekanntgegeben werden"
    reference = "SR 366.1 Art. 11 Abs. 5"
