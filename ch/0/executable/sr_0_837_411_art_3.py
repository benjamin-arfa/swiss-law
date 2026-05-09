"""SR 0.837.411 Art. 3 - Partial unemployment

Art. 3: In case of partial unemployment, indemnities or allowances must
be granted to workers whose employment is reduced.

Generated from: ch/0/fr/0.837.411.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH
from openfisca_switzerland.entities import Person


class chomage_partiel(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is in partial unemployment - reduced employment (Art. 3)"
    default_value = False


class droit_indemnite_chomage_partiel(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Right to partial unemployment benefit (Art. 3)"

    def formula(person, period, parameters):
        return (
            person("chomage_partiel", period)
            * person("couvert_convention_chomage", period)
        )
