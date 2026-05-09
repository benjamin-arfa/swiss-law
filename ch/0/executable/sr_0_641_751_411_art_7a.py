"""SR 0.641.751.411 Art. 7a - Emission reduction certificates 2013-2024

Art. 7a: For the 2013-2024 period:
- Par. 1: LI companies surrender emission reduction certificates to Swiss authorities
- Par. 2: Swiss authorities cancel all certificates at end of period
- Par. 4: LI companies pay sanction amounts to Swiss authorities
- Par. 5: Swiss authorities transfer sanctions paid by LI companies back to LI

Generated from: ch/0/fr/0.641.751.411.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_switzerland.entities import Person


class certificats_reduction_emissions_li(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Number of emission reduction certificates surrendered by LI companies (Art. 7a par. 1)"
    default_value = 0


class sanctions_taxe_co2_li(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Sanction amounts paid by LI companies for CO2 non-compliance (Art. 7a par. 4)"
    default_value = 0


class transfert_sanctions_vers_li(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Sanctions transferred from Swiss to LI authorities at period end (Art. 7a par. 5)"

    def formula(person, period, parameters):
        return person("sanctions_taxe_co2_li", period)
