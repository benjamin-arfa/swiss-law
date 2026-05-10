"""SR 171.13 Art. 34

Generated from: ch/171/de/171.13.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sitzungsbeginn_montag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Sitzungsbeginn am Montag (Uhrzeit als Dezimalzahl)"
    reference = "SR 171.13 Art. 34 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        return 14.5


class sitzungsende_montag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Sitzungsende am Montag (Uhrzeit als Dezimalzahl)"
    reference = "SR 171.13 Art. 34 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        return 19.0


class nachtsitzung_beginn(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Beginn einer Nachtsitzung (Uhrzeit als Dezimalzahl)"
    reference = "SR 171.13 Art. 34 Abs. 2"

    def formula(person, period, parameters):
        return 19.0


class nachtsitzung_ende(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Ende einer Nachtsitzung (Uhrzeit als Dezimalzahl)"
    reference = "SR 171.13 Art. 34 Abs. 2"

    def formula(person, period, parameters):
        return 22.0
