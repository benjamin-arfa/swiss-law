"""SR 221.214.1 Art. 17

Generated from: ch/221/fr/221.214.1.md

Early repayment: consumer right to prepay; leasing minimum 30-day notice
to end of contract quarter.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lcc_remboursement_anticipe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Le consommateur effectue un remboursement anticipe du credit"
    reference = "SR 221.214.1 Art. 17 al. 1"


class lcc_droit_remise_interets(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Droit a la remise des interets et reduction des frais pour duree non utilisee"
    reference = "SR 221.214.1 Art. 17 al. 2"

    def formula(person, period, parameters):
        return person('lcc_remboursement_anticipe', period)


class lcc_est_contrat_leasing(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Le contrat est un contrat de leasing"
    reference = "SR 221.214.1 Art. 17 al. 3"


class lcc_leasing_delai_resiliation_jours(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Delai minimum de resiliation pour le leasing en jours"
    reference = "SR 221.214.1 Art. 17 al. 3"

    def formula(person, period, parameters):
        return 30
