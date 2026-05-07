"""SR 531.211.36 Art. 1

Generated from: ch/531/de/531.211.36.md
Scope: This ordinance applies to rabies vaccines (ATC code J07BG).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class is_rabies_vaccine_under_stockpile_regulation(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Whether the product falls under mandatory stockpile release regulation for rabies vaccines (ATC J07BG)"
    reference = "SR 531.211.36 Art. 1"

    def formula(person, period, parameters):
        # Art. 1: The ordinance applies to rabies vaccines with ATC code J07BG
        is_rabies_vaccine = person("product_atc_code_is_j07bg", period)
        return is_rabies_vaccine
