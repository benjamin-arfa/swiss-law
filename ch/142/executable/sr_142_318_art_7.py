"""SR 142.318 Art. 7

Generated from: ch/142/de/142.318.md

Eroeffnung und Zustellung in den Zentren des Bundes: Wenn Zustellung
an den Leistungserbringer nicht moeglich, erfolgt sie an die
asylsuchende Person. Das SEM informiert die Rechtsvertretung am
gleichen Tag.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class zustellung_leistungserbringer_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Zustellung an den Leistungserbringer der Rechtsvertretung moeglich ist"
    reference = "SR 142.318 Art. 7"


class zustellung_an_asylsuchende_person(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Eroeffnung und Zustellung direkt an die asylsuchende Person erfolgt"
    reference = "SR 142.318 Art. 7"

    def formula_2020_04(person, period, parameters):
        return not_(person('zustellung_leistungserbringer_moeglich', period))
