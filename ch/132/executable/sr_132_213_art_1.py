"""SR 132.213 Art. 1 - Genehmigung Gebietsveraenderung

Generated from: ch/132/de/132.213.md

Die Gebietsveraenderung zwischen den Kantonen Bern und Jura betreffend den
Wechsel der Gemeinde Moutier vom Kanton Bern zum Kanton Jura wird genehmigt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class moutier_kantonswechsel_genehmigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Gebietsveraenderung (Kantonswechsel Moutier von Bern nach Jura) genehmigt ist"
    reference = "SR 132.213 Art. 1"

    def formula_2026_01_01(person, period, parameters):
        # Ab 1. Januar 2026 ist der Kantonswechsel genehmigt
        return True
