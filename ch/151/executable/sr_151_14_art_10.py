"""SR 151.14 Art. 10

Generated from: ch/151/de/151.14.md

Spaetester Zeitpunkt der ersten Lohngleichheitsanalyse: 30. Juni 2021.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class lohngleichheitsanalyse_frist(Variable):
    value_type = date
    entity_key = 'person'
    definition_period = YEAR
    label = "Frist fuer die erste Lohngleichheitsanalyse (30. Juni 2021)"
    reference = "SR 151.14 Art. 10"
