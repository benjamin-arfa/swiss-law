"""SR 0.142.114.544 Art. 3

Generated from: ch/0/de/0.142.114.544.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class stagiairebewilligung_extension(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Stagiairebewilligung extension approved (Art. 3)"

    def formula(person, period, parameters):
        duration = person("stagiairebewilligung_duration", period)
        max_duration = parameters(period).labour.market_regulations.stagiairebewilligung.max_duration
        return duration > max_duration
