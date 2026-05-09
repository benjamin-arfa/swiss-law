"""SR 971.119 Art. 2

Generated from: ch/971/de/971.119.md

Der Bundesrat wird ermaechtigt, den Beitritt der Schweiz zum
Internationalen konsultativen Baumwollkomitee zu vollziehen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bundesrat_ermaechtigt_beitritt_baumwollkomitee(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Bundesrat ermaechtigt ist, den Beitritt zum Baumwollkomitee zu vollziehen"
    reference = "SR 971.119 Art. 2"

    def formula_1951(person, period, parameters):
        """Ermaechtigung seit 26. April 1951."""
        return True
