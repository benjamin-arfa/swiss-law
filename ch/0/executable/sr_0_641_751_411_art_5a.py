"""SR 0.641.751.411 Art. 5a - CO2 vehicle emission sanctions revenue sharing

Art. 5a: Revenue from sanctions on CO2 emissions of passenger cars,
delivery vehicles, light tractors, and heavy vehicles is paid into a
common fund. Liechtenstein receives its share per Appendix IV formula.

Generated from: ch/0/fr/0.641.751.411.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_switzerland.entities import Person


class recettes_sanctions_co2_vehicules(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Revenues from CO2 vehicle emission sanctions (Art. 5a par. 1)"
    default_value = 0


class part_li_sanctions_co2_vehicules(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Liechtenstein's share of CO2 vehicle sanction revenues (Art. 5a par. 2)"
    default_value = 0
