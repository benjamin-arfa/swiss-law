"""SR 0.101.094 Art. 17

Generated from: ch/0/de/0.101.094.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class Beitragsänderung_Stand_Referenzjahr(variables.Variable):
    label = "Beitragsänderung Stand Referenzjahr"
    reference = "SR 0.101.094 Art. 17"

    def formula_2020(p, period, transition, parameters):
        return 0

    def formula(year, period, transition, parameters):
        return 0
