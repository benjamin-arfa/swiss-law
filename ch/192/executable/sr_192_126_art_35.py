"""SR 192.126 Art. 35

Generated from: ch/192/de/192.126.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dienstjahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Dienstjahre beim aktuellen Arbeitgeber"
    reference = "SR 192.126 Art. 35"

class kuendigungsfrist_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Kuendigungsfrist in Monaten (Art. 35)"
    reference = "SR 192.126 Art. 35"

    def formula(person, period, parameters):
        dienstjahre = person('dienstjahre', period)
        # Art. 35: 1 Monat im 1. Dienstjahr, 2 Monate ab 2. bis 9. Dienstjahr, 3 Monate ab 10. Dienstjahr
        return where(dienstjahre < 1, 1,
               where(dienstjahre < 10, 2, 3))
