"""SR 836.21 Art. 10a - Duration of entitlement for self-employed persons

Art. 10a: Entitlement begins on the first day of the month in which
self-employment starts and ends on the last day of the month in which
self-employment ceases. For interruptions and death, Art. 10 applies
by analogy.

Generated from: ch/836/de/836.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class selbststaendig_erwerbstaetig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is self-employed (Art. 10a FamZV)"
    default_value = False


class selbststaendigkeit_beginn_monat(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Self-employment started in this month (Art. 10a par. 1 FamZV)"
    default_value = False


class selbststaendigkeit_ende_monat(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Self-employment ended in this month (Art. 10a par. 1 FamZV)"
    default_value = False


class anspruch_famz_selbststaendig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Entitlement to family allowances for self-employed (Art. 10a FamZV)"

    def formula(person, period, parameters):
        return person("selbststaendig_erwerbstaetig", period)
