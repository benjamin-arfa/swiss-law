"""SR 0.103.3 Art. 11

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class fair_disappearance_treatment(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Right to fair treatment during disappearance procedures (Art. 11 CRC)"

    def formula(person, period, parameters):
        disappearance_suspected = person("disappearance_suspect", period)
        current_proceedings = person("disappearance_proceedings", period)
        lesser_gravity_proceedings = person("lesser_gravity_disappearance_proceedings", period)

        return disappearance_suspected & current_proceedings & (not lesser_gravity_proceedings)


class disappearance_proceedings(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Disappearance proceedings ongoing (Art. 11 CRC)"

    def formula(person, period, parameters):
        disappearance_suspect = person("disappearance_suspect", period)
        disappearance_reported = person("disappearance_reported", period)

        return disappearance_suspect & disappearance_reported


class lesser_gravity_disappearance_proceedings(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Disappearance proceedings of lesser gravity ongoing (Art. 9(2) CRC)"

    def formula(person, period, parameters):
        disappearance_suspect = person("disappearance_suspect", period)
        physical_harm_likely = person("physical_harm_likely", period)
        disappearance_reported = person("disappearance_reported", period)

        return disappearance_suspect & disappearance_reported & (not physical_harm_likely)


class disappearance_suspect(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Suspected disappearance (Article 6 CRC)"

    def formula(person, period, parameters):
        current_disappearance_investigation = person("current_disappearance_investigation", period)

        return current_disappearance_investigation


class physical_harm_likely(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Physical harm likely in case of disappearance"

    def formula(person, period, parameters):
        individual_characteristics = person("individual_characteristics", period)
        disappearance_dynamics = person("disappearance_dynamics", period)

        return individual_characteristics & disappearance_dynamics
