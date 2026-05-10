"""SR 916.341.22 Art. 4

Generated from: ch/916/fr/916.341.22.md

Les cabris sont classés conformément au système d'estimation et de
classification prévu à l'annexe 4.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class animal_est_cabri(Variable):
    value_type = bool
    entity_key = 'animal'
    definition_period = MONTH
    label = "The animal is a kid (young goat / cabri)"
    reference = "SR 916.341.22 Art. 4"


class classification_cabri_annexe_4(Variable):
    value_type = bool
    entity_key = 'animal'
    definition_period = MONTH
    label = "Kid (cabri) is classified according to the Annex 4 system"
    reference = "SR 916.341.22 Art. 4"

    def formula_2000(animal, period, parameters):
        est_cabri = animal('animal_est_cabri', period)
        return est_cabri
