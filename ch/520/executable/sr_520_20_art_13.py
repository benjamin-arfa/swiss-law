"""SR 520.20 Art. 13

Generated from: ch/520/de/520.20.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vrsl_in_kraft(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Die VRSL ist in Kraft (Geltungsdauer verlaengert bis 31. Dezember 2025)"
    reference = "SR 520.20 Art. 13"

    def formula_2016_04(person, period, parameters):
        """In force from 1 April 2016, extended until 31 December 2025."""
        return period.start.year <= 2025
