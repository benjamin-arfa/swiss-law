"""SR 431.031 Art. 5

Generated from: ch/431/de/431.031.md

Aufbau der UID - Praefix CHE, 8-stellige Zufallszahl, Pruefziffer.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class uid_praefix(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Praefix der Unternehmens-Identifikationsnummer"
    reference = "SR 431.031 Art. 5 Bst. a"
    default_value = "CHE"


class uid_zufallszahl_stellen(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Stellen der Zufallszahl in der UID"
    reference = "SR 431.031 Art. 5 Bst. b"
    default_value = 8


class uid_hat_pruefziffer(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "UID enthaelt eine Pruefziffer"
    reference = "SR 431.031 Art. 5 Bst. c"
    default_value = True


class uid_aufbau_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "UID entspricht dem vorgeschriebenen Aufbau (CHE + 8 Ziffern + Pruefziffer)"
    reference = "SR 431.031 Art. 5"

    def formula(person, period, parameters):
        return person('uid_hat_pruefziffer', period)
