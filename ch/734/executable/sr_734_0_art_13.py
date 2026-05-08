"""SR 734.0 Art. 13

Generated from: ch/734/de/734.0.md

Art. 13: Geltungsbereich Starkstromanlagen
- Abs. 1: Alle Starkstromanlagen fallen unter die Bestimmungen dieses Gesetzes.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class eleg_starkstrom_unter_gesetz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Starkstromanlage faellt unter das EleG (alle Starkstromanlagen)"
    reference = "SR 734.0 Art. 13 Abs. 1"

    def formula(person, period, parameters):
        return person('eleg_anlage_ist_starkstrom', period)
