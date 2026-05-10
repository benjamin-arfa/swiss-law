"""SR 142.318 Art. 5

Generated from: ch/142/de/142.318.md

Teilnahme von weiteren Personen: Weitere Personen nach Art. 29 Abs. 2
AsylG koennen im gleichen Raum teilnehmen, sofern BAG-Vorgaben
eingehalten werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class weitere_personen_gleicher_raum_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob weitere Personen nach Art. 29 Abs. 2 AsylG im gleichen Raum teilnehmen koennen"
    reference = "SR 142.318 Art. 5"

    def formula_2020_04(person, period, parameters):
        return person('befragung_bag_vorgaben_eingehalten', period)
