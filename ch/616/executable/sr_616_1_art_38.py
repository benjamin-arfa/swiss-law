"""SR 616.1 Art. 38

Generated from: ch/616/de/616.1.md
Obtaining an advantage by fraud: Whoever intentionally provides incorrect or
incomplete information in a subsidy procedure to obtain an unjustified advantage
shall be punished with a fine.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class committed_subsidy_fraud(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether person intentionally provided false information to obtain subsidy advantage"
    reference = "SR 616.1 Art. 38"

    def formula(person, period, parameters):
        false_info = person("provided_false_subsidy_information", period)
        intentional = person("acted_intentionally", period)
        sought_advantage = person("sought_unjustified_advantage", period)
        return false_info * intentional * sought_advantage
