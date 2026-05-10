"""SR 730.022.2 Art. 4

Generated from: ch/730/fr/730.022.2.md

Art. 4 - Calculation of primary energy gasoline equivalents:
Conversion factors from fuel consumption to primary energy gasoline equivalents:
  a. Diesel: consumption (l/100km) * 1.09
  b. Natural gas: consumption (m3/100km) * 0.78 l/m3
  c. LPG: consumption (l/100km) * 0.78
  d. E85: consumption (l/100km) * 1.67
  e. Electricity: consumption (kWh/100km) * 0.17 l/kWh
  f. Hydrogen: consumption (m3/100km) * 0.61 l/m3
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class oee_vvt_equivalent_essence_primaire_total(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Total primary energy gasoline equivalent from all fuel types (l/100km)"
    reference = "SR 730.022.2 Art. 4"

    def formula(person, period, parameters):
        p = parameters(period).sr_730_022_2

        essence = person('oee_vvt_consommation_essence_l', period)
        diesel = person('oee_vvt_consommation_diesel_l', period)
        gaz = person('oee_vvt_consommation_gaz_naturel_m3', period)
        gpl = person('oee_vvt_consommation_gpl_l', period)
        e85 = person('oee_vvt_consommation_e85_l', period)
        elec = person('oee_vvt_consommation_electricite_kwh', period)
        h2 = person('oee_vvt_consommation_hydrogene_m3', period)

        return (
            essence  # Gasoline is the reference, factor = 1.0
            + diesel * p.facteur_primaire_diesel
            + gaz * p.facteur_primaire_gaz_naturel
            + gpl * p.facteur_primaire_gpl
            + e85 * p.facteur_primaire_e85
            + elec * p.facteur_primaire_electricite
            + h2 * p.facteur_primaire_hydrogene
        )
