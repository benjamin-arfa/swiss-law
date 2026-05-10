"""SR 441.1 Art. 21

Generated from: ch/441/de/441.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_mehrsprachiger_kanton(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist ein mehrsprachiger Kanton (BE, FR, GR, VS)"
    reference = "SR 441.1, Art. 21 Abs. 2"

    def formula(self, period, parameters):
        kanton = self.person('kanton_code', period)
        # Mehrsprachige Kantone: Bern, Freiburg, Graubünden, Wallis
        return (kanton == 'BE') + (kanton == 'FR') + (kanton == 'GR') + (kanton == 'VS')


class kanton_code(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Kantonscode (z.B. BE, FR, GR, VS)"
    reference = "SR 441.1, Art. 21 Abs. 2"


class finanzhilfe_mehrsprachiger_kanton(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anspruch auf Finanzhilfen für besondere Aufgaben mehrsprachiger Kantone"
    reference = "SR 441.1, Art. 21 Abs. 1"

    def formula(self, period, parameters):
        return self.person('ist_mehrsprachiger_kanton', period)
