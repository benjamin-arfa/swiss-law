"""SR 132.213 Art. 1

Generated from: ch/132/de/132.213.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class gemeinde_moutier_kantonswechsel_genehmigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Gebietsveraenderung zwischen den Kantonen Bern und Jura betreffend den Wechsel der Gemeinde Moutier vom Kanton Bern zum Kanton Jura ist genehmigt"
    reference = "SR 132.213 Art. 1"

    def formula_2026_01_01(self, period, parameters):
        return True
