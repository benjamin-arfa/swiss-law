"""SR 170.32 Art. 3

Generated from: ch/170/de/170.32.md

Haftung des Bundes für Schaden, den ein Beamter Dritten widerrechtlich zufügt.
Kausalhaftung (ohne Rücksicht auf Verschulden).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class schaden_in_amtlicher_taetigkeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat in Ausübung amtlicher Tätigkeit Dritten widerrechtlich Schaden zugefügt (Art. 3 Abs. 1 VG)"
    reference = "SR 170.32, Art. 3 Abs. 1"


class schaden_unter_sonderhaftpflicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tatbestand fällt unter Haftpflichtbestimmungen anderer Erlasse (Art. 3 Abs. 2 VG)"
    reference = "SR 170.32, Art. 3 Abs. 2"


class schadenshoehe_dritte(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Höhe des dem Dritten zugefügten Schadens in CHF"
    reference = "SR 170.32, Art. 3"


class bund_haftet_fuer_schaden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bund haftet für den Schaden (Art. 3 Abs. 1 VG)"
    reference = "SR 170.32, Art. 3 Abs. 1"

    def formula(person, period, parameters):
        ist_beamter = person('untersteht_verantwortlichkeitsgesetz', period)
        schaden = person('schaden_in_amtlicher_taetigkeit', period)
        sonderhaftpflicht = person('schaden_unter_sonderhaftpflicht', period)
        return ist_beamter * schaden * (1 - sonderhaftpflicht)


class geschaedigter_hat_anspruch_gegen_beamten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Geschädigter hat Anspruch gegen den fehlbaren Beamten (Art. 3 Abs. 3 VG)"
    reference = "SR 170.32, Art. 3 Abs. 3"

    def formula(person, period, parameters):
        # Gegenüber dem Fehlbaren steht dem Geschädigten kein Anspruch zu
        return person('untersteht_verantwortlichkeitsgesetz', period) * 0
