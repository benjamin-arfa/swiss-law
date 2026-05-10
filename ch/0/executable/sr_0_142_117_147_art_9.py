"""SR 0.142.117.147 Art. 9

Generated from: ch/0/de/0.142.117.147.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ahv_regulation_validity(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Validation of AHV regulation from 1948-01-01 to 1948-12-31 (Art. 9: SR 0.142.117.147)"

    def formula(person, period, parameters):
        end_date = parameters(period).social_security.start_date
        return (end_date <= period.date) | (end_date > period.date & person("early_opt_out", period) | person("kündigung_1_juli", period))
