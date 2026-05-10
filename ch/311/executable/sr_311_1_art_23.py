"""SR 311.1 Art. 23

Generated from: ch/311/de/311.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class verbrechen_oder_vergehen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat der Jugendliche ein Verbrechen oder Vergehen begangen"
    reference = "SR 311.1 Art. 23"


class persoenliche_leistung_max_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Dauer der persoenlichen Leistung in Tagen"
    reference = "SR 311.1 Art. 23 Abs. 3"

    def formula(person, period, parameters):
        alter = person('alter_bei_tat', period)
        verbrechen = person('verbrechen_oder_vergehen', period)
        # Under 15: max 10 days
        # 15+ with crime/misdemeanor: up to 3 months (~90 days)
        return where(
            (alter >= 15) * verbrechen,
            90,
            10
        )
