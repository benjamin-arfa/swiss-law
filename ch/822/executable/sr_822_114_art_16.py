"""SR 822.114 Art. 16 - Rampenauffahrten (Ramp gradients)

ArGV 4 - Maximum ramp gradients.
Art. 16:
  - General vehicles: max 10% gradient
  - Hand-drawn vehicles: max 5% gradient

Generated from: ch/822/de/822.114.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_switzerland.entities import Person


class argv4_rampe_handgezogen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the ramp is used for hand-drawn vehicles (SR 822.114 Art. 16)"
    reference = "SR 822.114 Art. 16"
    default_value = False


class argv4_max_rampenneigung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximum ramp gradient in percent (SR 822.114 Art. 16)"
    reference = "SR 822.114 Art. 16"

    def formula(person, period, parameters):
        handgezogen = person("argv4_rampe_handgezogen", period)
        return where(handgezogen, 5.0, 10.0)


class argv4_rampenneigung_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether actual ramp gradient meets requirements (SR 822.114 Art. 16)"
    reference = "SR 822.114 Art. 16"

    def formula(person, period, parameters):
        tatsaechlich = person("argv4_tatsaechliche_rampenneigung", period)
        maximum = person("argv4_max_rampenneigung", period)
        return tatsaechlich <= maximum


class argv4_tatsaechliche_rampenneigung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Actual ramp gradient in percent (SR 822.114 Art. 16)"
    reference = "SR 822.114 Art. 16"
    default_value = 0.0
