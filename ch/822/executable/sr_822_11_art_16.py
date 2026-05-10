"""SR 822.11 Art. 16

Generated from: ch/822/de/822.11.md

Art. 16: Nachtarbeitsverbot - Employment of workers outside of the
operational day and evening work hours (Art. 10) is prohibited,
subject to Art. 17 exceptions.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class arg_arbeitet_nachts(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Arbeitnehmer arbeitet ausserhalb der betrieblichen Tages-/Abendarbeit (Nachtarbeit)"
    reference = "SR 822.11 Art. 16"


class arg_nachtarbeit_bewilligt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Nachtarbeit ist nach Art. 17 ArG bewilligt"
    reference = "SR 822.11 Art. 17"
    default_value = False


class arg_nachtarbeit_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Nachtarbeit ist zulaessig (grundsaetzlich verboten, Art. 17 Ausnahmen vorbehalten)"
    reference = "SR 822.11 Art. 16"

    def formula(person, period, parameters):
        arbeitet_nachts = person('arg_arbeitet_nachts', period)
        bewilligt = person('arg_nachtarbeit_bewilligt', period)

        # Art. 16: Nachtarbeit ist untersagt, ausser wenn nach Art. 17 bewilligt
        return where(arbeitet_nachts, bewilligt, True)
