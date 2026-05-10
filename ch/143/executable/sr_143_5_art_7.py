"""SR 143.5 Art. 7

Generated from: ch/143/fr/143.5.md

Return visa: persons to be protected and provisionally admitted persons
with valid travel document from their state of origin must obtain a return visa
to travel abroad. Exception for those with Art. 4 al. 2 let. b passport.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class odv_est_personne_a_proteger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "La personne est une personne a proteger"
    reference = "SR 143.5 Art. 7 al. 1"


class odv_dispose_document_voyage_valable_etat_origine(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Dispose d'un document de voyage valable emis par l'etat d'origine reconnu par la Suisse"
    reference = "SR 143.5 Art. 7 al. 1"


class odv_a_passeport_etranger_art4_al2_b(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Titulaire d'un passeport pour etrangers selon art. 4 al. 2 let. b"
    reference = "SR 143.5 Art. 7 al. 3"


class odv_visa_retour_obligatoire(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Obligation d'obtenir un visa de retour pour voyager a l'etranger"
    reference = "SR 143.5 Art. 7 al. 1"

    def formula(person, period, parameters):
        proteger = person('odv_est_personne_a_proteger', period)
        provisoire = person('odv_est_personne_admise_provisoirement', period)
        doc_valable = person('odv_dispose_document_voyage_valable_etat_origine', period)
        passeport_art4 = person('odv_a_passeport_etranger_art4_al2_b', period)
        return (proteger + provisoire) * doc_valable * not_(passeport_art4) > 0
