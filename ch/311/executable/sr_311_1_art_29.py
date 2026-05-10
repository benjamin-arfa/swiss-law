"""SR 311.1 Art. 29

Generated from: ch/311/de/311.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class probezeit_bedingte_entlassung_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Probezeit bei bedingter Entlassung in Monaten (entspricht Strafrest, min 6, max 24)"
    reference = "SR 311.1 Art. 29 Abs. 1"

    def formula(person, period, parameters):
        dauer = person('freiheitsentzug_dauer_tage', period)
        verbuesst = person('freiheitsentzug_verbuesst_tage', period)
        strafrest_monate = (dauer - verbuesst) / 30  # approximate
        return where(
            strafrest_monate < 6,
            6,
            where(strafrest_monate > 24, 24, strafrest_monate)
        )
