"""SR 642.11 Art. 14

Generated from: ch/642/fr/642.11.md

Art. 14 Imposition d'après la dépense (Expenditure-based taxation):
Conditions for being taxed based on living expenses instead of income:
1. The taxpayer must:
   a. Not have Swiss nationality
   b. Be subject to unlimited tax liability (Art. 3) for the first time
      or after an absence of at least 10 years
   c. Not exercise a gainful activity in Switzerland
2. Both spouses must meet the conditions if living together.
3. Tax is calculated on annual living expenses, but at minimum the highest of:
   a. CHF 435,000 per year (2026 value, adjusted for inflation)
   b. For heads of household: 7x the annual rent or rental value (Art. 21(1)(b))
   c. For others: 3x the annual cost of board and lodging
   d. The sum of gross Swiss-source income elements
4. Tax is levied at the ordinary rate schedule (Art. 36).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ifd_depense_nationalite_suisse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the taxpayer has Swiss nationality"
    reference = "SR 642.11 Art. 14 Abs. 1 Bst. a"


class ifd_depense_premier_assujettissement(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether this is the first unlimited tax liability or after 10+ years absence"
    reference = "SR 642.11 Art. 14 Abs. 1 Bst. b"


class ifd_depense_activite_lucrative_ch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the taxpayer exercises a gainful activity in Switzerland"
    reference = "SR 642.11 Art. 14 Abs. 1 Bst. c"


class ifd_depense_eligible(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the taxpayer is eligible for expenditure-based taxation"
    reference = "SR 642.11 Art. 14 Abs. 1"

    def formula(person, period, parameters):
        suisse = person('ifd_depense_nationalite_suisse', period)
        premier = person('ifd_depense_premier_assujettissement', period)
        activite = person('ifd_depense_activite_lucrative_ch', period)
        return not_(suisse) * premier * not_(activite)


class ifd_depense_train_de_vie(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Annual living expenses of the taxpayer and dependents (CHF)"
    reference = "SR 642.11 Art. 14 Abs. 3"


class ifd_depense_loyer_annuel(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Annual rent or rental value of primary residence (CHF)"
    reference = "SR 642.11 Art. 14 Abs. 3 Bst. b"


class ifd_depense_chef_menage(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the taxpayer is head of household"
    reference = "SR 642.11 Art. 14 Abs. 3 Bst. b"


class ifd_depense_pension_annuelle(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Annual cost of board and lodging at place of residence (CHF)"
    reference = "SR 642.11 Art. 14 Abs. 3 Bst. c"


class ifd_depense_revenus_suisses_bruts(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Sum of gross Swiss-source income elements (CHF)"
    reference = "SR 642.11 Art. 14 Abs. 3 Bst. d"


class ifd_depense_base_imposable(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Taxable base for expenditure-based taxation (CHF)"
    reference = "SR 642.11 Art. 14 Abs. 3"

    def formula(person, period, parameters):
        eligible = person('ifd_depense_eligible', period)
        train_de_vie = person('ifd_depense_train_de_vie', period)
        loyer = person('ifd_depense_loyer_annuel', period)
        chef = person('ifd_depense_chef_menage', period)
        pension = person('ifd_depense_pension_annuelle', period)
        revenus_ch = person('ifd_depense_revenus_suisses_bruts', period)
        minimum_legal = parameters(period).sr_642_11.imposition_depense_minimum

        # (b) 7x rent for heads of household
        controle_loyer = where(chef, loyer * 7, 0)
        # (c) 3x board/lodging for others
        controle_pension = where(not_(chef), pension * 3, 0)

        # Maximum of all control amounts
        controle = max_(minimum_legal,
                        max_(controle_loyer,
                             max_(controle_pension, revenus_ch)))

        # The higher of actual living expenses or control amount
        base = max_(train_de_vie, controle)

        return eligible * base
