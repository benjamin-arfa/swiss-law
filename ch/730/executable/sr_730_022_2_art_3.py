"""SR 730.022.2 Art. 3

Generated from: ch/730/fr/730.022.2.md

Art. 3 - Calculation of gasoline equivalents for passenger vehicles:
Conversion factors from fuel consumption to gasoline equivalents:
  a. Diesel: consumption (l/100km) * 1.14
  b. Natural gas: consumption (m3/100km) * 1.03 l/m3
  c. LPG: consumption (l/100km) * 0.80
  d. E85: consumption (l/100km) * 0.72
  e. Electricity: consumption (kWh/100km) * 0.11 l/kWh
  f. Hydrogen: consumption (m3/100km) * 0.34 l/m3
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class oee_vvt_consommation_diesel_l(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Diesel consumption (l/100km)"
    reference = "SR 730.022.2 Art. 3"
    default_value = 0


class oee_vvt_consommation_gaz_naturel_m3(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Natural gas consumption (m3/100km)"
    reference = "SR 730.022.2 Art. 3"
    default_value = 0


class oee_vvt_consommation_gpl_l(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "LPG consumption (l/100km)"
    reference = "SR 730.022.2 Art. 3"
    default_value = 0


class oee_vvt_consommation_e85_l(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "E85 fuel consumption (l/100km)"
    reference = "SR 730.022.2 Art. 3"
    default_value = 0


class oee_vvt_consommation_electricite_kwh(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Electricity consumption (kWh/100km)"
    reference = "SR 730.022.2 Art. 3"
    default_value = 0


class oee_vvt_consommation_hydrogene_m3(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hydrogen consumption (m3/100km)"
    reference = "SR 730.022.2 Art. 3"
    default_value = 0


class oee_vvt_consommation_essence_l(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gasoline (petrol) consumption (l/100km)"
    reference = "SR 730.022.2 Art. 3"
    default_value = 0


class oee_vvt_equivalent_essence_total(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Total gasoline equivalent consumption from all fuel types (l/100km)"
    reference = "SR 730.022.2 Art. 3"

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
            + diesel * p.facteur_diesel
            + gaz * p.facteur_gaz_naturel
            + gpl * p.facteur_gpl
            + e85 * p.facteur_e85
            + elec * p.facteur_electricite
            + h2 * p.facteur_hydrogene
        )
