"""SR 744.103 Art. 5a

Generated from: ch/744/de/744.103.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_geschaeftsraeume_mit_unternehmensunterlagen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verfügt über Räumlichkeiten mit Originalen der wichtigsten Unternehmensunterlagen (zugänglich für BAV)"
    reference = "SR 744.103 Art. 5a Bst. a"

    def formula(person, period, parameters):
        return person('hat_zugaengliche_geschaeftsraeume', period)


class hat_angemessene_fahrzeuge_und_fahrer(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verfügt dauerhaft über angemessene Anzahl zugelassener Fahrzeuge und Fahrer im Verhältnis zur Verkehrstätigkeit"
    reference = "SR 744.103 Art. 5a Bst. b"

    def formula(person, period, parameters):
        hat_zulassung = person('hat_zulassung_strassentransportunternehmen', period)
        angemessene_fahrzeuge = person('hat_angemessene_anzahl_fahrzeuge', period)
        angemessene_fahrer = person('hat_angemessene_anzahl_fahrer', period)
        return hat_zulassung * angemessene_fahrzeuge * angemessene_fahrer


class uebst_administrative_taetigkeiten_tatsaechlich_aus(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Übt administrative und gewerbliche Tätigkeiten tatsächlich und dauerhaft mit angemessener Ausstattung aus"
    reference = "SR 744.103 Art. 5a Bst. c"

    def formula(person, period, parameters):
        return person('hat_angemessene_administrative_ausstattung', period)


class uebst_verkehrstaetigkeiten_tatsaechlich_aus(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Übt Verkehrstätigkeit tatsächlich und dauerhaft mit angemessener technischer Ausstattung aus"
    reference = "SR 744.103 Art. 5a Bst. d"

    def formula(person, period, parameters):
        return person('hat_angemessene_technische_fahrzeugausstattung', period)


class nachweis_tatsaechlicher_und_dauerhafter_sitz_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Nachweis des tatsächlichen und dauerhaften Sitzes in der Schweiz als Strassentransportunternehmen"
    reference = "SR 744.103 Art. 5a"

    def formula(person, period, parameters):
        bedingung_a = person('hat_geschaeftsraeume_mit_unternehmensunterlagen', period)
        bedingung_b = person('hat_angemessene_fahrzeuge_und_fahrer', period)
        bedingung_c = person('uebst_administrative_taetigkeiten_tatsaechlich_aus', period)
        bedingung_d = person('uebst_verkehrstaetigkeiten_tatsaechlich_aus', period)
        return bedingung_a * bedingung_b * bedingung_c * bedingung_d
