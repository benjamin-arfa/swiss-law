"""SR 523.51 Art. 6

Generated from: ch/523/de/523.51.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class einzelleistung_note(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Note fuer eine Einzelleistung (1.0 bis 6.0, ganze oder halbe Noten)"
    reference = "SR 523.51 Art. 6"

    def formula(person, period, parameters):
        raw = person('einzelleistung_note_roh', period)
        # Clamp to valid range 1.0 - 6.0, round to nearest 0.5
        clamped = max_(min_(raw, 6.0), 1.0)
        return round_(clamped * 2) / 2


class einzelleistung_note_roh(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Rohe Note fuer eine Einzelleistung (vor Rundung)"
    reference = "SR 523.51 Art. 6"
