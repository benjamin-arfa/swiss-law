"""SR 744.10 Art. 7

Generated from: ch/744/de/744.10.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class verkehrsleiter_pruefung_bestanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verkehrsleiter hat die Eignungsprüfung bestanden"
    reference = "SR 744.10 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        return person('verkehrsleiter_pruefung_abgelegt', period) * person('verkehrsleiter_pruefung_note_bestanden', period)


class verkehrsleiter_pruefung_abgelegt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verkehrsleiter hat die Eignungsprüfung abgelegt"
    reference = "SR 744.10 Art. 7 Abs. 1"


class verkehrsleiter_pruefung_note_bestanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verkehrsleiter hat die Prüfung mit genügender Note bestanden"
    reference = "SR 744.10 Art. 7 Abs. 1, 3"


class verkehrsleiter_fachausweis(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verkehrsleiter besitzt einen Fachausweis"
    reference = "SR 744.10 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        return person('verkehrsleiter_pruefung_bestanden', period) + person('verkehrsleiter_pruefungsbefreiung', period)


class verkehrsleiter_befreiung_durch_diplom(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Befreiung von bestimmten Prüfungsfächern durch anerkannten Fachausweis oder Diplom"
    reference = "SR 744.10 Art. 7 Abs. 4"


class verkehrsleiter_befreiung_berufspruefung_strassenverkehr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Befreiung von der Prüfung durch bestandene Berufsprüfung oder höhere Fachprüfung im Sachgebiet Strassenverkehr"
    reference = "SR 744.10 Art. 7 Abs. 6"

    def formula(person, period, parameters):
        berufspruefung_bestanden = person('berufspruefung_strassenverkehr_bestanden', period)
        hoehere_fachpruefung_bestanden = person('hoehere_fachpruefung_strassenverkehr_bestanden', period)
        return berufspruefung_bestanden + hoehere_fachpruefung_bestanden


class berufspruefung_strassenverkehr_bestanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person hat eine Berufsprüfung im Sachgebiet Strassenverkehr erfolgreich abgelegt"
    reference = "SR 744.10 Art. 7 Abs. 6"


class hoehere_fachpruefung_strassenverkehr_bestanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person hat eine höhere Fachprüfung im Sachgebiet Strassenverkehr erfolgreich abgelegt"
    reference = "SR 744.10 Art. 7 Abs. 6"


class verkehrsleiter_pruefungsbefreiung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist von der Eignungsprüfung für Verkehrsleiter befreit"
    reference = "SR 744.10 Art. 7 Abs. 4, 6"

    def formula(person, period, parameters):
        befreiung_berufspruefung = person('verkehrsleiter_befreiung_berufspruefung_strassenverkehr', period)
        befreiung_diplom = person('verkehrsleiter_befreiung_durch_diplom', period)
        return befreiung_berufspruefung + befreiung_diplom


class verkehrsleiter_fachliche_eignung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verkehrsleiter erfüllt die Anforderungen der fachlichen Eignung gemäss SR 744.10 Art. 7"
    reference = "SR 744.10 Art. 7"

    def formula(person, period, parameters):
        fachausweis = person('verkehrsleiter_fachausweis', period)
        pruefungsbefreiung = person('verkehrsleiter_pruefungsbefreiung', period)
        return fachausweis + pruefungsbefreiung
