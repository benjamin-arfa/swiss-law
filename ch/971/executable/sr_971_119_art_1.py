"""SR 971.119 Art. 1

Generated from: ch/971/de/971.119.md

Beitritt der Schweiz zum Internationalen konsultativen Baumwollkomitee
(International Cotton Advisory Committee) wird genehmigt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class beitritt_baumwollkomitee_genehmigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Beitritt der Schweiz zum Internationalen konsultativen Baumwollkomitee genehmigt ist"
    reference = "SR 971.119 Art. 1"

    def formula_1951(person, period, parameters):
        """Genehmigt seit 26. April 1951."""
        return True
