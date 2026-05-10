"""SR 642.11 Art. 33

Generated from: ch/642/fr/642.11.md

Art. 33 Intérêts passifs et autres réductions (Deductions from income):
Key computable provisions:
- (a) Private debt interest up to wealth income + CHF 50,000
- (d) AVS/AI/LPP statutory contributions (fully deductible)
- (e) Pillar 3a contributions (per federal schedule)
- (f) APG, unemployment and accident insurance contributions
- (g) Insurance/savings interest: max CHF 3,700 (married) / CHF 1,800 (single)
      + CHF 700 per child; doubled if no pillar 2/3a contributions
- (h) Medical expenses exceeding 5% of net income
- (i) Political party contributions up to CHF 10,600
- (j) Professional training costs up to CHF 13,000
Art. 33 Abs. 2: Dual-income deduction for married couples (50% of lower
  income, min CHF 8,600 / max CHF 14,100)
Art. 33 Abs. 3: Childcare costs up to CHF 25,800 per child under 14
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# --- Art. 33 Abs. 1 Bst. g: Insurance premiums and savings ---

class ifd_primes_assurance_versees(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Insurance premiums and savings interest actually paid (CHF)"
    reference = "SR 642.11 Art. 33 Abs. 1 Bst. g"


class ifd_cotisation_prevoyance_2e_3e(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the taxpayer pays pillar 2 or 3a contributions (Art. 33(1)(d)/(e))"
    reference = "SR 642.11 Art. 33 Abs. 1bis Bst. a"
    default_value = True


class ifd_deduction_assurance(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Deduction for insurance premiums and savings interest (CHF)"
    reference = "SR 642.11 Art. 33 Abs. 1 Bst. g"

    def formula(person, period, parameters):
        p = parameters(period).sr_642_11
        marie = person('ifd_marie_menage_commun', period)
        nb_enfants = person('ifd_nombre_enfants', period)
        nb_pers = person('ifd_nombre_personnes_a_charge', period)
        cotise_prevoyance = person('ifd_cotisation_prevoyance_2e_3e', period)
        primes = person('ifd_primes_assurance_versees', period)

        # Base max: married vs. single
        plafond_base = where(marie, p.deduction_insurance_married, p.deduction_insurance_single)

        # Art. 33(1bis)(a): doubled if no pillar 2/3a contributions
        plafond_base = where(cotise_prevoyance, plafond_base, plafond_base * 2)

        # Art. 33(1bis)(b): +700 per child/dependent
        plafond = plafond_base + (nb_enfants + nb_pers) * p.deduction_insurance_per_child

        return min_(primes, plafond)


# --- Art. 33 Abs. 1 Bst. i: Political party donations ---

class ifd_dons_partis_politiques(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Donations to political parties actually paid (CHF)"
    reference = "SR 642.11 Art. 33 Abs. 1 Bst. i"


class ifd_deduction_dons_partis(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Deduction for political party donations (CHF)"
    reference = "SR 642.11 Art. 33 Abs. 1 Bst. i"

    def formula(person, period, parameters):
        dons = person('ifd_dons_partis_politiques', period)
        plafond = parameters(period).sr_642_11.deduction_political_max
        return min_(dons, plafond)


# --- Art. 33 Abs. 1 Bst. j: Professional training ---

class ifd_frais_formation_verses(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Professional training/continuing education costs actually paid (CHF)"
    reference = "SR 642.11 Art. 33 Abs. 1 Bst. j"


class ifd_diplome_secondaire_ii(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the taxpayer holds a secondary-II diploma or is 20+ in non-first-diploma training"
    reference = "SR 642.11 Art. 33 Abs. 1 Bst. j"


class ifd_deduction_formation(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Deduction for professional training costs (CHF)"
    reference = "SR 642.11 Art. 33 Abs. 1 Bst. j"

    def formula(person, period, parameters):
        frais = person('ifd_frais_formation_verses', period)
        eligible = person('ifd_diplome_secondaire_ii', period)
        plafond = parameters(period).sr_642_11.deduction_training_max
        return eligible * min_(frais, plafond)


# --- Art. 33 Abs. 2: Dual-income deduction for married couples ---

class ifd_revenu_activite_conjoint_1(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Net employment income of spouse 1 (CHF)"
    reference = "SR 642.11 Art. 33 Abs. 2"


class ifd_revenu_activite_conjoint_2(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Net employment income of spouse 2 (CHF)"
    reference = "SR 642.11 Art. 33 Abs. 2"


class ifd_deduction_double_revenu(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Dual-income deduction for married couples (CHF)"
    reference = "SR 642.11 Art. 33 Abs. 2"

    def formula(person, period, parameters):
        p = parameters(period).sr_642_11
        marie = person('ifd_marie_menage_commun', period)
        rev1 = person('ifd_revenu_activite_conjoint_1', period)
        rev2 = person('ifd_revenu_activite_conjoint_2', period)

        # 50% of the lower income
        revenu_inferieur = min_(rev1, rev2)
        deduction_brute = revenu_inferieur * 0.5

        # Capped between min and max
        deduction = max_(min_(deduction_brute, p.deduction_dual_income_max),
                         where(marie * (revenu_inferieur > 0), p.deduction_dual_income_min, 0))

        return marie * deduction


# --- Art. 33 Abs. 3: Childcare deduction ---

class ifd_frais_garde_enfants(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Third-party childcare costs actually paid (CHF)"
    reference = "SR 642.11 Art. 33 Abs. 3"


class ifd_nombre_enfants_moins_14(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Number of children under 14 living in the same household"
    reference = "SR 642.11 Art. 33 Abs. 3"


class ifd_deduction_garde_enfants(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Deduction for third-party childcare costs (CHF)"
    reference = "SR 642.11 Art. 33 Abs. 3"

    def formula(person, period, parameters):
        frais = person('ifd_frais_garde_enfants', period)
        nb_enfants = person('ifd_nombre_enfants_moins_14', period)
        plafond_par_enfant = parameters(period).sr_642_11.deduction_childcare_max
        plafond_total = nb_enfants * plafond_par_enfant
        return min_(frais, plafond_total)
