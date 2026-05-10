"""SR 842 Art. 19

Generated from: ch/fr/842.md

Art. 19: Duree de l'aide federale pour logements locatifs.

Abs. 1: L'aide federale est accordee pour 25 ans au maximum.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class log_annee_debut_aide_locatif(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Annee de debut de l'aide federale pour logement locatif"
    reference = "SR 842 Art. 19 al. 1"


class log_duree_aide_locatif_restante(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Duree restante de l'aide federale pour logement locatif (annees)"
    reference = "SR 842 Art. 19 al. 1"

    def formula(person, period, parameters):
        p = parameters(period)
        annee_debut = person('log_annee_debut_aide_locatif', period)
        duree_max = p.sr_842.art_19.duree_max_aide_locatif
        annee_courante = period.start.year
        annees_ecoulees = annee_courante - annee_debut
        return max_(duree_max - annees_ecoulees, 0)


class log_aide_locatif_en_cours(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'aide federale pour logement locatif est encore en cours"
    reference = "SR 842 Art. 19 al. 1"

    def formula(person, period, parameters):
        duree_restante = person('log_duree_aide_locatif_restante', period)
        return duree_restante > 0
