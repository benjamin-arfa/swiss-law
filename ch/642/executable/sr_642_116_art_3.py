"""SR 642.116 Art. 3

Generated from: ch/642/de/642.116.md

Art. 3: Replacement construction (Ersatzneubau)

A replacement construction is a building erected within a reasonable
time on the same plot after demolition of a residential or mixed-use
building, with the same type of use.

This is a definitional article; no calculable formula.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class liegenschaft_ist_ersatzneubau(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Der Bau gilt als Ersatzneubau (gleicher Standort, gleichartige Nutzung, angemessene Frist)"
    reference = "SR 642.116 Art. 3"
