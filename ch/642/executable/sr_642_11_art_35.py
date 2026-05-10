"""SR 642.11 Art. 35

Generated from: ch/642/fr/642.11.md

Art. 35 Déductions sociales (Social deductions):
1. The following are deducted from income:
   a. CHF 6,800 per minor child or child in education/apprenticeship
      that the taxpayer supports; when parents are taxed separately,
      the deduction is split in half if they share parental authority
      and do not claim a maintenance deduction under Art. 33(1)(c).
   b. CHF 6,800 per person wholly or partially incapable of gainful
      employment whom the taxpayer supports, provided the support
      amounts to at least the deduction; not granted for spouse or
      children already covered under (a).
   c. CHF 2,800 for married couples living together.
2. Deductions are based on the taxpayer's situation at the end of the
   tax period.
3. In cases of partial tax liability, deductions are granted proportionally.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ifd_nombre_enfants(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Number of minor children or children in education/apprenticeship that the taxpayer supports"
    reference = "SR 642.11 Art. 35 Abs. 1 Bst. a"


class ifd_autorite_parentale_conjointe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the taxpayer shares parental authority with a separately-taxed parent"
    reference = "SR 642.11 Art. 35 Abs. 1 Bst. a"


class ifd_nombre_personnes_a_charge(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Number of dependent persons incapable of gainful employment that the taxpayer supports"
    reference = "SR 642.11 Art. 35 Abs. 1 Bst. b"


class ifd_marie_menage_commun(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the taxpayer is married and living in a common household"
    reference = "SR 642.11 Art. 35 Abs. 1 Bst. c"


class ifd_taux_assujettissement(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Proportion of tax liability (1.0 = full, <1.0 = partial)"
    reference = "SR 642.11 Art. 35 Abs. 3"
    default_value = 1.0


class ifd_deduction_enfants(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Total child deduction amount (CHF)"
    reference = "SR 642.11 Art. 35 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        nb_enfants = person('ifd_nombre_enfants', period)
        autorite_conjointe = person('ifd_autorite_parentale_conjointe', period)
        taux = person('ifd_taux_assujettissement', period)
        deduction_par_enfant = parameters(period).sr_642_11.deduction_child

        # Half deduction when shared parental authority with separately-taxed parent
        facteur = where(autorite_conjointe, 0.5, 1.0)
        return nb_enfants * deduction_par_enfant * facteur * taux


class ifd_deduction_personnes_a_charge(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Total deduction for dependent persons (CHF)"
    reference = "SR 642.11 Art. 35 Abs. 1 Bst. b"

    def formula(person, period, parameters):
        nb_personnes = person('ifd_nombre_personnes_a_charge', period)
        taux = person('ifd_taux_assujettissement', period)
        deduction = parameters(period).sr_642_11.deduction_dependent
        return nb_personnes * deduction * taux


class ifd_deduction_couple(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Deduction for married couples living together (CHF)"
    reference = "SR 642.11 Art. 35 Abs. 1 Bst. c"

    def formula(person, period, parameters):
        marie = person('ifd_marie_menage_commun', period)
        taux = person('ifd_taux_assujettissement', period)
        deduction = parameters(period).sr_642_11.deduction_married
        return marie * deduction * taux


class ifd_deductions_sociales(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Total social deductions under Art. 35 (CHF)"
    reference = "SR 642.11 Art. 35"

    def formula(person, period, parameters):
        enfants = person('ifd_deduction_enfants', period)
        personnes = person('ifd_deduction_personnes_a_charge', period)
        couple = person('ifd_deduction_couple', period)
        return enfants + personnes + couple
