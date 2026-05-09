"""SR 614.0 Art. 13

Generated from: ch/614/de/614.0.md

Finanzkontrollgesetz (FKG) - Art. 13: Zusammenarbeit mit andern Kontrollstellen.
EFK koordiniert mit Parlamentarischer Verwaltungskontrollstelle und meldet
Maengel an Querschnittsaemter.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class efk_koordiniert_mit_pvk(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK tauscht mit der Parlamentarischen Verwaltungskontrollstelle "
        "die Revisions- bzw. Pruefungsprogramme aus und koordiniert ihre "
        "Taetigkeit (Art. 13 Abs. 1)"
    )
    reference = "SR 614.0 Art. 13 Abs. 1"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_meldet_maengel_an_querschnittsaemter(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK teilt Maengel in Organisation, Verwaltungsfuehrung oder "
        "Aufgabenerfuellung den betroffenen Querschnittsaemtern mit (Art. 13 Abs. 2)"
    )
    reference = "SR 614.0 Art. 13 Abs. 2"

    def formula(person, period, parameters):
        ist_efk = person('ist_eidgenoessische_finanzkontrolle', period)
        maengel_festgestellt = person('efk_hat_maengel_festgestellt', period)
        return ist_efk * maengel_festgestellt


class efk_hat_maengel_festgestellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "EFK hat Maengel in Organisation, Verwaltungsfuehrung oder Aufgabenerfuellung festgestellt"
    reference = "SR 614.0 Art. 13 Abs. 2"


class efk_informiert_bj_gesetzgebungsluecken(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK informiert das Bundesamt fuer Justiz bei Luecken oder Maengeln "
        "in der Gesetzgebung (Art. 13 Abs. 3)"
    )
    reference = "SR 614.0 Art. 13 Abs. 3"

    def formula(person, period, parameters):
        ist_efk = person('ist_eidgenoessische_finanzkontrolle', period)
        luecken = person('efk_hat_gesetzgebungsluecken_festgestellt', period)
        return ist_efk * luecken


class efk_hat_gesetzgebungsluecken_festgestellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "EFK hat Luecken oder Maengel in der Gesetzgebung festgestellt"
    reference = "SR 614.0 Art. 13 Abs. 3"
