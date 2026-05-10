"""SR 632.102.1 Art. 3

Generated from: ch/632/de/632.102.1.md
Entry into force and validity: The ordinance enters into force on 1 July 2019
and is valid until 31 December 2023.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class textile_tariff_suspension_in_force(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Whether the textile tariff suspension ordinance is in force"
    reference = "SR 632.102.1 Art. 3"

    def formula(person, period, parameters):
        year = period.start.year
        month = period.start.month
        # In force from 1 July 2019 to 31 December 2023
        start = (year > 2019) + (year == 2019) * (month >= 7)
        end = (year < 2023) + (year == 2023) * (month <= 12)
        return start * end
