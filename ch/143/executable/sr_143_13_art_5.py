"""SR 143.13 Art. 5

Generated from: ch/143/de/143.13.md

Entry into force: 1 February 2010.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class sr_143_13_inkrafttreten(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Datum des Inkrafttretens der Verordnung SR 143.13"
    reference = "SR 143.13 Art. 5"
    default_value = "2010-02-01"
