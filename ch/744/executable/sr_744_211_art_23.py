"""SR 744.211 Art. 23

Generated from: ch/744/de/744.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class trolleybus_haftpflichtversicherung_abgeschlossen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Haftpflichtversicherung gemäss Art. 16 BG Trolleybusunternehmungen abgeschlossen"
    reference = "SR 744.211 Art. 23 Abs. 1"

    def formula(person, period, parameters):
        return person('trolleybus_haftpflichtversicherung_vorhanden', period)


class trolleybus_haftpflichtversicherung_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Liegt die nach Art. 16 BG Trolleybusunternehmungen (29. März 1950) vorgeschriebene Haftpflichtversicherung vor"
    reference = "SR 744.211 Art. 23 Abs. 1; SR 744.21 Art. 16"


class trolleybus_anlagen_geprueft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anlagen, Einrichtungen und Fahrzeuge durch das Bundesamt untersucht und erprobt"
    reference = "SR 744.211 Art. 23 Abs. 2"


class trolleybus_behoerden_eingeladen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Beteiligte eidgenössische und kantonale Behörden zur Prüfung eingeladen"
    reference = "SR 744.211 Art. 23 Abs. 2"


class trolleybus_betriebseroffnung_bewilligung_erteilt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bewilligung des Bundesamtes zur Betriebseröffnung erteilt"
    reference = "SR 744.211 Art. 23"

    def formula(person, period, parameters):
        versicherung = person('trolleybus_haftpflichtversicherung_abgeschlossen', period)
        geprueft = person('trolleybus_anlagen_geprueft', period)
        behoerden_eingeladen = person('trolleybus_behoerden_eingeladen', period)
        return versicherung * geprueft * behoerden_eingeladen
