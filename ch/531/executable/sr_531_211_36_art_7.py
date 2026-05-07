"""SR 531.211.36 Art. 7

Generated from: ch/531/de/531.211.36.md
Appeals: Against decisions of the Heilmittel division, the stockpile holder
may file an objection within 5 days pursuant to Art. 45 LVG (SR 531).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class stockpile_appeal_deadline_days(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Number of days to file objection against Heilmittel division decisions"
    reference = "SR 531.211.36 Art. 7"

    def formula(person, period, parameters):
        return 5  # Fixed 5-day deadline per Art. 45 LVG
