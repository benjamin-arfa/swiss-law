"""SR 173.320.3 Art. 7

Generated from: ch/173/de/173.320.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kostenvoranschlag_schwelle_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Schwelle ab der voraussichtliche Kosten mitgeteilt werden in CHF (Art. 7)"
    reference = "SR 173.320.3 Art. 7"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 200.0
