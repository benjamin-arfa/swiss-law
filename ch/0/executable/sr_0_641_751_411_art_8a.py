"""SR 0.641.751.411 Art. 8a - Fuel compensation obligation

Art. 8a: Liechtenstein guarantees measures equivalent to Swiss rules
for compensating greenhouse gas emissions from fossil fuel use.
- Par. 2: Emissions from fossil fuels marketed in LI serve as basis
- Par. 3: Swiss authorities account for LI quantities in computing
  the total emissions to compensate in Switzerland

Generated from: ch/0/fr/0.641.751.411.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_switzerland.entities import Person


class emissions_ges_carburants_li(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "GHG emissions from fossil fuels marketed in Liechtenstein in tonnes CO2eq (Art. 8a par. 2)"
    default_value = 0


class obligation_compensation_li(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "LI must take measures equivalent to Swiss fuel compensation rules (Art. 8a par. 1)"
    default_value = True


class emissions_li_prises_en_compte_ch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "LI emissions accounted for in Swiss total compensation calculation (Art. 8a par. 3)"
    default_value = True
