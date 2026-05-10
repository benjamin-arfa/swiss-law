"""SR 432.21 Art. 8a

Generated from: ch/432/de/432.21.md

Gewerbliche Leistungen der Nationalbibliothek - Voraussetzungen und Kostendeckung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class leistung_steht_in_engem_zusammenhang_mit_hauptaufgaben(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gewerbliche Leistung steht in engem Zusammenhang mit Hauptaufgaben"
    reference = "SR 432.21 Art. 8a Abs. 1 Bst. a"


class leistung_beeintraechtigt_hauptaufgaben_nicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gewerbliche Leistung beeintraechtigt die Erfuellung der Hauptaufgaben nicht"
    reference = "SR 432.21 Art. 8a Abs. 1 Bst. b"


class leistung_erfordert_keine_bedeutenden_zusatzmittel(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gewerbliche Leistung erfordert keine bedeutenden zusaetzlichen sachlichen und personellen Mittel"
    reference = "SR 432.21 Art. 8a Abs. 1 Bst. c"


class gewerbliche_leistung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gewerbliche Leistung ist zulaessig"
    reference = "SR 432.21 Art. 8a Abs. 1"

    def formula(person, period, parameters):
        return (
            person('leistung_steht_in_engem_zusammenhang_mit_hauptaufgaben', period) *
            person('leistung_beeintraechtigt_hauptaufgaben_nicht', period) *
            person('leistung_erfordert_keine_bedeutenden_zusatzmittel', period)
        )


class gewerbliche_leistung_kosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kosten der gewerblichen Leistung"
    reference = "SR 432.21 Art. 8a Abs. 2"


class gewerbliche_leistung_preis(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Preis der gewerblichen Leistung"
    reference = "SR 432.21 Art. 8a Abs. 2"


class ausnahme_kostendeckung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Departement hat Ausnahme von Kostendeckungspflicht zugelassen"
    reference = "SR 432.21 Art. 8a Abs. 2"


class gewerbliche_leistung_preiskonform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Preis der gewerblichen Leistung ist mindestens kostendeckend oder Ausnahme liegt vor"
    reference = "SR 432.21 Art. 8a Abs. 2"

    def formula(person, period, parameters):
        kostendeckend = person('gewerbliche_leistung_preis', period) >= person('gewerbliche_leistung_kosten', period)
        ausnahme = person('ausnahme_kostendeckung', period)
        return kostendeckend + ausnahme * not_(kostendeckend)
