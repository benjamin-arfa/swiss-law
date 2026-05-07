"""SR 0.142.117.542 Art. 3

Generated from: ch/0/de/0.142.117.542.md
"""

# Import necessary libraries
from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person

# Define the entity for the variable
class bilateral_residency_obligation(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Bilateral residency obligation under reciprocal agreement"

    def formula(person, period, parameters):
        return person("residency_status_abroad", period) == "compliant"

# Define another variable for residency status in Switzerland
class residency_status_abroad(Variable):
    value_type = str
    entity = Person
    definition_period = MONTH
    label = "Residency status of individual within foreign territory"

    def formula(person, period, parameters):
        return choose_period(
            period,
            [parameters(period).residency_status_abroad
             if not (parameters(period).bilateral_residency_agreement
                    and (parameters(period).bilateral_residency_agreement
                        == "foreign_restriction_in_force"))
             else parameters(period).residency_status_abroad,
            default=""
        ),
        default="" # default value if not specified
    )

# Define entity residency status abroad
class residency_status_abroad_parameters(ScenarioParameters):
    values = [
        "compliant",
        "noncompliant",
        "no_agreement",
        "undocumented",
        None,
        ""
    ]
    # bilateral residency agreement
    bilateral_residency_agreement = [
        "foreign_restriction_in_force",
        "local_restriction_in_force",
        None,
        ""
    ]
