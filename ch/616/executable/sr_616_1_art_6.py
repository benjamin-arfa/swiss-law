"""SR 616.1 Art. 6

Generated from: ch/616/de/616.1.md
Conditions for financial aids: Federal interest, cantonal inability,
insufficient fulfilment without aid, exhausted self-help, no simpler alternative.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class financial_aid_conditions_met(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether all conditions for granting a financial aid are met"
    reference = "SR 616.1 Art. 6"

    def formula(person, period, parameters):
        federal_interest = person("federal_interest_in_task", period)
        cantonal_gap = person("cantons_cannot_fulfill_independently", period)
        insufficient_without = person("task_insufficient_without_aid", period)
        self_help_exhausted = person("self_help_measures_exhausted", period)
        no_simpler_way = person("no_simpler_alternative_exists", period)

        return (federal_interest * cantonal_gap * insufficient_without
                * self_help_exhausted * no_simpler_way)
