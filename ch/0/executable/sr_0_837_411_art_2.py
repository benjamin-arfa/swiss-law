"""SR 0.837.411 Art. 2 - Scope of application

Art. 2: Convention applies to all persons habitually employed for wages.
Exceptions may be made for domestic workers, homeworkers, government employees,
high-income non-manual workers, seasonal workers (<6 months), young/old workers, etc.
Does not apply to seamen, fishermen, or agricultural workers.

Generated from: ch/0/fr/0.837.411.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class est_employe_salarie(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is habitually employed for wages (Art. 2 par. 1)"


class est_gens_de_maison(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is a domestic worker (Art. 2 par. 2 let. a)"
    default_value = False


class est_travailleur_a_domicile(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is a homeworker (Art. 2 par. 2 let. b)"
    default_value = False


class est_employe_gouvernement_stable(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person holds stable government/public utility employment (Art. 2 par. 2 let. c)"
    default_value = False


class est_travailleur_saisonnier_court(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is a seasonal worker with season < 6 months (Art. 2 par. 2 let. e)"
    default_value = False


class est_marin_ou_pecheur(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is a seaman or fisherman (Art. 2 par. 4)"
    default_value = False


class est_travailleur_agricole(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is an agricultural worker (Art. 2 par. 4)"
    default_value = False


class couvert_convention_chomage(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is covered by the unemployment convention (Art. 2)"

    def formula(person, period, parameters):
        est_salarie = person("est_employe_salarie", period)

        # Exclusions from Art. 2 par. 2
        exclusion_domestique = person("est_gens_de_maison", period)
        exclusion_domicile = person("est_travailleur_a_domicile", period)
        exclusion_gouvernement = person("est_employe_gouvernement_stable", period)
        exclusion_saisonnier = person("est_travailleur_saisonnier_court", period)

        # Absolute exclusions from Art. 2 par. 4
        exclusion_marin = person("est_marin_ou_pecheur", period)
        exclusion_agricole = person("est_travailleur_agricole", period)

        return (
            est_salarie
            * not_(exclusion_domestique)
            * not_(exclusion_domicile)
            * not_(exclusion_gouvernement)
            * not_(exclusion_saisonnier)
            * not_(exclusion_marin)
            * not_(exclusion_agricole)
        )
