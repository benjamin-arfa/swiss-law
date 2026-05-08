"""SR 916.341.22 Art. 1

Generated from: ch/916/fr/916.341.22.md

Les animaux de l'espèce bovine sont classés conformément au système
d'estimation et de classification prévu à l'annexe 1.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class animal_espece_bovine(Variable):
    value_type = bool
    entity_key = 'animal'
    definition_period = MONTH
    label = "The animal is of the bovine species"
    reference = "SR 916.341.22 Art. 1"


class classification_bovine_annexe_1(Variable):
    value_type = bool
    entity_key = 'animal'
    definition_period = MONTH
    label = "Bovine animal is classified according to the Annex 1 system"
    reference = "SR 916.341.22 Art. 1"

    def formula_2000(animal, period, parameters):
        est_bovin = animal('animal_espece_bovine', period)
        return est_bovin
