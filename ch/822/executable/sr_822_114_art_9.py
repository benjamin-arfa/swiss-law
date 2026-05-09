"""SR 822.114 Art. 9 - Ausführung von Treppenanlagen und Korridoren

ArGV 4 - Staircase and corridor dimensions.
Art. 9:
  Abs. 1: Min clear width of stairs and corridors: 1.20 m
  Abs. 2: Min clear width of technical stairs/platforms: 0.80 m

Generated from: ch/822/de/822.114.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_switzerland.entities import Person


class argv4_ist_technische_treppe(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the staircase serves technical installations only (SR 822.114 Art. 9 Abs. 2)"
    reference = "SR 822.114 Art. 9"
    default_value = False


class argv4_min_treppe_breite(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Minimum clear width of stairs and corridors in meters (SR 822.114 Art. 9)"
    reference = "SR 822.114 Art. 9"

    def formula(person, period, parameters):
        ist_technisch = person("argv4_ist_technische_treppe", period)
        # Technical stairs: min 0.80 m; regular stairs: min 1.20 m
        return where(ist_technisch, 0.80, 1.20)
