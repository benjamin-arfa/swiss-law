"""SR 916.341.22 Art. 2

Generated from: ch/916/fr/916.341.22.md

Les animaux de l'espèce chevaline sont classés conformément au système
d'estimation et de classification prévu à l'annexe 2.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class animal_espece_chevaline(Variable):
    value_type = bool
    entity_key = 'animal'
    definition_period = MONTH
    label = "The animal is of the equine species"
    reference = "SR 916.341.22 Art. 2"


class classification_chevaline_annexe_2(Variable):
    value_type = bool
    entity_key = 'animal'
    definition_period = MONTH
    label = "Equine animal is classified according to the Annex 2 system"
    reference = "SR 916.341.22 Art. 2"

    def formula_2000(animal, period, parameters):
        est_chevalin = animal('animal_espece_chevaline', period)
        return est_chevalin
