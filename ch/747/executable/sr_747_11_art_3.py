"""SR 747.11 Art. 3

Generated from: ch/747/de/747.11.md

Art. 3: Complaints against the ship register office - 30-day time limit
for complaints about rejection of registration, annotation, modification
or deletion; otherwise unlimited.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class schiffsreg_beschwerde_abweisung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Beschwerde betrifft Abweisung einer Eintragung/Vormerkung/Änderung/Löschung"
    reference = "SR 747.11 Art. 3 Abs. 1"


class schiffsreg_beschwerdefrist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Beschwerdefrist gegen das Schiffsregisteramt (Tage, 0 = unbefristet)"
    reference = "SR 747.11 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        ist_abweisung = person('schiffsreg_beschwerde_abweisung', period)
        # 30 days for rejection complaints, 0 (unlimited) otherwise
        return where(ist_abweisung, 30, 0)
