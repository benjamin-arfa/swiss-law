"""SR 817.0 Art. 14

Generated from: ch/817/de/817.0.md

Abgabe- und Werbebeschraenkungen fuer alkoholische Getraenke:
- Abs. 1: Abgabe alkoholischer Getraenke an Jugendliche unter 16 Jahren ist verboten.
- Abs. 2: Bundesrat kann Werbung fuer alkoholische Getraenke, die sich speziell an
  Jugendliche unter 18 Jahren richtet, einschraenken.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class alter_person(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Alter der Person in Jahren"


class ist_alkoholisches_getraenk(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob es sich um ein alkoholisches Getraenk handelt"
    reference = "SR 817.0 Art. 14"


class abgabe_alkohol_verboten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Abgabe alkoholischer Getraenke an diese Person verboten ist"
    reference = "SR 817.0 Art. 14 Abs. 1"

    def formula(person, period, parameters):
        alter = person('alter_person', period)
        ist_alkoholisch = person('ist_alkoholisches_getraenk', period)
        mindestalter = parameters(period).sr_817_0.mindestalter_abgabe_alkohol
        return ist_alkoholisch * (alter < mindestalter)


class werbung_richtet_sich_an_jugendliche(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob sich die Werbung speziell an Jugendliche richtet"
    reference = "SR 817.0 Art. 14 Abs. 2"


class werbung_alkohol_einschraenkbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Werbung fuer alkoholische Getraenke eingeschraenkt werden kann"
    reference = "SR 817.0 Art. 14 Abs. 2"

    def formula(person, period, parameters):
        ist_alkoholisch = person('ist_alkoholisches_getraenk', period)
        an_jugendliche = person('werbung_richtet_sich_an_jugendliche', period)
        alter = person('alter_person', period)
        altersgrenze = parameters(period).sr_817_0.altersgrenze_werbung_alkohol
        return ist_alkoholisch * an_jugendliche * (alter < altersgrenze)
