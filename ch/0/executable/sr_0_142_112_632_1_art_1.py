"""SR 0.142.112.632.1 Art. 1

Generated from: ch/0/de/0.142.112.632.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class residence_visitation_exemption_criteria(Variable):
    value_type = bool
    definition_period = MONTH
    label: str = "Residency country exemption criteria"
    description: str = "Return True if the visitor can pass this criterion"

    def formula(period):
        # assuming we have a country-level computation available
        visitor_country = period.visitor.country
        if (
            visitor_country.id == "CL" # Colombia - visitor's country
            and
            (ColombianCitizen.exemption_criteria(period).start.period('day').date <= period.date <= ColombianCitizen.exemption_criteria(period).end.period('day').date)
            or 
            (
                visitor_country.id == "CH" 
                and 
                (SwissCitizen.exemption_criteria(period).start.period('day').date <= period.date <= SwissCitizen.exemption_criteria(period).end.period('day').date)
            )
        ):
            return True
        else:
            return False
