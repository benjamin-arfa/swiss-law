"""SR 918.1 Art. 13 - Inkrafttreten und Geltungsdauer

Generated from: ch/918/de/918.1.md

Inkrafttreten: 1. Januar 2025. Gilt bis 31. Dezember 2032.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class vpev_in_kraft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die VPEV (Verordnung Praemienverbilligung Ernteversicherungen) ist in Kraft"
    reference = "SR 918.1 Art. 13"

    def formula_2025(self, period, parameters):
        return period.start.year <= 2032

    def formula_2033(self, period, parameters):
        return False
