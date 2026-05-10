"""SR 916.341.22 Art. 3

Generated from: ch/916/fr/916.341.22.md

Les animaux de l'espèce ovine sont classés conformément au système
d'estimation et de classification prévu à l'annexe 3.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class animal_espece_ovine(Variable):
    value_type = bool
    entity_key = 'animal'
    definition_period = MONTH
    label = "The animal is of the ovine species"
    reference = "SR 916.341.22 Art. 3"


class classification_ovine_annexe_3(Variable):
    value_type = bool
    entity_key = 'animal'
    definition_period = MONTH
    label = "Ovine animal is classified according to the Annex 3 system"
    reference = "SR 916.341.22 Art. 3"

    def formula_2000(animal, period, parameters):
        est_ovin = animal('animal_espece_ovine', period)
        return est_ovin
