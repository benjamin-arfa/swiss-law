"""SR 0.142.116.902 Art. 3

Generated from: ch/0/de/0.142.116.902.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class diplomatic_passholder(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Diplomatic passholder with visa exemption (Art. 3 SR 0.142.116.902)"

    def formula(person, period, parameters):
        diplomatic_passholder = person("has_diplomatic_pass", period.start)
        on_diplomatic_mission = person("on_diplomatic_mission", period.start)
        resides_in_foreign_state = person("resides_in_foreign_state", period.start)

        return (diplomatic_passholder & on_diplomatic_mission) & resides_in_foreign_state
