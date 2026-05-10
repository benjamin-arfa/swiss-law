"""SR 151.1 Art. 4

Generated from: ch/151/de/151.1.md

Diskriminierung durch sexuelle Belaestigung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sexuelle_belaestigung_am_arbeitsplatz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob sexuelle Belaestigung am Arbeitsplatz vorliegt"
    reference = "SR 151.1 Art. 4"


class diskriminierung_durch_sexuelle_belaestigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Diskriminierung durch sexuelle Belaestigung vorliegt"
    reference = "SR 151.1 Art. 4"

    def formula(person, period, parameters):
        return person('sexuelle_belaestigung_am_arbeitsplatz', period)
