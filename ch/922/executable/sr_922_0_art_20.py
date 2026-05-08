"""SR 922.0 Art. 20

Generated from: ch/922/de/922.0.md

Art. 20: Entzug und Verweigerung der Jagdberechtigung:
- Court may revoke hunting authorization for 1-10 years if:
  a. Person intentionally/negligently killed/injured someone while hunting or committed
     an offense under Art. 17; AND
  b. Risk of further such offenses exists
- Revocation applies to all of Switzerland
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
import numpy as np


class jsg_person_verletzt_getoetet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person hat bei der Jagd eine Person getötet oder erheblich verletzt"
    reference = "SR 922.0 Art. 20 Abs. 1 Bst. a"


class jsg_art17_vergehen_begangen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person hat ein Vergehen nach Art. 17 begangen"
    reference = "SR 922.0 Art. 20 Abs. 1 Bst. a"


class jsg_wiederholungsgefahr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gefahr weiterer solcher Taten besteht"
    reference = "SR 922.0 Art. 20 Abs. 1 Bst. b"


class jsg_entzug_jagdberechtigung_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Entzug der Jagdberechtigung durch Gericht ist möglich"
    reference = "SR 922.0 Art. 20 Abs. 1"

    def formula(person, period, parameters):
        verletzt = person('jsg_person_verletzt_getoetet', period)
        vergehen = person('jsg_art17_vergehen_begangen', period)
        wiederholung = person('jsg_wiederholungsgefahr', period)

        # Condition a: either killed/injured person OR committed Art. 17 offense
        bedingung_a = (verletzt + vergehen) > 0
        # Condition b: risk of repetition
        return bedingung_a * wiederholung


class jsg_entzug_min_dauer_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Minimale Entzugsdauer der Jagdberechtigung (Jahre)"
    reference = "SR 922.0 Art. 20 Abs. 1"

    def formula(person, period, parameters):
        entzug = person('jsg_entzug_jagdberechtigung_moeglich', period)
        return entzug * 1


class jsg_entzug_max_dauer_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Entzugsdauer der Jagdberechtigung (Jahre)"
    reference = "SR 922.0 Art. 20 Abs. 1"

    def formula(person, period, parameters):
        entzug = person('jsg_entzug_jagdberechtigung_moeglich', period)
        return entzug * 10
