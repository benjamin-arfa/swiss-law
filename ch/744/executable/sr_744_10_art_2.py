"""SR 744.10 Art. 2

Generated from: ch/744/de/744.10.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_motorfahrzeug(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Motorfahrzeug im Sinne von SR 744.10 Art. 2 Bst. a"
    reference = "SR 744.10 Art. 2 Bst. a"

    def formula(person, period, parameters):
        # Ein Motorfahrzeug ist jedes Fahrzeug im Sinne von Art. 7 Abs. 1 SVG (SR 741.01).
        # Die Qualifikation erfolgt durch das Strassenverkehrsgesetz; hier als externe Bedingung abgebildet.
        return person('fahrzeug_nach_svg_art7_abs1', period)


class fahrzeug_nach_svg_art7_abs1(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeug im Sinne von Art. 7 Abs. 1 SVG (SR 741.01)"
    reference = "SR 741.01 Art. 7 Abs. 1"


class ist_gewerbsmaessige_befoerderung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gewerbsmässige Beförderung im Sinne von SR 744.10 Art. 2 Bst. b"
    reference = "SR 744.10 Art. 2 Bst. b"

    def formula(person, period, parameters):
        # Gewerbsmässige Beförderung: Beförderung von Personen oder Gütern gegen wirtschaftliche Gegenleistung.
        befoerdert_personen_oder_gueter = person('befoerdert_personen_oder_gueter', period)
        erhaelt_wirtschaftliche_gegenleistung = person('erhaelt_wirtschaftliche_gegenleistung', period)
        return befoerdert_personen_oder_gueter * erhaelt_wirtschaftliche_gegenleistung


class befoerdert_personen_oder_gueter(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Strassentransportunternehmen befördert Personen oder Güter"
    reference = "SR 744.10 Art. 2 Bst. b"


class erhaelt_wirtschaftliche_gegenleistung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Strassentransportunternehmen erhält eine wirtschaftliche Gegenleistung für die Beförderung"
    reference = "SR 744.10 Art. 2 Bst. b"


class ist_verkehrsleiter(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verkehrsleiter oder Verkehrsleiterin im Sinne von SR 744.10 Art. 2 Bst. c"
    reference = "SR 744.10 Art. 2 Bst. c"

    def formula(person, period, parameters):
        # Verkehrsleiter: natürliche Person, die Verkehrstätigkeiten eines Strassentransportunternehmens
        # tatsächlich und dauerhaft leitet.
        ist_natuerliche_person = person('ist_natuerliche_person', period)
        leitet_tatsaechlich = person('leitet_verkehrstaetigkeiten_tatsaechlich', period)
        leitet_dauerhaft = person('leitet_verkehrstaetigkeiten_dauerhaft', period)
        return ist_natuerliche_person * leitet_tatsaechlich * leitet_dauerhaft


class ist_natuerliche_person(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Natürliche Person (im Gegensatz zu juristischer Person)"
    reference = "SR 744.10 Art. 2 Bst. c"

    def formula(person, period, parameters):
        return True


class leitet_verkehrstaetigkeiten_tatsaechlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person leitet Verkehrstätigkeiten eines Strassentransportunternehmens tatsächlich"
    reference = "SR 744.10 Art. 2 Bst. c"


class leitet_verkehrstaetigkeiten_dauerhaft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person leitet Verkehrstätigkeiten eines Strassentransportunternehmens dauerhaft"
    reference = "SR 744.10 Art. 2 Bst. c"
