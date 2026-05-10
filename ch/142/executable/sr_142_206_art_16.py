"""SR 142.206 Art. 16

Generated from: ch/142/de/142.206.md

Loeschung von Daten von Drittstaatsangehoerigen, die nicht mehr dem
EES unterstehen: Loeschung durch SEM wenn Asylgesuch, laengerfristiges
Visum, Aufenthaltsbewilligung oder Schweizer Buergerrecht.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class hat_asylgesuch_eingereicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person ein Asylgesuch in der Schweiz eingereicht hat"
    reference = "SR 142.206 Art. 16 Bst. a"


class hat_visum_laengerfristiger_aufenthalt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person ein Visum fuer einen laengerfristigen Aufenthalt in der Schweiz erworben hat"
    reference = "SR 142.206 Art. 16 Bst. b"


class hat_aufenthaltsbewilligung_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person eine Aufenthaltsbewilligung in der Schweiz besitzt"
    reference = "SR 142.206 Art. 16 Bst. c"


class hat_schweizer_buergerrecht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person das Schweizer Buergerrecht erworben hat"
    reference = "SR 142.206 Art. 16 Bst. d"


class ees_daten_loeschung_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die EES-Daten der Kategorien I-VI geloescht werden muessen"
    reference = "SR 142.206 Art. 16"

    def formula_2022_05(person, period, parameters):
        return (
            person('hat_asylgesuch_eingereicht', period)
            + person('hat_visum_laengerfristiger_aufenthalt', period)
            + person('hat_aufenthaltsbewilligung_schweiz', period)
            + person('hat_schweizer_buergerrecht', period)
        ) > 0
