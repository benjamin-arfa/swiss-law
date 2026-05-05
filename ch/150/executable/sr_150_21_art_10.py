"""SR 150.21 Art. 10

Generated from: ch/150/de/150.21.md

Aufbewahrungsdauer und Archivierung: Daten werden 20 Jahre nach erster
Erfassung vernichtet. Archivierung nach DSG und Archivierungsgesetz.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class aufbewahrungsdauer_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Aufbewahrungsdauer der Daten im System in Jahren"
    reference = "SR 150.21 Art. 10 Abs. 1"
    default_value = 20
