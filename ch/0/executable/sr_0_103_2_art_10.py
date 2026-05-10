"""SR 0.103.2 Art. 10

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class prison_minor_separation(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Separation of minors from adults in prison (Art. 10 SR 0.103.2)"

    def formula(person, period, parameters):
        age = (period.date - person("birth_date")).days / 365.25
        is_minor = age < 18

        # This variable assumes that a juvenile detention centre exists
        is_detained = person("detained", period)

        return is_minor & is_detained
