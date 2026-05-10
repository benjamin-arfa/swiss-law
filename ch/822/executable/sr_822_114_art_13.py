"""SR 822.114 Art. 13 - Gleise (Railway tracks)

ArGV 4 - Minimum safety distances between rail vehicle loading profiles
and buildings/obstacles.
Art. 13 Abs. 1:
  a) Restricted rail worker areas: min 60 cm
  b) General traffic areas: min 100 cm

Generated from: ch/822/de/822.114.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class argv4_gleisbereich_nur_bahnpersonal(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the rail area is exclusively for rail workers (SR 822.114 Art. 13 Abs. 1 lit. a)"
    reference = "SR 822.114 Art. 13"
    default_value = False


class argv4_min_sicherheitsabstand_gleise(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Minimum safety distance from rail vehicle profile to obstacles in cm (SR 822.114 Art. 13 Abs. 1)"
    reference = "SR 822.114 Art. 13"

    def formula(person, period, parameters):
        nur_bahnpersonal = person("argv4_gleisbereich_nur_bahnpersonal", period)
        # Rail workers only: 60 cm; general traffic: 100 cm
        return where(nur_bahnpersonal, 60.0, 100.0)
