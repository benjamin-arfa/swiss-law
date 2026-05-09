"""SR 641.81 Art. 19 - Verwendung der Abgabe (Revenue distribution)

Heavy Vehicle Tax Act (SVAG) - Distribution of net revenue.
Art. 19:
  Abs. 1: 1/3 to cantons, 2/3 to the federal government
  Abs. 2bis: Federal reserve of at least 300 million CHF in rail infrastructure fund

Generated from: ch/641/de/641.81.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_switzerland.entities import Person


class svag_reinertrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Net revenue from heavy vehicle tax in CHF (SR 641.81 Art. 19)"
    reference = "SR 641.81 Art. 19"
    default_value = 0.0


class svag_anteil_kantone(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Cantonal share of net revenue - 1/3 (SR 641.81 Art. 19 Abs. 1)"
    reference = "SR 641.81 Art. 19"

    def formula(person, period, parameters):
        reinertrag = person("svag_reinertrag", period)
        return reinertrag / 3.0


class svag_anteil_bund(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Federal share of net revenue - 2/3 (SR 641.81 Art. 19 Abs. 1)"
    reference = "SR 641.81 Art. 19"

    def formula(person, period, parameters):
        reinertrag = person("svag_reinertrag", period)
        return reinertrag * 2.0 / 3.0


class svag_bif_reserve_minimum(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Minimum reserve in rail infrastructure fund - 300 million CHF (SR 641.81 Art. 19 Abs. 2bis)"
    reference = "SR 641.81 Art. 19"
    default_value = 300000000.0
