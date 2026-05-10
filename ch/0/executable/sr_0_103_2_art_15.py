"""SR 0.103.2 Art. 15

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class was_offense_punishable(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Was the offense punishable at the time it was committed? (Art. 15 CR)"

    def formula(person, period, parameters):
        offense_date = dates.time_period(
            parameters(period).counsel.ofense_reference['date']
        ).start_date
        law_changes = parameters(period).counsel.history_of_law[
            offense_date
        ]
        was_punishable = law_changes.is_punishable
        return was_punishable
