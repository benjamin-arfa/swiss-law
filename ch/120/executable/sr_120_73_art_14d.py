"""SR 120.73 Art. 14d

Generated from: ch/120/de/120.73.md

Erhoehter Schutz: Enhanced protection when analysis shows elevated needs.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class erhoehter_schutzbedarf(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Schutzbedarfsanalyse einen erhoehten Schutzbedarf ergibt"
    reference = "SR 120.73 Art. 14d Abs. 1"


class zusaetzliche_sicherheitsmassnahmen_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob zusaetzliche Sicherheitsmassnahmen erforderlich sind"
    reference = "SR 120.73 Art. 14d Abs. 1"

    def formula(person, period, parameters):
        return person('erhoehter_schutzbedarf', period)
