"""SR 0.142.117.673 Art. 10

Generated from: ch/0/de/0.142.117.673.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class visa_extension_duration(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Visa extension duration for Ukrainian citizens in extraordinary circumstances (Art. 10 SR 0.142.117.673)"

    def formula(person, period, parameters):
        is_ukrainian = person("nationality", period) == "Ukraine"
        return parameters(period).visa_extension.duration if is_ukrainian else 0
