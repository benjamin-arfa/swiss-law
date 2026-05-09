"""SR 0.672.916.311 Art. 4 - Refund of Austrian capital yield tax

Art. 4: Swiss residents must request refund of Austrian capital yield tax
in writing using form R-CH R-A1.
- Par. 2: Request must be filed within 3 years after the end of the
  calendar year in which dividends/interest became due.
- Par. 3: Multiple claims in one year should be combined; up to 3 years
  can be combined in one request.

Generated from: ch/0/fr/0.672.916.311.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_switzerland.entities import Person


class annee_echeance_revenus_at(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Calendar year in which Austrian dividends/interest became due (Art. 4)"
    default_value = 0


class delai_demande_remboursement_at_ans(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Deadline for refund request: 3 years after year of payment (Art. 4 par. 2)"
    default_value = 3


class demande_remboursement_at_dans_delai(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Refund request for Austrian tax filed within 3-year deadline (Art. 4 par. 2)"

    def formula(person, period, parameters):
        annee_echeance = person("annee_echeance_revenus_at", period)
        annee_courante = period.start.year
        delai = person("delai_demande_remboursement_at_ans", period)
        return (annee_courante - annee_echeance) <= delai


class nombre_annees_regroupees_at(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Number of years grouped in one refund request - max 3 (Art. 4 par. 3)"
    default_value = 1

    def formula(person, period, parameters):
        # Claims for up to 3 years can be combined
        return min_(person("nombre_annees_regroupees_at", period), 3)
