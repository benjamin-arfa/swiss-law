"""SR 425.1 Art. 22

Generated from: ch/425/de/425.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gewerbliche_leistung_enger_zusammenhang_hauptaufgaben(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die gewerbliche Leistung steht in engem Zusammenhang mit den Hauptaufgaben"
    reference = "SR 425.1 Art. 22 Abs. 1 lit. a"


class gewerbliche_leistung_beeintraechtigt_aufgaben_nicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die gewerbliche Leistung beeintraechtigt die Aufgabenerfuellung nicht"
    reference = "SR 425.1 Art. 22 Abs. 1 lit. b"


class gewerbliche_leistung_keine_bedeutenden_zusatzmittel(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die gewerbliche Leistung erfordert keine bedeutenden zusaetzlichen Mittel"
    reference = "SR 425.1 Art. 22 Abs. 1 lit. c"


class gewerbliche_leistung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gewerbliche Leistung des Instituts ist zulaessig"
    reference = "SR 425.1 Art. 22 Abs. 1"

    def formula(person, period, parameters):
        zusammenhang = person('gewerbliche_leistung_enger_zusammenhang_hauptaufgaben', period)
        nicht_beeintraechtigt = person('gewerbliche_leistung_beeintraechtigt_aufgaben_nicht', period)
        keine_zusatzmittel = person('gewerbliche_leistung_keine_bedeutenden_zusatzmittel', period)
        return zusammenhang * nicht_beeintraechtigt * keine_zusatzmittel


class gewerbliche_leistung_steuerpflichtig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Institut ist fuer Gewinne aus gewerblichen Leistungen steuerpflichtig"
    reference = "SR 425.1 Art. 22 Abs. 5"

    def formula(person, period, parameters):
        zulaessig = person('gewerbliche_leistung_zulaessig', period)
        return zulaessig
