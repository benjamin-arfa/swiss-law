"""SR 311.1 Art. 36

Generated from: ch/311/de/311.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class strafdrohung_erwachsene_freiheitsstrafe_max_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Hoechststrafe fuer das Erwachsenendelikt in Jahren Freiheitsstrafe"
    reference = "SR 311.1 Art. 36"


class verfolgungsverjaehrung_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Verfolgungsverjaehrungsfrist in Jahren"
    reference = "SR 311.1 Art. 36 Abs. 1"

    def formula(person, period, parameters):
        strafdrohung = person('strafdrohung_erwachsene_freiheitsstrafe_max_jahre', period)
        return where(
            strafdrohung > 3,
            5,
            where(
                strafdrohung > 0,
                3,
                1
            )
        )
