"""SR 822.114 Art. 8 - Fluchtwege (Escape routes)

ArGV 4 - Maximum escape route lengths.
Art. 8:
  Abs. 3: Single exit: max 35 m; multiple exits: max 50 m
  Abs. 5: Max distance from any point in room to nearest exit: 35 m;
          total escape route with corridor: max 50 m

Generated from: ch/822/de/822.114.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_switzerland.entities import Person


class argv4_anzahl_ausgaenge(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Number of exits/staircases available for escape (SR 822.114 Art. 8)"
    reference = "SR 822.114 Art. 8"
    default_value = 1


class argv4_max_fluchtweg_laenge(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximum permitted escape route length in meters (SR 822.114 Art. 8 Abs. 3)"
    reference = "SR 822.114 Art. 8"

    def formula(person, period, parameters):
        ausgaenge = person("argv4_anzahl_ausgaenge", period)
        # Single exit: max 35 m; multiple exits: max 50 m
        return where(ausgaenge >= 2, 50.0, 35.0)


class argv4_fluchtweg_laenge(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Actual escape route length in meters (SR 822.114 Art. 8)"
    reference = "SR 822.114 Art. 8"
    default_value = 0.0


class argv4_fluchtweg_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether escape route length meets requirements (SR 822.114 Art. 8)"
    reference = "SR 822.114 Art. 8"

    def formula(person, period, parameters):
        laenge = person("argv4_fluchtweg_laenge", period)
        max_laenge = person("argv4_max_fluchtweg_laenge", period)
        return laenge <= max_laenge


class argv4_max_entfernung_raumausgang(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximum distance from any point to nearest room exit - 35 m (SR 822.114 Art. 8 Abs. 5)"
    reference = "SR 822.114 Art. 8"
    default_value = 35.0
