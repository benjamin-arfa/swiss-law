"""SR 744.21 Art. 15

Generated from: ch/744/de/744.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class trolleybus_schaden_durch_betrieb(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schaden durch Betrieb eines Trolleybusfahrzeuges (Tötung, Verletzung oder Sachschaden)"
    reference = "SR 744.21 Art. 15 Abs. 1"

    def formula(person, period, parameters):
        getoetet = person('trolleybus_mensch_getoetet', period)
        verletzt = person('trolleybus_mensch_verletzt', period)
        sachschaden = person('trolleybus_sachschaden', period)
        durch_betrieb = person('schaden_durch_betrieb_trolleybusfahrzeug', period)
        return durch_betrieb * (getoetet + verletzt + sachschaden)


class trolleybus_haftung_nach_strassenverkehrsgesetz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Haftung des Trolleybusunternehmens nach Strassenverkehrsgesetz (SR 741.01) bei Tötung, Verletzung oder Sachschaden durch Fahrzeugbetrieb"
    reference = "SR 744.21 Art. 15 Abs. 1"

    def formula(person, period, parameters):
        schaden = person('trolleybus_schaden_durch_betrieb', period)
        # Haftung nach SVG (SR 741.01); Bestimmungen über Haftpflicht beim Wechsel des Halters sind nicht anwendbar
        return schaden


class trolleybus_haftpflicht_halter_wechsel_nicht_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bestimmungen des SVG über Haftpflicht beim Wechsel des Halters sind auf Trolleybusunternehmen nicht anwendbar"
    reference = "SR 744.21 Art. 15 Abs. 1"

    def formula(person, period, parameters):
        haftung_svg = person('trolleybus_haftung_nach_strassenverkehrsgesetz', period)
        # Ausnahme gilt immer, wenn die SVG-Haftung greift
        return haftung_svg


class trolleybus_schaden_durch_elektrische_anlage(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schaden durch Betrieb einer elektrischen Anlage oder Einwirkung elektrischen Stroms auf das Trolleybusfahrzeug"
    reference = "SR 744.21 Art. 15 Abs. 2"

    def formula(person, period, parameters):
        getoetet = person('trolleybus_mensch_getoetet', period)
        verletzt = person('trolleybus_mensch_verletzt', period)
        sachschaden = person('trolleybus_sachschaden', period)
        durch_elektrische_anlage = person('schaden_durch_elektrische_anlage_oder_strom', period)
        return durch_elektrische_anlage * (getoetet + verletzt + sachschaden)


class trolleybus_haftung_nach_starkstromgesetz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Haftung des Trolleybusunternehmens nach Bundesgesetz über Schwach- und Starkstromanlagen (SR 734.0) bei Schaden durch elektrische Anlage oder Strom"
    reference = "SR 744.21 Art. 15 Abs. 2"

    def formula(person, period, parameters):
        schaden_elektro = person('trolleybus_schaden_durch_elektrische_anlage', period)
        return schaden_elektro


class trolleybus_mensch_getoetet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Durch Trolleybusbetrieb wurde ein Mensch getötet"
    reference = "SR 744.21 Art. 15"


class trolleybus_mensch_verletzt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Durch Trolleybusbetrieb wurde ein Mensch verletzt"
    reference = "SR 744.21 Art. 15"


class trolleybus_sachschaden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Durch Trolleybusbetrieb wurde Sachschaden verursacht"
    reference = "SR 744.21 Art. 15"


class schaden_durch_betrieb_trolleybusfahrzeug(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schaden wurde durch den Betrieb des Trolleybusfahrzeuges verursacht (nicht durch elektrische Anlage)"
    reference = "SR 744.21 Art. 15 Abs. 1"


class schaden_durch_elektrische_anlage_oder_strom(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schaden wurde durch Betrieb einer elektrischen Anlage oder Einwirkung elektrischen Stroms auf das Fahrzeug verursacht"
    reference = "SR 744.21 Art. 15 Abs. 2"
