"""SR 730.022.2 Art. 5

Generated from: ch/730/fr/730.022.2.md

Art. 5 - CO2 emissions from fuel/electricity supply:
CO2 emission factors for upstream supply chain (g CO2/km):
  a. Gasoline: consumption (l/100km) * 506 g CO2/l
  b. Diesel: consumption (l/100km) * 484 g CO2/l
  c. Natural gas: consumption (m3/100km) * 273 g CO2/m3
  d. LPG: consumption (l/100km) * 390 g CO2/l
  e. E85: consumption (l/100km) * 464 g CO2/l
  f. Electricity: consumption (kWh/100km) * 25 g CO2/kWh
  g. Hydrogen: consumption (m3/100km) * 68 g CO2/m3
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class oee_vvt_co2_fourniture_g_km(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "CO2 emissions from fuel/electricity supply chain (g CO2/km)"
    reference = "SR 730.022.2 Art. 5"

    def formula(person, period, parameters):
        p = parameters(period).sr_730_022_2

        essence = person('oee_vvt_consommation_essence_l', period)
        diesel = person('oee_vvt_consommation_diesel_l', period)
        gaz = person('oee_vvt_consommation_gaz_naturel_m3', period)
        gpl = person('oee_vvt_consommation_gpl_l', period)
        e85 = person('oee_vvt_consommation_e85_l', period)
        elec = person('oee_vvt_consommation_electricite_kwh', period)
        h2 = person('oee_vvt_consommation_hydrogene_m3', period)

        # CO2 per 100km, divide by 100 to get g/km
        co2_par_100km = (
            essence * p.co2_essence_g_l
            + diesel * p.co2_diesel_g_l
            + gaz * p.co2_gaz_naturel_g_m3
            + gpl * p.co2_gpl_g_l
            + e85 * p.co2_e85_g_l
            + elec * p.co2_electricite_g_kwh
            + h2 * p.co2_hydrogene_g_m3
        )

        return co2_par_100km / 100
