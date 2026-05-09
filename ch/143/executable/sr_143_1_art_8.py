"""SR 143.1 Art. 8 - Verlust (Loss of Identity Document)

Generated from: ch/143/de/143.1.md

Every loss of a document must be reported to the police.
The police enters the loss into RIPOL, which automatically
forwards it to the information system (Art. 11).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ausweis_verlust_gemeldet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Verlust des Ausweises der Polizei angezeigt wurde"
    reference = "SR 143.1 Art. 8"


class ausweis_in_ripol_als_verloren(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der verlorene Ausweis im RIPOL erfasst ist"
    reference = "SR 143.1 Art. 8"

    def formula(person, period, parameters):
        return person('ausweis_verlust_gemeldet', period)
