"""SR 744.211 Art. 21

Generated from: ch/744/de/744.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class trolleybus_konzession_vorschriften_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Trolleybusunternehmen unterliegt den Bestimmungen der Konzession und den Vorschriften der Eisenbahn- und Elektrizitätsgesetzgebung"
    reference = "SR 744.211 Art. 21"

    def formula(person, period, parameters):
        ist_trolleybus_unternehmen = person("ist_trolleybus_unternehmen", period)
        hat_konzession = person("hat_trolleybus_konzession", period)
        return ist_trolleybus_unternehmen * hat_konzession


class ist_trolleybus_unternehmen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person oder Unternehmen betreibt ein Trolleybusunternehmen"
    reference = "SR 744.211 Art. 21"


class hat_trolleybus_konzession(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Trolleybusunternehmen verfügt über eine gültige Konzession"
    reference = "SR 744.211 Art. 21"


class eisenbahn_vorschriften_eingehalten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Trolleybusunternehmen hält die Vorschriften der Eisenbahngesetzgebung ein"
    reference = "SR 744.211 Art. 21"


class elektrizitaet_vorschriften_eingehalten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Trolleybusunternehmen hält die Vorschriften der Elektrizitätsgesetzgebung ein"
    reference = "SR 744.211 Art. 21"


class trolleybus_betrieb_rechtskonform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Trolleybusbetrieb wird rechtskonform gemäss Art. 21 SR 744.211 geführt"
    reference = "SR 744.211 Art. 21"

    def formula(person, period, parameters):
        konzession_anwendbar = person("trolleybus_konzession_vorschriften_anwendbar", period)
        eisenbahn = person("eisenbahn_vorschriften_eingehalten", period)
        elektrizitaet = person("elektrizitaet_vorschriften_eingehalten", period)
        return konzession_anwendbar * eisenbahn * elektrizitaet
