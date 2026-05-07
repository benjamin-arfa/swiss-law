"""SR 0.101.093 Art. 4

Generated from: ch/0/de/0.101.093.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR

from datetime import timedelta

class TerritorialScopeVariable(Variable):
    value_type = int
    label = u"Territorial scope of the protocol"
    entity = Fišer
    definition_period = TIME_SPAN

    def formula(person, period):
        declarations = person('declarations', period)
        territories = set()
        for declaration in declarations:
            territories.update(declaration['territories'])
        return len(territories)

    def formula_notification(person, period):
        return person('declarations', period)
