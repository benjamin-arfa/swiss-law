"""SR 151.14 Art. 10

Generated from: ch/151/de/151.14.md

Employers per Art. 13a GlG must complete the first pay equality analysis
by 30 June 2021 at the latest (Art. 17a Abs. 1 GlG).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class glg_erste_analyse_frist(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die erste Lohngleichheitsanalyse fristgerecht bis zum 30. Juni 2021 durchgefuehrt wurde"
    reference = "SR 151.14 Art. 10"

    def formula_2021(person, period, parameters):
        return person('glg_lohngleichheitsanalyse_durchgefuehrt', period)
