"""SR 441.11 Art. 23

Generated from: ch/441/de/441.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class finanzhilfe_org_ti_gesamtkosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gesamtkosten der italienischsprachigen Organisation oder Institution (Kanton Tessin)"
    reference = "SR 441.11, Art. 23 Abs. 3"


class finanzhilfe_org_ti_max_betrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximale Finanzhilfe für Organisationen TI (höchstens 90% der Gesamtkosten)"
    reference = "SR 441.11, Art. 23 Abs. 3"

    def formula(self, period, parameters):
        gesamtkosten = self.person('finanzhilfe_org_ti_gesamtkosten', period)
        return gesamtkosten * 0.90
