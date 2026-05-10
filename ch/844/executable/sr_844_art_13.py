"""SR 844 Art. 13

Generated from: ch/fr/844.md

Art. 13: Remboursement des prestations.

Abs. 2: Dans les 20 ans apres le versement des subventions (ou versement final),
si l'objet est detourne de sa destination ou l'immeuble aliene avec benefice,
les prestations doivent etre remboursees en tout ou partie.

Abs. 4: Un transfert de propriete ne peut etre inscrit au registre foncier
dans les 20 ans sans declaration de l'autorite cantonale et federale.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lalm_date_versement_final(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Annee du versement final des subventions"
    reference = "SR 844 Art. 13 al. 2"


class lalm_detournement_destination(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'objet subventionne est detourne de sa destination premiere"
    reference = "SR 844 Art. 13 al. 2"


class lalm_alienation_avec_benefice(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'immeuble subventionne est aliene avec benefice"
    reference = "SR 844 Art. 13 al. 2"


class lalm_dans_delai_protection(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'operation a lieu dans le delai de protection de 20 ans"
    reference = "SR 844 Art. 13 al. 2"

    def formula(person, period, parameters):
        p = parameters(period)
        annee_versement = person('lalm_date_versement_final', period)
        delai = p.sr_844.art_13.delai_protection_ans
        annee_courante = period.start.year
        return (annee_courante - annee_versement) <= delai


class lalm_obligation_remboursement(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Obligation de rembourser les prestations federales"
    reference = "SR 844 Art. 13 al. 2"

    def formula(person, period, parameters):
        dans_delai = person('lalm_dans_delai_protection', period)
        detournement = person('lalm_detournement_destination', period)
        alienation = person('lalm_alienation_avec_benefice', period)
        return dans_delai * (detournement + alienation > 0)


class lalm_transfert_propriete_autorise(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Transfert de propriete autorise (hors delai ou avec declaration)"
    reference = "SR 844 Art. 13 al. 4"

    def formula(person, period, parameters):
        dans_delai = person('lalm_dans_delai_protection', period)
        # Hors delai = toujours autorise; dans delai = necessite declaration
        return not_(dans_delai)
