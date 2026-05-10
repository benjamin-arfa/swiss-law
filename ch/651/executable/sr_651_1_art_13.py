"""SR 651.1 Art. 13 - Mesures de contrainte

Generated from: ch/651/fr/651.1.md

Coercive measures: conditions, types, and authorization requirements.
Must be ordered by the FTA director or authorized representative.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class droit_suisse_prevoit_mesure_contrainte(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Le droit suisse prevoit l'execution de mesures de contrainte"
    reference = "SR 651.1 Art. 13 al. 1 let. a"


class remise_renseignements_art_8_al_2_exigee(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La remise de renseignements au sens de l'art. 8 al. 2 est exigee"
    reference = "SR 651.1 Art. 13 al. 1 let. b"


class mesure_ordonnee_par_directeur_afc(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La mesure de contrainte est ordonnee par le directeur de l'AFC ou son representant"
    reference = "SR 651.1 Art. 13 al. 3"


class peril_en_la_demeure(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Il y a peril en la demeure"
    reference = "SR 651.1 Art. 13 al. 4"


class delai_approbation_jours(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Delai d'approbation d'une mesure de contrainte urgente (jours ouvrables)"
    reference = "SR 651.1 Art. 13 al. 4"
    default_value = 3


class mesure_contrainte_autorisee(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Les mesures de contrainte peuvent etre ordonnees"
    reference = "SR 651.1 Art. 13 al. 1"

    def formula(self, period, parameters):
        droit_suisse = self('droit_suisse_prevoit_mesure_contrainte', period)
        art_8_al_2 = self('remise_renseignements_art_8_al_2_exigee', period)
        directeur = self('mesure_ordonnee_par_directeur_afc', period)
        peril = self('peril_en_la_demeure', period)

        # al. 1: conditions (a OR b)
        condition = droit_suisse + art_8_al_2 > 0
        # al. 3: must be ordered by director (or al. 4: urgent exception)
        autorisation = directeur + peril > 0
        return condition * autorisation
