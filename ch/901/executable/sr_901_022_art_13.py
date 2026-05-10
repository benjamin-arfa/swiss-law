"""SR 901.022 Art. 13

Generated from: ch/901/fr/901.022.md

Art. 13: Proposition du canton.

Abs. 3: Le canton doit deposer sa proposition au SECO au plus tard
270 jours civils apres le debut de l'imposition fiscale.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class rpol_date_debut_imposition(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Date de debut de l'imposition fiscale (jour julien)"
    reference = "SR 901.022 Art. 13 al. 3"


class rpol_date_depot_proposition(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Date de depot de la proposition du canton (jour julien)"
    reference = "SR 901.022 Art. 13 al. 3"


class rpol_proposition_dans_delai(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La proposition du canton est deposee dans le delai de 270 jours"
    reference = "SR 901.022 Art. 13 al. 3"

    def formula(person, period, parameters):
        p = parameters(period)
        date_debut = person('rpol_date_debut_imposition', period)
        date_depot = person('rpol_date_depot_proposition', period)
        delai = p.sr_901_022.art_13.delai_depot_jours
        return (date_depot - date_debut) <= delai
