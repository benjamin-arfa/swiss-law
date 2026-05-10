"""SR 192.126 Art. 49

Generated from: ch/192/de/192.126.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class feiertage_pro_jahr(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl bezahlter Feiertage pro Jahr (Art. 49)"
    reference = "SR 192.126 Art. 49"

    def formula(person, period, parameters):
        # Art. 49: Mindestens 9 bezahlte Feiertage pro Jahr
        return person('alter', period) * 0 + 9
