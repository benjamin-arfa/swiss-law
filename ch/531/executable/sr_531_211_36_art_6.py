"""SR 531.211.36 Art. 6

Generated from: ch/531/de/531.211.36.md
Bookkeeping and reporting obligation: Stockpile holders must maintain records
of all stocks and changes, and report weekly to the Heilmittel division.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class has_stockpile_reporting_obligation(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Whether entity has weekly reporting obligation to Heilmittel division"
    reference = "SR 531.211.36 Art. 6"

    def formula(person, period, parameters):
        return person("is_mandatory_stockpile_holder", period)
