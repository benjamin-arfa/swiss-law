"""SR 836.21 Art. 8 - Purchasing power adjustment for children abroad

Art. 8: Family allowances for children domiciled abroad are adjusted
for purchasing power in the child's country of residence:
(a) > 2/3 of Swiss PPP -> 100% of statutory minimum
(b) > 1/3 but <= 2/3 of Swiss PPP -> 2/3 of statutory minimum
(c) <= 1/3 of Swiss PPP -> 1/3 of statutory minimum

The assignment of countries to groups is based on World Bank PPP GNI
per capita data, reviewed every 3 years.

Generated from: ch/836/de/836.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH
from openfisca_switzerland.entities import Person


class kaufkraft_wohnsitzstaat_anteil(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Purchasing power ratio of child's country of residence relative to Switzerland (Art. 8 FamZV)"
    default_value = 1.0


class gesetzlicher_mindestbetrag_famz(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Statutory minimum family allowance amount (Art. 8 FamZV)"
    default_value = 200


class familienzulage_kaufkraftbereinigt(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Purchasing-power-adjusted family allowance for children abroad (Art. 8 FamZV)"

    def formula(person, period, parameters):
        kaufkraft = person("kaufkraft_wohnsitzstaat_anteil", period)
        mindestbetrag = person("gesetzlicher_mindestbetrag_famz", period)

        # (a) > 2/3 -> 100%
        # (b) > 1/3 and <= 2/3 -> 66.67%
        # (c) <= 1/3 -> 33.33%
        anteil = where(
            kaufkraft > 2 / 3,
            1.0,
            where(
                kaufkraft > 1 / 3,
                2 / 3,
                1 / 3,
            ),
        )
        return mindestbetrag * anteil
