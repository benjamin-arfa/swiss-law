"""SR 0.641.751.411 Art. 6 - CO2 tax revenue sharing

Art. 6: CO2 tax revenues paid into a common fund.
- Par. 2: Liechtenstein receives its share per Appendix III formula.
- Par. 3: CO2 tax refunds to Liechtenstein companies follow Swiss principles.

Generated from: ch/0/fr/0.641.751.411.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_switzerland.entities import Person


class recettes_taxe_co2(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Total CO2 tax revenues from both territories (Art. 6 par. 1)"
    default_value = 0


class part_li_taxe_co2(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Liechtenstein's share of CO2 tax revenues per Appendix III (Art. 6 par. 2)"
    default_value = 0


class retrocession_taxe_co2_entreprises_li(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "CO2 tax refund to LI companies follows Swiss principles (Art. 6 par. 3)"
    default_value = True
