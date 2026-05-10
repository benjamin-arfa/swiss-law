"""SR 425.1 Art. 7

Generated from: ch/425/de/425.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class maximale_anzahl_institutsratsmitglieder(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Anzahl Mitglieder des Institutsrats"
    reference = "SR 425.1 Art. 7 Abs. 2"

    def formula(person, period, parameters):
        return 9


class amtsdauer_institutsrat_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Amtsdauer der Institutsratsmitglieder in Jahren"
    reference = "SR 425.1 Art. 7 Abs. 5"

    def formula(person, period, parameters):
        return 4


class maximale_wiederwahlen_institutsrat(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Anzahl Wiederwahlen der Institutsratsmitglieder"
    reference = "SR 425.1 Art. 7 Abs. 5"

    def formula(person, period, parameters):
        return 2
