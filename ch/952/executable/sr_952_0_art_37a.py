"""SR 952.0 Art. 37a - Depots privilegies (Privileged Deposits)

Generated from: ch/952/fr/952.0.md

Privileged deposits in bank bankruptcy:
- Deposits in the name of the depositor (including custody bonds) are attributed
  to the 2nd class (LP Art. 219 al. 4), up to a maximum of CHF 100,000 per creditor
- Deposits with unauthorized institutions have NO privilege
- A claim is only privileged once, even if it has multiple holders
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


MONTANT_MAXIMAL_DEPOT_PRIVILEGIE = 100000  # CHF


class lb_montant_depot(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Montant du depot aupres de la banque (en francs)"
    reference = "SR 952.0 Art. 37a al. 1"


class lb_depot_au_nom_deposant(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le depot est libelle au nom du deposant"
    reference = "SR 952.0 Art. 37a al. 1"


class lb_banque_autorisee(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La banque a recu l'autorisation de la FINMA"
    reference = "SR 952.0 Art. 37a al. 3"


class lb_montant_depot_privilegie(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Montant du depot privilegie de 2eme classe (max 100'000 CHF)"
    reference = "SR 952.0 Art. 37a al. 1"

    def formula(person, period, parameters):
        montant = person('lb_montant_depot', period)
        au_nom = person('lb_depot_au_nom_deposant', period)
        autorisee = person('lb_banque_autorisee', period)

        # Pas de privilege si banque non autorisee ou depot pas au nom du deposant
        eligible = au_nom * autorisee

        # Plafond a 100'000 CHF par creancier
        montant_plafonne = min_(montant, MONTANT_MAXIMAL_DEPOT_PRIVILEGIE)

        return eligible * montant_plafonne


class lb_montant_depot_non_privilegie(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Montant du depot non privilegie (3eme classe, au-dela de 100'000 CHF)"
    reference = "SR 952.0 Art. 37a"

    def formula(person, period, parameters):
        montant = person('lb_montant_depot', period)
        privilegie = person('lb_montant_depot_privilegie', period)
        return max_(montant - privilegie, 0)
