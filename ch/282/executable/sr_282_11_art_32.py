"""SR 282.11 Art. 32 - Entscheid und provisorische Stundung

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class provisorische_stundung_maximale_dauer_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Dauer der provisorischen Stundung vor Beiratschaftsbestellung in Monaten"
    reference = "SR 282.11 Art. 32 Abs. 3"

    def formula(self, period, parameters):
        return 3
