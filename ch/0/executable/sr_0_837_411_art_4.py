"""SR 0.837.411 Art. 4 - Conditions for benefit entitlement

Art. 4: Benefit eligibility may require:
a) Fitness and availability for work
b) Registration at a public employment office
c) Compliance with other national regulations

Generated from: ch/0/fr/0.837.411.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH
from openfisca_switzerland.entities import Person


class apte_au_travail(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is fit for work (Art. 4 let. a)"
    default_value = True


class disponible_pour_travail(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is available for work (Art. 4 let. a)"
    default_value = True


class inscrit_bureau_placement(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is registered at a public employment office (Art. 4 let. b)"
    default_value = False


class remplit_conditions_base_chomage(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person meets all basic conditions for unemployment benefit (Art. 4)"

    def formula(person, period, parameters):
        return (
            person("apte_au_travail", period)
            * person("disponible_pour_travail", period)
            * person("inscrit_bureau_placement", period)
        )
