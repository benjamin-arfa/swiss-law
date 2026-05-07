"""SR 725.11 Art. 8

Generated from: ch/725/de/725.11.md

Strassenhoheit und Eigentum: Nationalstrassen stehen unter der
Strassenhoheit und im Eigentum des Bundes. Nebenanlagen stehen
im Eigentum der Kantone.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_nebenanlage(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Anlage eine Nebenanlage im Sinne von Art. 7 ist"
    reference = "SR 725.11 Art. 8 Abs. 2"


class eigentuemer_ist_bund(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Strasse/Anlage im Eigentum des Bundes steht"
    reference = "SR 725.11 Art. 8"

    def formula(person, period, parameters):
        ist_ns = person('ist_nationalstrasse', period)
        ist_neben = person('ist_nebenanlage', period)

        # Nationalstrassen: Eigentum Bund; Nebenanlagen: Eigentum Kanton
        return ist_ns * (1 - ist_neben)
