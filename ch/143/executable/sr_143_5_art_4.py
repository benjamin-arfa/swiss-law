"""SR 143.5 Art. 4

Generated from: ch/143/fr/143.5.md

Passport for foreigners: right for those under Art. 59 al. 2 let. b and c LEI;
may be granted to those without travel documents but with residence permit,
asylum seekers, or provisionally admitted persons.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class odv_est_etranger_art59_al2_let_b_c(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Etranger au sens de l'art. 59 al. 2 let. b et c LEI"
    reference = "SR 143.5 Art. 4 al. 1"


class odv_depourvu_documents_voyage(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "La personne est depourvue de documents de voyage"
    reference = "SR 143.5 Art. 4 al. 2"


class odv_titulaire_autorisation_sejour(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Titulaire d'une autorisation de sejour ou carte de legitimation"
    reference = "SR 143.5 Art. 4 al. 2 let. a"


class odv_est_requerant_asile(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "La personne est requerant d'asile"
    reference = "SR 143.5 Art. 4 al. 2 let. b"


class odv_est_personne_admise_provisoirement(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "La personne est admise a titre provisoire"
    reference = "SR 143.5 Art. 4 al. 2 let. b"


class odv_droit_passeport_etranger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Droit a un passeport pour etrangers"
    reference = "SR 143.5 Art. 4 al. 1"

    def formula(person, period, parameters):
        return person('odv_est_etranger_art59_al2_let_b_c', period)


class odv_peut_beneficier_passeport_etranger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Peut beneficier d'un passeport pour etrangers (al. 2)"
    reference = "SR 143.5 Art. 4 al. 2"

    def formula(person, period, parameters):
        sans_docs = person('odv_depourvu_documents_voyage', period)
        sejour = person('odv_titulaire_autorisation_sejour', period)
        asile = person('odv_est_requerant_asile', period)
        provisoire = person('odv_est_personne_admise_provisoirement', period)
        return sans_docs * ((sejour + asile + provisoire) > 0)
