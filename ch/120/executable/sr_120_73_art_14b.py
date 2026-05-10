"""SR 120.73 Art. 14b

Generated from: ch/120/de/120.73.md

Schutzbedarfsanalyse: Protection needs analysis for IT assets.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class informatikschutzobjekt_vorhanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Informatikschutzobjekt vorhanden ist"
    reference = "SR 120.73 Art. 14b Abs. 1"


class schutzbedarfsanalyse_aktuell(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine aktuelle Schutzbedarfsanalyse vorliegt"
    reference = "SR 120.73 Art. 14b Abs. 1"


class schutzbedarfsanalyse_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Schutzbedarfsanalyse erforderlich ist"
    reference = "SR 120.73 Art. 14b Abs. 1"

    def formula(person, period, parameters):
        return (
            person('informatikschutzobjekt_vorhanden', period) *
            not_(person('schutzbedarfsanalyse_aktuell', period))
        )
