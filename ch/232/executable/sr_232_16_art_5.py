"""SR 232.16 Art. 5

Generated from: ch/232/de/232.16.md

Art. 5 defines the scope of plant variety protection: what actions
require consent of the variety protection holder.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_sortenschutzinhaber(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist Inhaber des Sortenschutzes"
    reference = "SR 232.16 Art. 5"


class hat_zustimmung_sortenschutzinhaber(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person hat die Zustimmung des Sortenschutzinhabers"
    reference = "SR 232.16 Art. 5 Abs. 1"


class handlung_mit_vermehrungsmaterial(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person erzeugt, vermehrt, bietet an, verkauft, ein-/ausfuehrt oder bewahrt Vermehrungsmaterial"
    reference = "SR 232.16 Art. 5 Abs. 1 lit. a-e"


class sorte_ist_geschuetzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Die betroffene Pflanzensorte ist durch Sortenschutz geschuetzt"
    reference = "SR 232.16 Art. 5"


class sortenschutz_verletzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Sortenschutz wird verletzt (Handlung ohne Zustimmung des Inhabers)"
    reference = "SR 232.16 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        geschuetzt = person('sorte_ist_geschuetzt', period)
        handlung = person('handlung_mit_vermehrungsmaterial', period)
        zustimmung = person('hat_zustimmung_sortenschutzinhaber', period)
        ist_inhaber = person('ist_sortenschutzinhaber', period)

        return geschuetzt * handlung * (1 - zustimmung) * (1 - ist_inhaber)
