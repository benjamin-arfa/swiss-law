"""SR 141.0 Art. 42 - Entzug des Buergerrechts

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_doppelbuerger(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person ist Doppelbuergerin oder Doppelbuerger"
    reference = "SR 141.0 Art. 42"


class verhalten_schaedigt_interessen_ansehen_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Verhalten der Person ist den Interessen oder dem Ansehen der Schweiz erheblich nachteilig"
    reference = "SR 141.0 Art. 42"


class zustimmung_heimatkanton(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Behoerde des Heimatkantons stimmt dem Entzug zu"
    reference = "SR 141.0 Art. 42"


class entzug_buergerrecht_moeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Entzug des Schweizer Buergerrechts ist moeglich"
    reference = "SR 141.0 Art. 42"

    def formula(self, period, parameters):
        doppelbuerger = self('ist_doppelbuerger', period)
        schaedigt = self('verhalten_schaedigt_interessen_ansehen_schweiz', period)
        zustimmung = self('zustimmung_heimatkanton', period)
        return doppelbuerger * schaedigt * zustimmung
