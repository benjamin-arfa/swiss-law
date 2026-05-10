"""SR 531.211.36 Art. 3

Generated from: ch/531/de/531.211.36.md
Release: A stockpile holder who does not have sufficient free supplies and cannot
procure the missing quantity may request release from the Heilmittel division.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class eligible_for_stockpile_release_request(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Whether a stockpile holder may request release of rabies vaccine stockpile"
    reference = "SR 531.211.36 Art. 3"

    def formula(person, period, parameters):
        is_stockpile_holder = person("is_mandatory_stockpile_holder", period)
        has_insufficient_supplies = person("has_insufficient_free_supplies", period)
        cannot_procure = person("unable_to_procure_missing_quantity", period)
        return is_stockpile_holder * has_insufficient_supplies * cannot_procure
