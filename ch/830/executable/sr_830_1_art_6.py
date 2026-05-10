"""SR 830.1 Art. 6

Generated from: ch/830/de/830.1.md

Art. 6: Arbeitsunfähigkeit - Full or partial inability to perform reasonable
work in one's current occupation or area of activity, caused by a health
impairment.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class grad_arbeitsunfaehigkeit(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = (
        "Grad der Arbeitsunfähigkeit (0.0 bis 1.0): durch Beeinträchtigung der "
        "Gesundheit bedingte Unfähigkeit, im bisherigen Beruf oder Aufgabenbereich "
        "zumutbare Arbeit zu leisten (Art. 6 ATSG)"
    )
    reference = "SR 830.1 Art. 6"


class ist_arbeitsunfaehig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person ist arbeitsunfähig im Sinne von Art. 6 ATSG"
    reference = "SR 830.1 Art. 6"

    def formula(person, period, parameters):
        return person('grad_arbeitsunfaehigkeit', period) > 0
