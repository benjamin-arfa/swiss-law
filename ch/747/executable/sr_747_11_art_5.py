"""SR 747.11 Art. 5

Generated from: ch/747/de/747.11.md

Art. 5: Optional (voluntary) registration of inland vessels.
Requirements: carrying capacity >= 10t or displacement >= 5m³,
plus Art. 4 Abs. 1 conditions (Swiss ownership etc.)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class schiffsreg_fakultative_aufnahme(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Fakultative Aufnahme in das Schiffsregister möglich (Art. 5)"
    reference = "SR 747.11 Art. 5"

    def formula(person, period, parameters):
        eigentum_ch = person('schiffsreg_eigentumsanteil_schweiz', period)
        tragfaehigkeit = person('schiffsreg_tragfaehigkeit_tonnen', period)
        verdraengung = person('schiffsreg_wasserverdraengung_m3', period)
        ist_gueter = person('schiffsreg_ist_gueterschiff', period)

        p = parameters(period).sr_747_11

        # Swiss ownership >50%
        eigentum_ok = eigentum_ch > 0.5

        # Not used for commercial transport (otherwise Art. 4 applies)
        gewerbe = person('schiffsreg_gewerbsmaessige_befoerderung', period)
        nicht_gewerbe = not_(gewerbe)

        # Lower thresholds: 10t or 5m³
        groesse_ok = where(
            ist_gueter,
            tragfaehigkeit >= p.mindest_tragfaehigkeit_fakultativ,
            verdraengung >= p.mindest_verdraengung_fakultativ
        )

        return eigentum_ok * nicht_gewerbe * groesse_ok
