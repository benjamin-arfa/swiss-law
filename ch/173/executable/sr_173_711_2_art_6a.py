"""SR 173.711.2 Art. 6a

Generated from: ch/173/de/173.711.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_mitglied_verwaltungskommission(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist Mitglied der Verwaltungskommission"
    reference = "SR 173.711.2 Art. 6a"

class funktionszulage_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Funktionszulage fuer Mitglieder der Verwaltungskommission in CHF (Art. 6a)"
    reference = "SR 173.711.2 Art. 6a"

    def formula(person, period, parameters):
        # Art. 6a: 10'000 CHF pro Jahr fuer Mitglieder der Verwaltungskommission
        return person('ist_mitglied_verwaltungskommission', period) * 10000
