"""SR 221.214.1 Art. 27

Generated from: ch/221/fr/221.214.1.md

Credit card reporting obligation: must report to information center when
consumer uses credit option 3 consecutive times; no obligation if
outstanding amount < 3000 CHF.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lcc_option_credit_utilisee_3_fois_consecutives(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Le consommateur a utilise l'option de credit 3 fois consecutives"
    reference = "SR 221.214.1 Art. 27 al. 1"


class lcc_montant_restant_a_payer_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Montant restant a payer sur la carte de credit en CHF"
    reference = "SR 221.214.1 Art. 27 al. 1"


class lcc_seuil_annonce_carte_credit_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Seuil en dessous duquel l'annonce au centre n'est pas obligatoire (3000 CHF)"
    reference = "SR 221.214.1 Art. 27 al. 1"

    def formula(person, period, parameters):
        return 3000.0


class lcc_obligation_annonce_carte_credit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Obligation d'annoncer au centre de renseignements (usage carte credit)"
    reference = "SR 221.214.1 Art. 27 al. 1"

    def formula(person, period, parameters):
        trois_fois = person('lcc_option_credit_utilisee_3_fois_consecutives', period)
        montant = person('lcc_montant_restant_a_payer_chf', period)
        return trois_fois * (montant >= 3000)
