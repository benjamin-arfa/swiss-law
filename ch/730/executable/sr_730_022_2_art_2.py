"""SR 730.022.2 Art. 2

Generated from: ch/730/fr/730.022.2.md

Art. 2 - Average CO2 emissions:
The average CO2 emissions of newly registered passenger vehicles
is 149 g/km for the year 2022.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class oee_vvt_moyenne_co2_reference_g_km(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Reference average CO2 emissions of newly registered passenger vehicles (g/km)"
    reference = "SR 730.022.2 Art. 2"

    def formula(person, period, parameters):
        p = parameters(period).sr_730_022_2
        return p.moyenne_co2_g_km + 0 * person('oee_vvt_consommation_essence_l', period)
