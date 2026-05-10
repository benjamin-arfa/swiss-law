"""SR 822.114 Art. 7 - Treppenanlagen und Ausgänge (Staircases and exits)

ArGV 4 - Requirements for escape route staircases.
Art. 7 Abs. 2:
  a) Floor area <= 900 m2: at least 1 staircase or direct exit
  b) Floor area >  900 m2: at least 2 staircases

Generated from: ch/822/de/822.114.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class argv4_geschossflaeche(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Floor area per storey in m2 (SR 822.114 Art. 7)"
    reference = "SR 822.114 Art. 7"
    default_value = 0.0


class argv4_min_treppenanlagen(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Minimum number of staircases required (SR 822.114 Art. 7 Abs. 2)"
    reference = "SR 822.114 Art. 7"

    def formula(person, period, parameters):
        flaeche = person("argv4_geschossflaeche", period)
        return where(flaeche <= 900.0, 1, 2)


class argv4_treppenanlagen_vorhanden(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Number of available staircases or direct exits (SR 822.114 Art. 7)"
    reference = "SR 822.114 Art. 7"
    default_value = 0


class argv4_treppenanlagen_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the number of staircases meets requirements (SR 822.114 Art. 7)"
    reference = "SR 822.114 Art. 7"

    def formula(person, period, parameters):
        vorhanden = person("argv4_treppenanlagen_vorhanden", period)
        minimum = person("argv4_min_treppenanlagen", period)
        return vorhanden >= minimum
