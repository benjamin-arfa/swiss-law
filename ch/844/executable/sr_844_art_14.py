"""SR 844 Art. 14

Generated from: ch/fr/844.md

Art. 14: Prescription du droit au remboursement.

Abs. 1: Le droit au remboursement se prescrit par 3 ans des que
l'autorite cantonale en a eu connaissance, mais au plus tard par
10 ans des la naissance du droit.

Abs. 2: Si le fait resulte d'un acte punissable, l'action se prescrit
au plus tot a l'echeance de la prescription penale. Si un jugement
de premiere instance a ete rendu, l'action civile se prescrit au plus
tot par 3 ans apres notification du jugement.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lalm_date_connaissance_droit(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Annee ou l'autorite cantonale a eu connaissance du droit au remboursement"
    reference = "SR 844 Art. 14 al. 1"


class lalm_date_naissance_droit(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Annee de naissance du droit au remboursement"
    reference = "SR 844 Art. 14 al. 1"


class lalm_acte_punissable(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le fait donnant lieu au remboursement resulte d'un acte punissable"
    reference = "SR 844 Art. 14 al. 2"


class lalm_droit_remboursement_prescrit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le droit au remboursement est prescrit"
    reference = "SR 844 Art. 14 al. 1"

    def formula(person, period, parameters):
        p = parameters(period)
        annee_courante = period.start.year
        date_connaissance = person('lalm_date_connaissance_droit', period)
        date_naissance = person('lalm_date_naissance_droit', period)
        acte_punissable = person('lalm_acte_punissable', period)
        delai_relatif = p.sr_844.art_14.delai_prescription_relatif
        delai_absolu = p.sr_844.art_14.delai_prescription_absolu

        prescrit_relatif = (annee_courante - date_connaissance) > delai_relatif
        prescrit_absolu = (annee_courante - date_naissance) > delai_absolu

        # Prescription normale (non-punissable): relatif OU absolu
        prescrit_normal = prescrit_relatif + prescrit_absolu > 0

        # Si acte punissable, la prescription penale peut etre plus longue
        # (simplifie: on ne prescrit pas si acte punissable dans le delai absolu)
        return where(acte_punissable, prescrit_absolu, prescrit_normal)
