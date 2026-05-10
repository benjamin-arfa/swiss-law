"""SR 744.211 Art. 17

Generated from: ch/744/de/744.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class trolleybus_mindestalter_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person hat das 21. Lebensjahr vollendet (Voraussetzung Trolleybus-Führerausweis)"
    reference = "SR 744.211 Art. 17 Abs. 3"

    def formula(person, period, parameters):
        alter = person('alter', period)
        return alter >= 21


class trolleybus_aerztliche_anforderungen_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person erfüllt ärztliche Minimalanforderungen zur Führung eines schweren Motorwagens zum Personentransport"
    reference = "SR 744.211 Art. 17 Abs. 3"

    def formula(person, period, parameters):
        return person('aerztliche_minimalanforderungen_schwerer_motorwagen_personentransport', period)


class trolleybus_arztzeugnis_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zeugnis eines durch die kantonale Behörde anerkannten Arztes liegt vor"
    reference = "SR 744.211 Art. 17 Abs. 3"


class trolleybus_leumundszeugnis_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Leumundszeugnis liegt vor"
    reference = "SR 744.211 Art. 17 Abs. 3"


class trolleybus_vostra_auszug_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Privatauszug aus dem Strafregister-Informationssystem VOSTRA liegt vor"
    reference = "SR 744.211 Art. 17 Abs. 3"


class trolleybus_fuehrerausweis_dokumente_vollstaendig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Alle erforderlichen Dokumente für den Trolleybus-Führerausweis sind beigebracht"
    reference = "SR 744.211 Art. 17 Abs. 3"

    def formula(person, period, parameters):
        arztzeugnis = person('trolleybus_arztzeugnis_vorhanden', period)
        leumundszeugnis = person('trolleybus_leumundszeugnis_vorhanden', period)
        vostra = person('trolleybus_vostra_auszug_vorhanden', period)
        return arztzeugnis * leumundszeugnis * vostra


class trolleybus_fuehrerausweis_anspruch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person erfüllt alle Voraussetzungen für den Führerausweis der Kategorie Trolleybus"
    reference = "SR 744.211 Art. 17 Abs. 3"

    def formula(person, period, parameters):
        mindestalter = person('trolleybus_mindestalter_erfuellt', period)
        aerztlich = person('trolleybus_aerztliche_anforderungen_erfuellt', period)
        dokumente = person('trolleybus_fuehrerausweis_dokumente_vollstaendig', period)
        return mindestalter * aerztlich * dokumente


class trolleybus_lernfahrausweis_anspruch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person kann Lernfahrausweis für Trolleybusse für Lernfahrten gemäss Art. 18 erhalten"
    reference = "SR 744.211 Art. 17 Abs. 2"
