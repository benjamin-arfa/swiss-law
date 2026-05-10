"""SR 0.142.117.149 Art. 4

Generated from: ch/0/de/0.142.117.149.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class take_responsibility(Variable):
    value_type = bool
    entity = Country
    definition_period = MONTH
    label = "Take or reject responsibility for stateless person"

    def formula(country, period, parameters):
        permit = country("last_valid_entry_permit", period)
        conditions = (
            country("has_valid_entries_permit", period, permit)
            & country("have_non_compliant_entries_from_other_country", period, permit)
        )
        responsible_country = country("first_country_to_issue_last_valid_entry_permit", period)

        return (country.index == responsible_country) & conditions
