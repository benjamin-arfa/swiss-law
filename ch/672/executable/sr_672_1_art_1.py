"""SR 672.1 Art. 1

Generated from: ch/672/fr/672.1.md

Reciprocal declarations on taxation of maritime, inland waterway
and air navigation enterprises.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


# --- Input variables ---

class entreprise_navigation_maritime_ou_aerienne(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'entreprise exploite la navigation maritime, interieure ou aerienne"
    reference = "SR 672.1 Art. 1 al. 1"


class etat_etranger_garantit_reciprocite(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'Etat etranger garantit la reciprocite"
    reference = "SR 672.1 Art. 1 al. 1"


class direction_effective_en_suisse(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La direction effective de l'entreprise se trouve en Suisse"
    reference = "SR 672.1 Art. 1 al. 2"


class vehicules_immatricules_en_suisse(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Les vehicules sont immatricules en Suisse"
    reference = "SR 672.1 Art. 1 al. 2"


class participe_pool_exploitation_commune(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'entreprise participe a un pool ou exploitation en commun"
    reference = "SR 672.1 Art. 1 al. 3"


# --- Computed variables ---

class imposition_exclusive_un_seul_etat(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Un seul Etat a le droit d'imposer les recettes et benefices de navigation"
    reference = "SR 672.1 Art. 1 al. 1"

    def formula(self, period, parameters):
        navigation = self('entreprise_navigation_maritime_ou_aerienne', period)
        reciprocite = self('etat_etranger_garantit_reciprocite', period)
        return navigation * reciprocite


class competence_imposition_suisse(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La Suisse a la competence exclusive d'imposition"
    reference = "SR 672.1 Art. 1 al. 2"

    def formula(self, period, parameters):
        exclusif = self('imposition_exclusive_un_seul_etat', period)
        direction = self('direction_effective_en_suisse', period)
        immatriculation = self('vehicules_immatricules_en_suisse', period)
        return exclusif * (direction + immatriculation > 0)
