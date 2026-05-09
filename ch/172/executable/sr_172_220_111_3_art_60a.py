"""SR 172.220.111.3 Art. 60a - Modification du taux d'occupation (Work Rate After Birth)

Generated from: ch/172/fr/172.220.111.3.md

After birth or adoption, parents/registered partners may:
- Reduce work rate by up to 20% (but not below 60%)
- Must exercise right within 12 months of birth/adoption
- Reduced work starts at latest on first day after 12-month deadline
- One-time right to increase back by same amount (up to 20%)
- Request to increase must be within 3 years of last reduction taking effect
  and at least 3 months before desired effective date
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class opers_taux_occupation_actuel(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Taux d'occupation actuel en pourcentage"
    reference = "SR 172.220.111.3 Art. 60a"


class opers_naissance_ou_adoption(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Naissance ou adoption d'un ou plusieurs enfants"
    reference = "SR 172.220.111.3 Art. 60a al. 1"


class opers_mois_depuis_naissance_adoption(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Nombre de mois ecoules depuis la naissance ou l'adoption"
    reference = "SR 172.220.111.3 Art. 60a al. 2"


class opers_reduction_taux_max_pourcent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Reduction maximale du taux d'occupation autorisee en points de pourcentage"
    reference = "SR 172.220.111.3 Art. 60a al. 1"

    def formula(person, period, parameters):
        naissance = person('opers_naissance_ou_adoption', period.this_year)
        mois = person('opers_mois_depuis_naissance_adoption', period)
        taux = person('opers_taux_occupation_actuel', period)

        # Right exists within 12 months of birth/adoption
        dans_delai = mois <= 12

        # Max 20% reduction but floor at 60%
        reduction_possible = max_(taux - 60, 0)
        reduction_max = min_(reduction_possible, 20)

        return where(naissance * dans_delai, reduction_max, 0)


class opers_taux_occupation_minimum(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Taux d'occupation minimum apres reduction (60%)"
    reference = "SR 172.220.111.3 Art. 60a al. 1"

    def formula(person, period, parameters):
        return where(person('opers_naissance_ou_adoption', period.this_year), 60.0, 0.0)
