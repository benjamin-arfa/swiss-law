"""SR 813.1 Art. 1

Generated from: ch/813/de/813.1.md

Zweck: Schutz des Lebens und der Gesundheit vor schaedlichen Einwirkungen
durch Stoffe und Zubereitungen (Chemikaliengesetz, ChemG).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class chemg_schutz_leben_gesundheit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Schutz des Lebens und der Gesundheit vor schaedlichen Einwirkungen durch Stoffe und Zubereitungen anwendbar ist"
    reference = "SR 813.1 Art. 1"

    def formula(person, period, parameters):
        """ChemG schuetzt das Leben und die Gesundheit des Menschen vor
        schaedlichen Einwirkungen durch Stoffe und Zubereitungen."""
        return True
