"""SR 672.916.31 Art. 2 — Anrechnung österreichischer Quellensteuer auf Grenzgänger

Art. 2: Soweit Österreich Einkünfte aus in seinem Gebiet ausgeübter
unselbständiger Erwerbstätigkeit von in der Schweiz ansässigen Grenzgängern
im Abzugswege an der Quelle besteuert, hat der Wohnsitzkanton die
österreichische Steuer auf seine Einkommenssteuer anzurechnen.

Generated from: ch/672/de/672.916.31.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_switzerland.entities import Person


class ist_grenzgaenger_ch_at(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist in der Schweiz ansässiger Grenzgänger mit Erwerbstätigkeit in Österreich (SR 672.916.31 Art. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1975/116_116_116/de#art_2"


class einkommen_unselbstaendig_grenzgaenger_ch_in_at(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Einkünfte aus unselbständiger Erwerbstätigkeit eines CH-Grenzgängers in Österreich"
    reference = "https://www.fedlex.admin.ch/eli/cc/1975/116_116_116/de#art_2"
    default_value = 0


class at_quellensteuer_auf_ch_grenzgaenger(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Von Österreich im Abzugswege erhobene Quellensteuer auf CH-Grenzgänger"
    reference = "https://www.fedlex.admin.ch/eli/cc/1975/116_116_116/de#art_2"
    default_value = 0


class anrechnung_at_quellensteuer_grenzgaenger(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anrechnung der österreichischen Quellensteuer auf kantonale Einkommenssteuer (SR 672.916.31 Art. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1975/116_116_116/de#art_2"

    def formula(person, period, parameters):
        # Art. 2: Der Wohnsitzkanton muss die österreichische Quellensteuer
        # auf die von ihm erhobene Einkommenssteuer anrechnen.
        ist_grenzgaenger = person('ist_grenzgaenger_ch_at', period)
        at_steuer = person('at_quellensteuer_auf_ch_grenzgaenger', period)
        return ist_grenzgaenger * at_steuer
