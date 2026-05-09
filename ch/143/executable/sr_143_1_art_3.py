"""SR 143.1 Art. 3 - Gueltigkeitsdauer (Validity Period)

Generated from: ch/143/de/143.1.md

Identity documents have a limited validity period, regulated by the Federal Council.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ausweis_gueltigkeitsdauer_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Gueltigkeitsdauer des Ausweises in Jahren (vom Bundesrat geregelt)"
    reference = "SR 143.1 Art. 3"


class ausweis_ist_gueltig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Ausweis noch gueltig ist (innerhalb der Gueltigkeitsdauer)"
    reference = "SR 143.1 Art. 3"
