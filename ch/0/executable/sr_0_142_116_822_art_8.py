"""SR 0.142.116.822 Art. 8

Generated from: ch/0/de/0.142.116.822.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lost_or_stolen_identity_eligibility(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligibility for repatriation with a substitute ID (Art. 8 SR 0.142.116.822)"

    def formula(person, period, parameters):
        nationality_swiss = person("nationality").contains("Switzerland") | person("nationality").contains("Serbia")
        identification_lost_or_stolen = person("identification_lost_or_stolen", period)
        substitute_id_valid = person("substitute_id_valid", period)
        return nationality_swiss & identification_lost_or_stolen & substitute_id_valid
