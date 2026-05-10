"""SR 172.041.0 Art. 5

Generated from: ch/172/de/172.041.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class barauslagen_verhaeltnismaessig_hoch_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Schwelle fuer verhaeltnismaessig hohe Barauslagen in CHF (Art. 5 Abs. 2)"
    reference = "SR 172.041.0 Art. 5"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 250
