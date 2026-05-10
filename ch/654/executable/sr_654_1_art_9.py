"""SR 654.1 Art. 9 - Societe mere de substitution

Generated from: ch/654/de/654.1.md

Rules on designating a substitute parent entity (substituierende
Konzernobergesellschaft) for CbC reporting.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class est_societe_mere_substitution_suisse(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'entite constitutive residente de Suisse est designee comme societe mere de substitution"
    reference = "SR 654.1 Art. 9 al. 1"


class etat_residence_societe_mere_substitution_est_partenaire(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'Etat de residence de la societe mere de substitution est un Etat partenaire"
    reference = "SR 654.1 Art. 9 al. 2 let. a"


class pas_defaillance_systemique_etat_societe_mere_substitution(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Aucune defaillance systemique n'est survenue dans l'Etat de la societe mere de substitution"
    reference = "SR 654.1 Art. 9 al. 2 let. b"


class notification_societe_mere_substitution_recue(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'Etat de residence a recu la notification de la qualite de societe mere de substitution"
    reference = "SR 654.1 Art. 9 al. 2 let. c"


class societe_mere_substitution_etrangere_valide(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'entite constitutive etrangere peut etre designee comme societe mere de substitution"
    reference = "SR 654.1 Art. 9 al. 2"

    def formula(self, period, parameters):
        est_partenaire = self('etat_residence_societe_mere_substitution_est_partenaire', period)
        pas_defaillance = self('pas_defaillance_systemique_etat_societe_mere_substitution', period)
        notification = self('notification_societe_mere_substitution_recue', period)
        return est_partenaire * pas_defaillance * notification
