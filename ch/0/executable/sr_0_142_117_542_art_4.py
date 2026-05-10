"""SR 0.142.117.542 Art. 4

Generated from: ch/0/de/0.142.117.542.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class denied_entry(Variable):
    value_type = bool
    entity = Person
    label = 'Entry denied based on public order;'
    definition_period = YEAR
    default_value = False

    def formula(person, period, parameters):
        public_order = has_denied_entry('public_order', person, parameters)
        national_security = has_denied_entry('national_security', person, parameters)
        public_health = has_denied_entry('public_health', person, parameters)
        other_reasons = has_denied_entry('other_reasons', person, parameters)

        weights = {
            'public_order': .2,
            'national_security': .1,
            'public_health': .3,
            'other_reasons': 0.2
        }

        max_value = np.sum([value for value in weights.values()])

        return public_order * weights['public_order'] / max_value + \
               national_security * weights['national_security'] / max_value + \
               public_health * weights['public_health'] / max_value + \
               other_reasons * weights['other_reasons'] / max_value > 0.05

def has_denied_entry(reason, person, parameters, period=period):
    return parameters(period).refused_entry[reason]
