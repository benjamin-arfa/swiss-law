"""SR 901.022 Art. 19

Generated from: ch/901/fr/901.022.md

Art. 19: Revocation de l'allegement fiscal.

Abs. 4: Le DEFR ne peut revoquer sa decision que pendant une periode
correspondant a la duree de l'allegement + la moitie de cette duree
(= 1.5x la duree).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class rpol_duree_allegement_accorde(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Duree de l'allegement fiscal accorde (annees)"
    reference = "SR 901.022 Art. 19 al. 4"


class rpol_annee_debut_allegement(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Annee de debut de l'allegement fiscal"
    reference = "SR 901.022 Art. 19 al. 4"


class rpol_delai_revocation(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Duree pendant laquelle la revocation est possible (annees)"
    reference = "SR 901.022 Art. 19 al. 4"

    def formula(person, period, parameters):
        p = parameters(period)
        duree = person('rpol_duree_allegement_accorde', period)
        facteur = p.sr_901_022.art_19.facteur_delai_revocation
        # duree + moitie = 1.5 * duree, arrondi a l'entier superieur
        return (duree * facteur).astype(int) + 1


class rpol_revocation_possible(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La revocation de l'allegement est encore possible"
    reference = "SR 901.022 Art. 19 al. 4"

    def formula(person, period, parameters):
        annee_debut = person('rpol_annee_debut_allegement', period)
        delai = person('rpol_delai_revocation', period)
        annee_courante = period.start.year
        return (annee_courante - annee_debut) <= delai
