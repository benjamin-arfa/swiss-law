"""SR 822.114 Art. 5 - Raumhöhe (Room height requirements)

ArGV 4 - Minimum room heights for workplaces based on floor area.
Art. 5 Abs. 1:
  a) Floor area <= 100 m2: min 2.75 m
  b) Floor area <= 250 m2: min 3.00 m
  c) Floor area <= 400 m2: min 3.50 m
  d) Floor area >  400 m2: min 4.00 m

Generated from: ch/822/de/822.114.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_switzerland.entities import Person


class argv4_bodenflaeche(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Floor area of the workspace in m2 (SR 822.114 Art. 5)"
    reference = "SR 822.114 Art. 5"
    default_value = 0.0


class argv4_min_raumhoehe(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Minimum required room height in meters (SR 822.114 Art. 5 Abs. 1)"
    reference = "SR 822.114 Art. 5"

    def formula(person, period, parameters):
        flaeche = person("argv4_bodenflaeche", period)
        return (
            where(flaeche <= 100.0, 2.75,
            where(flaeche <= 250.0, 3.00,
            where(flaeche <= 400.0, 3.50,
            4.00)))
        )


class argv4_raumhoehe_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether actual room height meets the minimum requirement (SR 822.114 Art. 5)"
    reference = "SR 822.114 Art. 5"

    def formula(person, period, parameters):
        tatsaechlich = person("argv4_tatsaechliche_raumhoehe", period)
        minimum = person("argv4_min_raumhoehe", period)
        return tatsaechlich >= minimum


class argv4_tatsaechliche_raumhoehe(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Actual clear room height in meters (SR 822.114 Art. 5)"
    reference = "SR 822.114 Art. 5"
    default_value = 0.0
