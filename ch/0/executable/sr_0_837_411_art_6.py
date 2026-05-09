"""SR 0.837.411 Art. 6 - Qualifying period (stage)

Art. 6: Benefit entitlement may be conditional on a qualifying period:
a) Payment of a set number of contributions in a defined period
b) Employment covered by the convention for a defined period
c) A combination of both

Generated from: ch/0/fr/0.837.411.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH
from openfisca_switzerland.entities import Person


class nombre_cotisations_versees(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Number of unemployment insurance contributions paid (Art. 6 let. a)"
    default_value = 0


class duree_emploi_couvert_mois(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Duration of covered employment in months (Art. 6 let. b)"
    default_value = 0


class stage_qualifiant_accompli(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person has completed the required qualifying period (Art. 6)"

    def formula(person, period, parameters):
        cotisations = person("nombre_cotisations_versees", period)
        duree_emploi = person("duree_emploi_couvert_mois", period)
        # Swiss law (RS 837.0) typically requires 12 months of contributions
        # in the 2 years preceding unemployment
        cotisations_min = 12
        return (cotisations >= cotisations_min) + (duree_emploi >= cotisations_min)
