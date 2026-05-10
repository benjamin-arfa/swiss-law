"""SR 441.1 Art. 22

Generated from: ch/441/de/441.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class finanzhilfe_gr_ti_gesamtkosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gesamtkosten der Massnahme zur Erhaltung/Förderung Rätoromanisch/Italienisch"
    reference = "SR 441.1, Art. 22 Abs. 3"


class finanzhilfe_gr_ti_max_anteil(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximaler Anteil der Bundesfinanzhilfe (höchstens 75% der Gesamtkosten)"
    reference = "SR 441.1, Art. 22 Abs. 3"

    def formula(self, period, parameters):
        return 0.75


class finanzhilfe_gr_ti_max_betrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximaler Betrag der Finanzhilfe für GR/TI (75% der Gesamtkosten)"
    reference = "SR 441.1, Art. 22 Abs. 3"

    def formula(self, period, parameters):
        gesamtkosten = self.person('finanzhilfe_gr_ti_gesamtkosten', period)
        max_anteil = self.person('finanzhilfe_gr_ti_max_anteil', period)
        return gesamtkosten * max_anteil


class ist_kanton_gr_oder_ti(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Kanton Graubünden oder Tessin"
    reference = "SR 441.1, Art. 22 Abs. 1"

    def formula(self, period, parameters):
        kanton = self.person('kanton_code', period)
        return (kanton == 'GR') + (kanton == 'TI')


class berechtigung_finanzhilfe_art_22(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Berechtigung auf Finanzhilfe nach Art. 22 SpG (Kantone GR und TI)"
    reference = "SR 441.1, Art. 22 Abs. 1"

    def formula(self, period, parameters):
        return self.person('ist_kanton_gr_oder_ti', period)
