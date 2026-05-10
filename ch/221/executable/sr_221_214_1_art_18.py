"""SR 221.214.1 Art. 18

Generated from: ch/221/fr/221.214.1.md

Default rules: lender can only terminate if arrears >= 10% of net credit;
leasing termination only if arrears > 3 monthly payments;
default interest cannot exceed contractual rate.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lcc_versements_en_suspens_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Montant des versements en suspens (arrieres) en CHF"
    reference = "SR 221.214.1 Art. 18 al. 1"


class lcc_montant_net_credit_ou_comptant_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Montant net du credit ou prix au comptant en CHF"
    reference = "SR 221.214.1 Art. 18 al. 1"


class lcc_redevance_mensuelle_leasing_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Montant de la redevance mensuelle de leasing en CHF"
    reference = "SR 221.214.1 Art. 18 al. 2"


class lcc_preteur_peut_resilier_credit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Le preteur peut resilier le contrat de credit (arrieres >= 10% du montant net)"
    reference = "SR 221.214.1 Art. 18 al. 1"

    def formula(person, period, parameters):
        arrieres = person('lcc_versements_en_suspens_chf', period)
        montant_net = person('lcc_montant_net_credit_ou_comptant_chf', period)
        return arrieres >= montant_net * 0.10


class lcc_donneur_peut_resilier_leasing(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Le donneur de leasing peut resilier (arrieres > 3 redevances mensuelles)"
    reference = "SR 221.214.1 Art. 18 al. 2"

    def formula(person, period, parameters):
        arrieres = person('lcc_versements_en_suspens_chf', period)
        redevance = person('lcc_redevance_mensuelle_leasing_chf', period)
        return arrieres > redevance * 3


class lcc_interet_moratoire_max_egal_taux_convenu(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'interet moratoire ne peut depasser le taux d'interet convenu"
    reference = "SR 221.214.1 Art. 18 al. 3"

    def formula(person, period, parameters):
        return True
