"""SR 367.1 Art. 4

Generated from: ch/367/de/367.1.md

Organe von PTI Schweiz und Amtsdauer.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class pti_amtsdauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Amtsdauer der gewaehlten Mitglieder der PTI-Organe in Jahren"
    reference = "SR 367.1 Art. 4 Abs. 3"

    def formula(person, period):
        return 4
