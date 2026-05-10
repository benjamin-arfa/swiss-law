"""SR 120.4 Art. 19

Generated from: ch/120/de/120.4.md

Datenerhebung: Data collection and minimum time periods for checks.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class datenerhebung_mindestzeitraum_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Mindestzeitraum in Jahren fuer Datenerhebung bei der PSP"
    reference = "SR 120.4 Art. 19 Abs. 3"

    def formula(person, period, parameters):
        grundsicherheit = person('grundsicherheitspruefung_erforderlich', period)
        erweitert = person('erweiterte_psp_erforderlich', period)
        erweitert_befragung = person('erweiterte_psp_mit_befragung_erforderlich', period)

        # lit. a: 5 Jahre bei Grundsicherheitspruefung
        # lit. b: 10 Jahre bei erweiterter PSP oder erweiterter PSP mit Befragung
        return where(
            grundsicherheit,
            5,
            where(erweitert + erweitert_befragung > 0, 10, 0)
        )
