"""SR 441.1 Art. 22a

Generated from: ch/441/de/441.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class finanzhilfe_ausserhalb_sprachgebiet_gesamtkosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gesamtkosten für Massnahmen zur Förderung Rätoromanisch/Italienisch ausserhalb angestammter Sprachgebiete"
    reference = "SR 441.1, Art. 22a Abs. 3"


class finanzhilfe_ausserhalb_sprachgebiet_max_betrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximaler Betrag der Finanzhilfe ausserhalb Sprachgebiet (höchstens 75% der Gesamtkosten)"
    reference = "SR 441.1, Art. 22a Abs. 3"

    def formula(self, period, parameters):
        gesamtkosten = self.person('finanzhilfe_ausserhalb_sprachgebiet_gesamtkosten', period)
        return gesamtkosten * 0.75
