"""SR 614.0 Art. 10a

Generated from: ch/614/de/614.0.md

Art. 10a: Meldungen und Datenbearbeitung - Die EFK nimmt Meldungen zu
Missständen entgegen, betreibt eine Meldestelle, klärt Sachverhalte ab.
Aufbewahrung: bis 5 Jahre nach Abklärung.
In Kraft seit 1. Jan. 2027.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class efk_nimmt_meldungen_entgegen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK nimmt Meldungen zu Missständen in ihrem Aufgaben- und "
        "Aufsichtsbereich entgegen (Art. 10a Abs. 1)"
    )
    reference = "SR 614.0 Art. 10a Abs. 1"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_betreibt_meldestelle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "EFK betreibt eine Meldestelle (Art. 10a Abs. 2)"
    reference = "SR 614.0 Art. 10a Abs. 2"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_datenaufbewahrungsfrist_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = (
        "Maximale Aufbewahrungsfrist der Daten nach Abklärung des Sachverhalts "
        "in Jahren (Art. 10a Abs. 6)"
    )
    reference = "SR 614.0 Art. 10a Abs. 6"

    def formula(person, period, parameters):
        # Art. 10a Abs. 6: bis fünf Jahre nach Abklärung des Sachverhalts
        return 5


class efk_darf_besonders_schuetzenswerte_daten_bearbeiten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK darf besonders schützenswerte Personendaten zur Abklärung "
        "bearbeiten (Art. 10a Abs. 4)"
    )
    reference = "SR 614.0 Art. 10a Abs. 4"

    def formula(person, period, parameters):
        # Abs. 4: Daten aus öffentlich zugänglichen Quellen erheben und
        # besonders schützenswerte Daten nach DSG Art. 5 Bst. c Ziff. 1, 2, 5, 6
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_darf_daten_weitergeben_mit_zustimmung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK darf Daten der meldenden Person nur mit deren Zustimmung "
        "bekanntgeben (Art. 10a Abs. 5)"
    )
    reference = "SR 614.0 Art. 10a Abs. 5"

    def formula(person, period, parameters):
        ist_efk = person('ist_eidgenoessische_finanzkontrolle', period)
        zustimmung = person('meldende_person_stimmt_datenweitergabe_zu', period)
        return ist_efk * zustimmung


class meldende_person_stimmt_datenweitergabe_zu(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Meldende Person stimmt der Datenweitergabe zu"
    reference = "SR 614.0 Art. 10a Abs. 5"
