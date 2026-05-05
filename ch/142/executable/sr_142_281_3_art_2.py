"""SR 142.281.3 Art. 2

Generated from: ch/142/de/142.281.3.md

Sicherheitszuschlag: 85'000 Franken pro Haftplatz.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class sicherheitszuschlag_pro_haftplatz(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Sicherheitszuschlag pro Haftplatz (CHF)"
    reference = "SR 142.281.3 Art. 2"
    default_value = 85000
