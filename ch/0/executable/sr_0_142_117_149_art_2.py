"""SR 0.142.117.149 Art. 2

Generated from: ch/0/de/0.142.117.149.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# import the custom entity Person from entities.py

from entities import Person


# an adaptation of the openfisca implementation
class ImmigrationStatus(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR

    def formula(person, period, parameters):
        immigration_date = person("immigration_date", period)
        # assuming the immigrant has nationalities
        nationality_1 = person("nationality_1", period)
        nationality_2 = person("nationality_2", period)

        # implement the conditions for recovery (Article 2), here simplified
        is_recovered = (nationality_1 == 'requested_state') | (nationality_2 == 'requested_state') | \
                       ((immigration_date == 'date_of_immigration') & (not nationality_1 == 'requested_state'))
        return is_recovered
