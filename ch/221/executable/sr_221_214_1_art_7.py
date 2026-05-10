"""SR 221.214.1 Art. 7

Generated from: ch/221/fr/221.214.1.md

Consumer credit exclusions: credit amount thresholds (< 500 CHF or > 80,000 CHF),
repayment deadline (3 months max for interest-free), mortgage-backed exclusion.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class lcc_montant_net_credit_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Montant net du credit a la consommation en CHF"
    reference = "SR 221.214.1 Art. 7 al. 1 let. e"


class lcc_credit_garanti_par_gage_immobilier(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Credit garanti directement ou indirectement par des gages immobiliers"
    reference = "SR 221.214.1 Art. 7 al. 1 let. a"


class lcc_credit_couvert_par_garantie_bancaire(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Credit couvert par une garantie bancaire usuelle ou avoirs deposes"
    reference = "SR 221.214.1 Art. 7 al. 1 let. b"


class lcc_credit_sans_interets_ni_frais(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Credit accorde sans remuneration en interets ni autres charges"
    reference = "SR 221.214.1 Art. 7 al. 1 let. c"


class lcc_delai_remboursement_mois(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Delai de remboursement du credit en mois"
    reference = "SR 221.214.1 Art. 7 al. 1 let. f"


class lcc_credit_exclu_par_montant(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Credit exclu du champ d'application en raison du montant (< 500 ou > 80000 CHF)"
    reference = "SR 221.214.1 Art. 7 al. 1 let. e"

    def formula(person, period, parameters):
        montant = person('lcc_montant_net_credit_chf', period)
        return (montant < 500) + (montant > 80000) > 0


class lcc_credit_exclu_par_delai_court(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Credit exclu car remboursement dans un delai de 3 mois maximum"
    reference = "SR 221.214.1 Art. 7 al. 1 let. f"

    def formula(person, period, parameters):
        return person('lcc_delai_remboursement_mois', period) <= 3


class lcc_credit_exclu_du_champ_application(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Credit exclu du champ d'application de la LCC"
    reference = "SR 221.214.1 Art. 7"

    def formula(person, period, parameters):
        gage = person('lcc_credit_garanti_par_gage_immobilier', period)
        garantie = person('lcc_credit_couvert_par_garantie_bancaire', period)
        sans_interets = person('lcc_credit_sans_interets_ni_frais', period)
        exclu_montant = person('lcc_credit_exclu_par_montant', period)
        exclu_delai = person('lcc_credit_exclu_par_delai_court', period)
        return (gage + garantie + sans_interets + exclu_montant + exclu_delai) > 0
