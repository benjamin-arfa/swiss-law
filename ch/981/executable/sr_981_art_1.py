"""SR 981 Art. 1

Generated from: ch/de/981.md

Purpose: regulates the determination of compensation claims of the
Confederation under international law, and the execution of
corresponding compensation agreements.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class entschaedigung_anspruch_ermittlung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Ermittlung von Entschaedigungsanspruechen der Eidgenossenschaft wegen Eingriffen auslaendischer Staaten geregelt ist"
    reference = "SR 981 Art. 1 Bst. a"


class entschaedigungsabkommen_vollzug(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Vollzug der Entschaedigungsabkommen geregelt ist"
    reference = "SR 981 Art. 1 Bst. b"
