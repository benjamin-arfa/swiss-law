"""SR 842 Art. 30

Generated from: ch/fr/842.md

Art. 30: Duree de l'aide federale pour logements en propriete.

Abs. 1: L'aide federale est accordee pour 25 ans au maximum.

Abs. 2: L'aide peut prendre fin avant terme avec accord de l'office
si le pret est rembourse et la Confederation liberee comme arriere-caution.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class log_annee_debut_aide_propriete(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Annee de debut de l'aide federale pour logement en propriete"
    reference = "SR 842 Art. 30 al. 1"


class log_pret_propriete_rembourse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le pret pour logement en propriete est rembourse"
    reference = "SR 842 Art. 30 al. 2"


class log_confederation_liberee_caution(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La Confederation est liberee en tant qu'arriere-caution"
    reference = "SR 842 Art. 30 al. 2"


class log_duree_aide_propriete_restante(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Duree restante de l'aide federale pour logement en propriete (annees)"
    reference = "SR 842 Art. 30 al. 1"

    def formula(person, period, parameters):
        p = parameters(period)
        annee_debut = person('log_annee_debut_aide_propriete', period)
        duree_max = p.sr_842.art_30.duree_max_aide_propriete
        annee_courante = period.start.year
        annees_ecoulees = annee_courante - annee_debut
        return max_(duree_max - annees_ecoulees, 0)


class log_aide_propriete_en_cours(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'aide federale pour logement en propriete est encore en cours"
    reference = "SR 842 Art. 30"

    def formula(person, period, parameters):
        duree_restante = person('log_duree_aide_propriete_restante', period)
        rembourse = person('log_pret_propriete_rembourse', period)
        liberee = person('log_confederation_liberee_caution', period)
        # Fin anticipee si pret rembourse ET confederation liberee
        fin_anticipee = rembourse * liberee
        return (duree_restante > 0) * not_(fin_anticipee)
