"""SR 362 Art. 3

Generated from: ch/de/362.md

Amendments to federal laws required by the Schengen/Dublin association.
The specific amendments can be consulted under AS 2008 447.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bundesgesetze_schengen_dublin_geaendert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Bundesgesetze gemaess Art. 3 geaendert wurden (AS 2008 447)"
    reference = "SR 362 Art. 3"
