"""SR 744.211 Art. 8

Generated from: ch/744/de/744.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class fahrzeug_bau_verkehrsanforderungen_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeugbau entspricht Anforderungen des Strassenverkehrs und des Linienbetriebs (Art. 8 Abs. 1)"
    reference = "SR 744.211 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        strassenverkehr_anforderungen = person('fahrzeug_strassenverkehr_konform', period)
        linienbetrieb_anforderungen = person('fahrzeug_linienbetrieb_konform', period)
        return strassenverkehr_anforderungen * linienbetrieb_anforderungen


class fahrzeug_strassenverkehr_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeug entspricht den Anforderungen des Strassenverkehrs"
    reference = "SR 744.211 Art. 8 Abs. 1"


class fahrzeug_linienbetrieb_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeug entspricht den Anforderungen des Linienbetriebs"
    reference = "SR 744.211 Art. 8 Abs. 1"


class fahrzeug_technische_ausruestung_bundesrecht_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Technische Ausrüstung des Fahrzeugs entspricht der Bundesgesetzgebung über den Motorfahrzeugverkehr (Art. 8 Abs. 2)"
    reference = "SR 744.211 Art. 8 Abs. 2"


class fahrzeug_grundausstattung_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeug verfügt mindestens über Heizung, elektrische Beleuchtung und Lüftungseinrichtung (Art. 8 Abs. 3)"
    reference = "SR 744.211 Art. 8 Abs. 3"

    def formula(person, period, parameters):
        heizung = person('fahrzeug_hat_heizung', period)
        beleuchtung = person('fahrzeug_hat_elektrische_beleuchtung', period)
        lueftung = person('fahrzeug_hat_lueftungseinrichtung', period)
        return heizung * beleuchtung * lueftung


class fahrzeug_hat_heizung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeug ist mit Heizung ausgestattet"
    reference = "SR 744.211 Art. 8 Abs. 3"


class fahrzeug_hat_elektrische_beleuchtung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeug ist mit elektrischer Beleuchtung ausgestattet"
    reference = "SR 744.211 Art. 8 Abs. 3"


class fahrzeug_hat_lueftungseinrichtung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeug ist mit Lüftungseinrichtung ausgestattet"
    reference = "SR 744.211 Art. 8 Abs. 3"


class fahrzeug_anforderungen_art8_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeug erfüllt alle Anforderungen gemäss Art. 8 SR 744.211"
    reference = "SR 744.211 Art. 8"

    def formula(person, period, parameters):
        bau = person('fahrzeug_bau_verkehrsanforderungen_erfuellt', period)
        technik = person('fahrzeug_technische_ausruestung_bundesrecht_konform', period)
        ausstattung = person('fahrzeug_grundausstattung_erfuellt', period)
        return bau * technik * ausstattung
