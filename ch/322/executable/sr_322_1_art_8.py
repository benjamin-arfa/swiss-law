"""SR 322.1 Art. 8

Generated from: ch/322/de/322.1.md

Zusammensetzung: Die Militaergerichte werden gebildet aus einem Praesidenten
(Oberst oder Oberstleutnant), vier Richtern und einem Gerichtsschreiber.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class militaergericht_korrekt_zusammengesetzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Militaergericht gemaess Art. 8 korrekt zusammengesetzt ist"
    reference = "SR 322.1 Art. 8 Abs. 1"
