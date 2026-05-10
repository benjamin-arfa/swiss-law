"""SR 744.103 Art. 2

Generated from: ch/744/de/744.103.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vostra_privatauszug_vorgelegt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person hat einen Privatauszug aus dem Strafregister-Informationssystem VOSTRA vorgelegt"
    reference = "SR 744.103 Art. 2"

    def formula(person, period, parameters):
        return person('vostra_privatauszug_eingereicht', period)


class vostra_privatauszug_alter_monate(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Alter des VOSTRA-Privatauszugs in Monaten"
    reference = "SR 744.103 Art. 2"


class vostra_privatauszug_nicht_aelter_als_drei_monate(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "VOSTRA-Privatauszug ist nicht älter als drei Monate"
    reference = "SR 744.103 Art. 2"

    def formula(person, period, parameters):
        alter = person('vostra_privatauszug_alter_monate', period)
        return alter <= 3


class vostra_privatauszug_eingereicht(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Privatauszug aus VOSTRA wurde eingereicht (Eingabevariable)"
    reference = "SR 744.103 Art. 2"


class zuverlaessigkeit_nachgewiesen(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Zuverlässigkeit des Verkehrsleiters/der Verkehrsleiterin ist nachgewiesen gemäss SR 744.103 Art. 2"
    reference = "SR 744.103 Art. 2"

    def formula(person, period, parameters):
        auszug_vorgelegt = person('vostra_privatauszug_vorgelegt', period)
        auszug_aktuell = person('vostra_privatauszug_nicht_aelter_als_drei_monate', period)
        return auszug_vorgelegt * auszug_aktuell
