"""SR 744.21 Art. 17

Generated from: ch/744/de/744.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class schwere_zuwiderhandlung_konzession(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schwere Zuwiderhandlung gegen das Gesetz, Vollziehungsvorschriften oder Konzessionsbestimmungen (SR 744.21 Art. 17 Abs. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1926/493_515_514/de#art_17"

    def formula(person, period, parameters):
        return person('schwere_zuwiderhandlung_konzession_sachverhalt', period)


class wiederholte_zuwiderhandlung_konzession(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wiederholte Zuwiderhandlung gegen das Gesetz, Vollziehungsvorschriften oder Konzessionsbestimmungen (SR 744.21 Art. 17 Abs. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1926/493_515_514/de#art_17"

    def formula(person, period, parameters):
        return person('wiederholte_zuwiderhandlung_konzession_sachverhalt', period)


class konzession_gegenstandslos(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Konzession ist gegenstandslos geworden (SR 744.21 Art. 17 Abs. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1926/493_515_514/de#art_17"

    def formula(person, period, parameters):
        return person('konzession_gegenstandslos_sachverhalt', period)


class konzession_aufhebung_ohne_entschaedigung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Aufhebung der Konzession ohne Entschädigung durch das Departement zulässig (SR 744.21 Art. 17 Abs. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1926/493_515_514/de#art_17"

    def formula(person, period, parameters):
        schwere_zuwiderhandlung = person('schwere_zuwiderhandlung_konzession', period)
        wiederholte_zuwiderhandlung = person('wiederholte_zuwiderhandlung_konzession', period)
        gegenstandslos = person('konzession_gegenstandslos', period)

        # Art. 17 Abs. 2: bei schwerer ODER wiederholter Zuwiderhandlung,
        # oder wenn die Konzession gegenstandslos geworden ist
        voraussetzung_erfuellt = schwere_zuwiderhandlung + wiederholte_zuwiderhandlung + gegenstandslos

        return voraussetzung_erfuellt


class konzession_aufhebung_kantonsanhoerung_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anhörung der Kantonsregierung vor Konzessionsaufhebung erforderlich (SR 744.21 Art. 17 Abs. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1926/493_515_514/de#art_17"

    def formula(person, period, parameters):
        # Die Kantonsregierung ist vorher anzuhören, wenn eine Aufhebung in Frage kommt
        aufhebung_zulaessig = person('konzession_aufhebung_ohne_entschaedigung_zulaessig', period)
        return aufhebung_zulaessig


# Input variables (fact placeholders to be set externally)

class schwere_zuwiderhandlung_konzession_sachverhalt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sachverhalt: schwere Zuwiderhandlung liegt vor"
    reference = "https://www.fedlex.admin.ch/eli/cc/1926/493_515_514/de#art_17"


class wiederholte_zuwiderhandlung_konzession_sachverhalt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sachverhalt: wiederholte Zuwiderhandlung liegt vor"
    reference = "https://www.fedlex.admin.ch/eli/cc/1926/493_515_514/de#art_17"


class konzession_gegenstandslos_sachverhalt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sachverhalt: Konzession ist gegenstandslos geworden"
    reference = "https://www.fedlex.admin.ch/eli/cc/1926/493_515_514/de#art_17"
