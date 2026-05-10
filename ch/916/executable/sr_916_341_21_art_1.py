"""SR 916.341.21 Art. 1

Generated from: ch/916/fr/916.341.21.md

Pourcentage de viande maigre (PVM) — La charnure est déterminée par le PVM,
qui est le rapport entre le poids de tous les muscles rouges striés mesurables
après la coupe et le poids de la carcasse.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class poids_muscles_rouges_stries(Variable):
    value_type = float
    entity_key = 'animal'
    definition_period = MONTH
    label = "Poids de tous les muscles rouges striés mesurables après la coupe (kg)"
    reference = "SR 916.341.21 Art. 1 al. 2"


class poids_carcasse(Variable):
    value_type = float
    entity_key = 'animal'
    definition_period = MONTH
    label = "Poids de la carcasse (kg)"
    reference = "SR 916.341.21 Art. 1 al. 2"


class pourcentage_viande_maigre(Variable):
    value_type = float
    entity_key = 'animal'
    definition_period = MONTH
    label = "Pourcentage de viande maigre (PVM) — ratio muscles rouges / carcasse"
    reference = "SR 916.341.21 Art. 1"

    def formula_2000(animal, period, parameters):
        muscles = animal('poids_muscles_rouges_stries', period)
        carcasse = animal('poids_carcasse', period)

        return np.where(carcasse > 0, muscles / carcasse, 0.0)
