"""SR 131.218 § 2

Generated from: ch/131/de/131.218.md

Popular sovereignty: Sovereignty rests in the entirety of the people.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class zuger_staatsangehoerigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person dem Zuger Staatsvolk angehört"
    reference = "SR 131.218 § 2"


class zuger_volkssouveraenitaet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Souveränität in der Gesamtheit des Zuger Volkes beruht"
    reference = "SR 131.218 § 2"

    def formula(person, period, parameters):
        return person('zuger_staatsangehoerigkeit', period)


class zuger_staatsmacht_vom_volk(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob alle Staatsgewalt vom Volk ausgeht"
    reference = "SR 131.218 § 2"

    def formula(person, period, parameters):
        return person('zuger_volkssouveraenitaet', period)