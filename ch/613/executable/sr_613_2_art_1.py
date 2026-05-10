"""SR 613.2 Art. 1

Generated from: ch/613/de/613.2.md
Subject: The FiLaG regulates resource equalization, geographic-topographic
and sociodemographic burden equalization, and intercantonal cooperation.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class is_subject_to_filag(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the canton is subject to the Financial Equalization Act (FiLaG)"
    reference = "SR 613.2 Art. 1"

    def formula(person, period, parameters):
        # All cantons are subject to FiLaG
        is_canton = person("is_swiss_canton", period)
        return is_canton
