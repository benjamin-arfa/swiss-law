"""SR 730.010.1 Art. 6

Generated from: ch/730/fr/730.010.1.md

Art. 6 - Determination of electricity quantity for pumped-storage:
1. When a hydroelectric installation uses pumping, the electricity quantity
   is calculated as: injected electricity minus (pumping electricity * 83%
   efficiency coefficient). Any negative balance from previous period is
   also deducted.
2. If actual efficiency is below 83% on annual average, the producer may
   request a lower value based on an independent study.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ogom_electricite_injectee_kwh(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Electricity injected into the grid (kWh)"
    reference = "SR 730.010.1 Art. 6 Abs. 1"


class ogom_electricite_pompage_kwh(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Electricity used for pumping (kWh)"
    reference = "SR 730.010.1 Art. 6 Abs. 1"


class ogom_solde_negatif_precedent_kwh(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Negative balance carried forward from previous period (kWh, positive value)"
    reference = "SR 730.010.1 Art. 6 Abs. 1"
    default_value = 0


class ogom_coefficient_efficacite(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Efficiency coefficient for pumped-storage deduction (default 83%)"
    reference = "SR 730.010.1 Art. 6 Abs. 1-2"

    def formula(person, period, parameters):
        coefficient_personnalise = person('ogom_coefficient_efficacite_personnalise', period)
        p = parameters(period).sr_730_010_1
        default_coeff = p.coefficient_efficacite_pompage

        return where(
            coefficient_personnalise > 0,
            coefficient_personnalise,
            default_coeff
        )


class ogom_coefficient_efficacite_personnalise(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Custom efficiency coefficient approved by execution body (0 = use default)"
    reference = "SR 730.010.1 Art. 6 Abs. 2"
    default_value = 0


class ogom_production_pompage_turbinage_kwh(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Net electricity attributable to natural sources after pumped-storage deduction (kWh)"
    reference = "SR 730.010.1 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        injectee = person('ogom_electricite_injectee_kwh', period)
        pompage = person('ogom_electricite_pompage_kwh', period)
        solde_negatif = person('ogom_solde_negatif_precedent_kwh', period)
        coeff = person('ogom_coefficient_efficacite', period)

        # Deduct: pumping energy * efficiency coefficient + previous negative balance
        deduction_pompage = pompage * coeff
        production_nette = injectee - deduction_pompage - solde_negatif

        # Result can be negative (carried forward to next period)
        return production_nette
