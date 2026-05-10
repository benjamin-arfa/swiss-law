"""SR 861 Art. 9a

Generated from: ch/de/861.md

Transitional provision: BSV grants financial aid under section 2
(Art. 2 and 3) until 31 January 2019 at the latest.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class finanzhilfe_abschnitt2_frist(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Finanzhilfen nach dem 2. Abschnitt (Art. 2 und 3) noch gewaehrt werden koennen"
    reference = "SR 861 Art. 9a"
