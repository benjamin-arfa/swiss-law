"""SR 362 Art. 2

Generated from: ch/de/362.md

Authorization for the Federal Council to conclude supplementary
agreements with Denmark and Norway/Iceland regarding Schengen and Dublin.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class daenemark_schengen_abkommen_ermaechtigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Bundesrat ermaechtigt ist, das Abkommen mit Daenemark zur Schengener Zusammenarbeit abzuschliessen"
    reference = "SR 362 Art. 2 Bst. a"


class daenemark_dublin_protokoll_ermaechtigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Bundesrat ermaechtigt ist, das Protokoll mit Daenemark zum Dublin-Abkommen abzuschliessen"
    reference = "SR 362 Art. 2 Bst. b"
