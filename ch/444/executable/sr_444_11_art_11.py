"""SR 444.11 Art. 11

Generated from: ch/444/de/444.11.md

Finanzhilfen fuer treuhänderische Aufbewahrung: Max 100'000 CHF pro Jahr.
Nur an Museen mit anerkannter Fachwelt-Taetigkeit und ICOM-Kodex.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class max_finanzhilfe_treuhaenderisch(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Finanzhilfe fuer treuhaenderische Aufbewahrung (100'000 CHF/Jahr)"
    reference = "SR 444.11 Art. 11 Abs. 1"
    default_value = 100000
