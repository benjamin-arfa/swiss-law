"""SR 0.142.116.659 Art. 4

Generated from: ch/0/de/0.142.116.659.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class swiss_state_return_request_acceptance(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Acceptance of return of a Swiss citizen from Russia (Art. 4 SR 0.142.116.659)"

    def formula(person, period, parameters):
        is_swiss_citizen = not person("abandoned_swiss_citizenship", previous_period)
        was_swiss_citizen_before_russian_residency = person("was_swiss_citizen_before_russian_residency", previous_period)
        return is_swiss_citizen & was_swiss_citizen_before_russian_residency
