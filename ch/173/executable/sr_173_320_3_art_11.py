"""SR 173.320.3 Art. 11

Generated from: ch/173/de/173.320.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class urteil_nachnahme_schwelle_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Schwelle fuer Nachnahme bei Urteilsherausgabe in CHF (Art. 11 Abs. 2)"
    reference = "SR 173.320.3 Art. 11"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 100.0
