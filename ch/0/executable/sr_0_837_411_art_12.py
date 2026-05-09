"""SR 0.837.411 Art. 12 - Means testing

Art. 12:
- Par. 1: Indemnity payments must NOT be subject to a means test.
- Par. 2: Allowance payments MAY be subject to a means test.

Generated from: ch/0/fr/0.837.411.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH
from openfisca_switzerland.entities import Person


class etat_de_besoin(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is in a state of financial need (Art. 12 par. 2)"
    default_value = False


class indemnite_exige_etat_besoin(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Indemnity requires means test - always False per Art. 12 par. 1"

    def formula(person, period, parameters):
        # Art. 12 par. 1: Indemnity payments must NOT be means-tested
        return person("chomage_involontaire", period) * 0


class allocation_exige_etat_besoin(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Allowance may require means test (Art. 12 par. 2)"

    def formula(person, period, parameters):
        # Art. 12 par. 2: Allowance MAY be subject to means test
        return person("etat_de_besoin", period)
