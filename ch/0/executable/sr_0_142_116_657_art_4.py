"""SR 0.142.116.657 Art. 4

Generated from: ch/0/de/0.142.116.657.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class stagiairesbewilligung_duration(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Stagiairesbewilligung duration (SR 0.142.116.657 Art. 4)"

    def formula(person, period, parameters):
        total_time_allowed = 12
        extension_allowed = 6
        extension_granted = person("extension_granted", period)
        total_duration = total_time_allowed + extension_granted
        return total_duration <= 18
