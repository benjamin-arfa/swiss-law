"""SR 143.13 Art. 1

Generated from: ch/143/de/143.13.md

Pass 2010: Einfuehrung auf den 1. Maerz 2010. Ab diesem Datum
darf nur noch der Pass 2010 ausgestellt werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class datum_passantrag(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Datum des Passantrags (YYYY-MM-DD)"
    reference = "SR 143.13 Art. 1"


class darf_nur_pass_2010_ausgestellt_werden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob nur noch der Pass 2010 ausgestellt werden darf (ab 1. Maerz 2010)"
    reference = "SR 143.13 Art. 1 Abs. 2"
    default_value = True
