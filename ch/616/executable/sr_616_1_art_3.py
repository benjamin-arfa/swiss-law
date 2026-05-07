"""SR 616.1 Art. 3

Generated from: ch/616/de/616.1.md
Definitions: Financial aids are monetary advantages granted outside federal
administration to promote tasks. Compensations are payments to offset financial
burdens from legally mandated or delegated public tasks.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class is_financial_aid(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the payment qualifies as a financial aid (Finanzhilfe) under SuG"
    reference = "SR 616.1 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        outside_admin = person("recipient_outside_federal_administration", period)
        promotes_task = person("promotes_recipient_chosen_task", period)
        return outside_admin * promotes_task


class is_compensation_payment(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the payment qualifies as a compensation (Abgeltung) under SuG"
    reference = "SR 616.1 Art. 3 Abs. 2"

    def formula(person, period, parameters):
        outside_admin = person("recipient_outside_federal_administration", period)
        mandated_task = person("fulfills_federally_mandated_task", period)
        delegated_task = person("fulfills_federally_delegated_task", period)
        return outside_admin * (mandated_task + delegated_task)
