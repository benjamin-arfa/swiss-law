"""SR 0.142.117.582 Art. 1

Generated from: ch/0/de/0.142.117.582.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class diplomatic_and_consular_exemption(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Diplomatic and consular personnel exemption from visa requirements (Art. 1 SR 0.142.117.582)"

    def formula(person, period, parameters):
        has_diplomatic_passport = person("has_diplomatic_passport", period)
        has_consular_tie = person("has_consular_tie", period)
        holder_of_national_special_passport = person("has_national_special_passport", period)

        returning_diplomat = (has_diplomatic_passport | has_consular_tie | holder_of_national_special_passport)
        return returning_diplomat
