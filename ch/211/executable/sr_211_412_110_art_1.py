"""SR 211.412.110 Art. 1

Generated from: ch/211/fr/211.412.110.md

Yield value calculation: capital whose interest (rent) corresponds to
multi-year average farm revenue. Calculation period 2009-2024,
average interest rate 4.24%.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class odfr_revenu_exploitation_annuel_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Revenu d'exploitation agricole annuel en CHF"
    reference = "SR 211.412.110 Art. 1 al. 2"


class odfr_part_revenu_capital(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Part du revenu du capital afferente au domaine rural (rente)"
    reference = "SR 211.412.110 Art. 1 al. 2"


class odfr_taux_interet_moyen_pourcent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Taux d'interet moyen pour le calcul de la valeur de rendement (4.24%)"
    reference = "SR 211.412.110 Art. 1 al. 3"

    def formula(person, period, parameters):
        return 4.24


class odfr_valeur_rendement_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Valeur de rendement de l'entreprise ou immeuble agricole en CHF"
    reference = "SR 211.412.110 Art. 1"

    def formula(person, period, parameters):
        rente = person('odfr_part_revenu_capital', period)
        taux = 4.24 / 100
        return where(taux > 0, rente / taux, 0)
