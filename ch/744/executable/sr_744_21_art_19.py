"""SR 744.21 Art. 19

Generated from: ch/744/de/744.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class trolleybus_unternehmen_konzessioniert_vor_inkrafttreten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Trolleybusunternehmen war vor Inkrafttreten des Gesetzes konzessioniert"
    reference = "SR 744.21 Art. 19 Abs. 1"

    def formula(person, period, parameters):
        return person('konzessioniert_vor_inkrafttreten', period)


class trolleybus_gesetz_anwendbar_auf_altkonzessionen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gesetz findet Anwendung auf vor Inkrafttreten konzessionierte Trolleybusunternehmen"
    reference = "SR 744.21 Art. 19 Abs. 1"

    def formula(person, period, parameters):
        konzessioniert_vorher = person('trolleybus_unternehmen_konzessioniert_vor_inkrafttreten', period)
        return konzessioniert_vorher


class trolleybus_konzession_anpassungspflichtig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Konzession muss innert drei Jahren den gesetzlichen Bestimmungen angepasst werden"
    reference = "SR 744.21 Art. 19 Abs. 1"

    def formula(person, period, parameters):
        anwendbar = person('trolleybus_gesetz_anwendbar_auf_altkonzessionen', period)
        konzession_bereits_angepasst = person('trolleybus_konzession_bereits_angepasst', period)
        return anwendbar * not_(konzession_bereits_angepasst)


class trolleybus_konzession_bereits_angepasst(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Konzession wurde bereits den gesetzlichen Bestimmungen angepasst"
    reference = "SR 744.21 Art. 19 Abs. 1"


class trolleybus_neue_technische_erscheinung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Neue technische Erscheinung bei Trolleybusfahrzeugen liegt vor"
    reference = "SR 744.21 Art. 19 Abs. 2"


class trolleybus_bundesrat_massnahme_ermaechtigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bundesrat ist ermächtigt, Massnahmen bei neuen technischen Erscheinungen zu treffen (vor gesetzlicher Regelung)"
    reference = "SR 744.21 Art. 19 Abs. 2"

    def formula(person, period, parameters):
        neue_technik = person('trolleybus_neue_technische_erscheinung', period)
        gesetzliche_regelung_vorhanden = person('trolleybus_gesetzliche_regelung_neue_technik_vorhanden', period)
        return neue_technik * not_(gesetzliche_regelung_vorhanden)


class trolleybus_gesetzliche_regelung_neue_technik_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gesetzliche Regelung für neue technische Erscheinungen bei Trolleybusfahrzeugen besteht bereits"
    reference = "SR 744.21 Art. 19 Abs. 2"
