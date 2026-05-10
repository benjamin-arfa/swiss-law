"""SR 822.11 Art. 18 - Sonntagsarbeit: Verbot

Generated from: ch/de/822/822.11.md

Sunday work prohibition:
- Prohibited from Saturday 23:00 to Sunday 23:00
- Shift by max 1 hour with employee representative consent
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sonntagsarbeit_geleistet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Sonntagsarbeit geleistet wird"
    reference = "SR 822.11 Art. 18 Abs. 1"


class sonntagsarbeit_bewilligt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine Bewilligung fuer Sonntagsarbeit vorliegt"
    reference = "SR 822.11 Art. 19"


class sonntagsarbeit_verbot_verletzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Sonntagsarbeitsverbot verletzt ist (Arbeit ohne Bewilligung)"
    reference = "SR 822.11 Art. 18"

    def formula(person, period, parameters):
        geleistet = person('sonntagsarbeit_geleistet', period)
        bewilligt = person('sonntagsarbeit_bewilligt', period)
        return geleistet * (1 - bewilligt)
