"""SR 314.11 Art. 2

Generated from: ch/314/de/314.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class parkieren_im_halteverbot_und_ruhender_verkehr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Parkieren/Halten im Halteverbot mit zusaetzlichem Tatbestand des ruhenden Verkehrs (Anhang 1 Ziff. 2)"
    reference = "SR 314.11 Art. 2 Abs. 1 Bst. a"


class halter_und_fuehrer_gleiche_person(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person ist zugleich Fahrzeughalterin und Fahrzeugfuehrerin (Anhang 1 Ziff. 4 und 5)"
    reference = "SR 314.11 Art. 2 Abs. 1 Bst. b"


class gleicher_schutzzweck_verkehr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zwei oder mehr missachtete Verkehrsregeln/Signale/Markierungen haben denselben Schutzzweck"
    reference = "SR 314.11 Art. 2 Abs. 1 Bst. c"


class bussen_nicht_zusammengezaehlt_strassenverkehr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Bussen werden bei Strassenverkehr nicht zusammengezaehlt (Ausnahme nach Art. 2 Abs. 1)"
    reference = "SR 314.11 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        parkieren = person('parkieren_im_halteverbot_und_ruhender_verkehr', period)
        halter_fuehrer = person('halter_und_fuehrer_gleiche_person', period)
        schutzzweck = person('gleicher_schutzzweck_verkehr', period)
        return parkieren + halter_fuehrer + schutzzweck > 0


class gleicher_schutzzweck_binnenschifffahrt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zwei oder mehr Binnenschifffahrtsregeln/Signale/Zeichen mit gleichem Schutzzweck missachtet"
    reference = "SR 314.11 Art. 2 Abs. 2"
