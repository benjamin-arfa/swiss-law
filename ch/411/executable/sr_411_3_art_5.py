"""SR 411.3 Art. 5

Generated from: ch/411/de/411.3.md

Gesuch - Jaehrliche Einreichung bis 28. Februar.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gesuch_eingereicht_vor_frist(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wurde das Gesuch bis zum 28. Februar eingereicht"
    reference = "SR 411.3 Art. 5 Abs. 1"


class gesuch_frist_tag(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist fuer die Einreichung des Gesuchs (Tag im Februar)"
    reference = "SR 411.3 Art. 5 Abs. 1"

    def formula(person, period):
        return 28
