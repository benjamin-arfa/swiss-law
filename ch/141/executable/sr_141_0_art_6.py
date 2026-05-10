"""SR 141.0 Art. 6 - Verlust durch Adoption

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class minderjaehriges_schweizer_kind(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person ist ein minderjaehriges Kind mit Schweizer Buergerrecht"
    reference = "SR 141.0 Art. 6 Abs. 1"


class adoptiert_von_auslaender(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Kind wird von einer Auslaenderin oder einem Auslaender adoptiert"
    reference = "SR 141.0 Art. 6 Abs. 1"


class erwirbt_oder_besitzt_staatsangehoerigkeit_des_adoptierenden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Kind erwirbt die Staatsangehoerigkeit des Adoptierenden oder besitzt diese bereits"
    reference = "SR 141.0 Art. 6 Abs. 1"


class kindesverhaeltnis_zu_schweizer_elternteil_besteht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ein Kindesverhaeltnis zu einem schweizerischen Elternteil wird begruendet oder besteht nach Adoption weiter"
    reference = "SR 141.0 Art. 6 Abs. 2"


class adoption_aufgehoben(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Adoption wurde aufgehoben"
    reference = "SR 141.0 Art. 6 Abs. 3"


class verlust_buergerrecht_durch_adoption(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verlust des Schweizer Buergerrechts durch Adoption durch Auslaender"
    reference = "SR 141.0 Art. 6"

    def formula(self, period, parameters):
        schweizer_kind = self('minderjaehriges_schweizer_kind', period)
        von_auslaender = self('adoptiert_von_auslaender', period)
        erwirbt_staat = self('erwirbt_oder_besitzt_staatsangehoerigkeit_des_adoptierenden', period)
        ch_elternteil = self('kindesverhaeltnis_zu_schweizer_elternteil_besteht', period)
        aufgehoben = self('adoption_aufgehoben', period)

        # Grundregel: Verlust wenn adoptiert und fremde Staatsangehoerigkeit
        grundregel = schweizer_kind * von_auslaender * erwirbt_staat

        # Ausnahme Abs. 2: Kein Verlust wenn CH-Elternteil besteht
        # Ausnahme Abs. 3: Kein Verlust wenn Adoption aufgehoben
        ausnahmen = ch_elternteil + aufgehoben > 0

        return grundregel * not_(ausnahmen)
