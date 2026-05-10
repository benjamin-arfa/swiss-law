"""SR 170.32 Art. 18

Generated from: ch/170/de/170.32.md

Verhältnis Disziplinarmassnahme zu Haftung und Strafrecht.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class disziplinarische_massnahme_ergriffen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eine disziplinarische Massnahme wurde ergriffen (Art. 18 Abs. 1 VG)"
    reference = "SR 170.32, Art. 18 Abs. 1"


class haftung_durch_disziplinarmassnahme_beruehrt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Haftung oder strafrechtliche Verantwortlichkeit durch Disziplinarmassnahme berührt (Art. 18 Abs. 1 VG)"
    reference = "SR 170.32, Art. 18 Abs. 1"

    def formula(person, period, parameters):
        # Haftung und Strafrecht werden durch Disziplin NICHT berührt
        return person('disziplinarische_massnahme_ergriffen', period) * 0
