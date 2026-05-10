"""SR 0.101 Art. 16

Generated from: ch/0/de/0.101.md

Restrictions on political activity of aliens: Articles 10, 11 and 14
shall not prevent the High Contracting Parties from imposing restrictions
on the political activity of aliens.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class emrk_person_ist_auslaender(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person eine auslaendische Person ist"
    reference = "SR 0.101 Art. 16"


class emrk_beschraenkung_politische_taetigkeit_auslaender(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Beschraenkung der politischen Taetigkeit von Auslaendern zulaessig ist"
    reference = "SR 0.101 Art. 16"

    def formula(person, period, parameters):
        return person('emrk_person_ist_auslaender', period)
