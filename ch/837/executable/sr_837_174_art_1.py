"""SR 837.174 Art. 1 – Versicherte Personen

Generated from: ch/837/de/837.174.md

Obligatorische berufliche Vorsorge für arbeitslose Personen:
Für die Risiken Tod und Invalidität sind arbeitslose Personen obligatorisch
versichert, die Anspruchsvoraussetzungen nach Art. 8 AVIG erfüllen und einen
koordinierten Tageslohn erzielen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class erfuellt_anspruch_avig_art8(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Erfüllt Anspruchsvoraussetzungen nach Art. 8 AVIG für Taggelder"
    reference = "SR 837.174 Art. 1 Abs. 1 lit. a"


class bezieht_entschaedigung_avig_art29(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Bezieht Entschädigungen nach Art. 29 AVIG"
    reference = "SR 837.174 Art. 1 Abs. 1 lit. a"


class koordinierter_tageslohn(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Koordinierter Tageslohn (CHF)"
    reference = "SR 837.174 Art. 4"


class bereits_bvg_versichert_art47(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Bereits nach Art. 47 Abs. 1 oder 47a BVG versichert in gleichem Umfang"
    reference = "SR 837.174 Art. 1 Abs. 2"


class obligatorisch_versichert_arbeitslos_tod_invaliditaet(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Obligatorisch versichert für Risiken Tod und Invalidität als arbeitslose Person"
    reference = "SR 837.174 Art. 1"

    def formula(person, period, parameters):
        anspruch_avig = person('erfuellt_anspruch_avig_art8', period)
        entschaedigung_art29 = person('bezieht_entschaedigung_avig_art29', period)
        koord_lohn = person('koordinierter_tageslohn', period)
        bereits_versichert = person('bereits_bvg_versichert_art47', period)

        # Abs. 1: Versichert wenn (a) Anspruch nach AVIG oder Entschädigung nach Art. 29
        # und (b) koordinierter Tageslohn > 0
        grundvoraussetzung = (anspruch_avig + entschaedigung_art29) * (koord_lohn > 0)

        # Abs. 2: Nicht versichert wenn bereits nach BVG Art. 47/47a versichert
        return grundvoraussetzung * not_(bereits_versichert)
