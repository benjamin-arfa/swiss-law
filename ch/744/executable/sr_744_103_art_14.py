"""SR 744.103 Art. 14

Generated from: ch/744/de/744.103.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bav_auskunftsrecht_gesuch_eingereicht(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person hat Auskunftsgesuch beim BAV gemäss Art. 16 DSV eingereicht"
    reference = "SR 744.103 Art. 14 Abs. 1"

    def formula(person, period, parameters):
        return person('bav_auskunftsrecht_gesuch_form_korrekt', period)


class bav_auskunftsrecht_gesuch_form_korrekt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Auskunftsgesuch wurde in der Form nach Art. 16 DSV (SR 235.11) eingereicht"
    reference = "SR 744.103 Art. 14 Abs. 1; SR 235.11 Art. 16"


class bav_auskunftsrecht_anspruch(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person hat Anspruch auf Auskunft über ihre Daten beim BAV"
    reference = "SR 744.103 Art. 14 Abs. 1"

    def formula(person, period, parameters):
        gesuch_korrekt = person('bav_auskunftsrecht_gesuch_form_korrekt', period)
        return gesuch_korrekt


class bav_berichtigungsrecht_anspruch(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person kann Berichtigungsrecht gegenüber dem BAV geltend machen (gemäss Art. 41 DSG SR 235.1)"
    reference = "SR 744.103 Art. 14 Abs. 2; SR 235.1 Art. 41"

    def formula(person, period, parameters):
        return person('dsg_berichtigungsrecht_voraussetzungen_erfuellt', period)


class dsg_berichtigungsrecht_voraussetzungen_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Voraussetzungen für Berichtigungsrecht nach Art. 41 DSG (SR 235.1) sind erfüllt"
    reference = "SR 235.1 Art. 41"
