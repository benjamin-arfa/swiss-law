"""SR 120.4 Art. 9

Generated from: ch/120/de/120.4.md

Pruefstufen: Three levels of personnel security checks.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class PRUEFSTUFE(Enum):
    keine = "Keine Pruefung"
    grundsicherheitspruefung = "Grundsicherheitspruefung"
    erweiterte_psp = "Erweiterte Personensicherheitspruefung"
    erweiterte_psp_mit_befragung = "Erweiterte Personensicherheitspruefung mit Befragung"


class psp_pruefstufe(Variable):
    value_type = Enum
    possible_values = PRUEFSTUFE
    default_value = PRUEFSTUFE.keine
    entity_key = 'person'
    definition_period = YEAR
    label = "Pruefstufe der Personensicherheitspruefung"
    reference = "SR 120.4 Art. 9 Abs. 1"
