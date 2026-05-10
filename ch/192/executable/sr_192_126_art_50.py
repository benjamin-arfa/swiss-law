"""SR 192.126 Art. 50

Generated from: ch/192/de/192.126.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ferientage_pro_jahr(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Ferientage pro Jahr (Art. 50)"
    reference = "SR 192.126 Art. 50"

    def formula(person, period, parameters):
        alter = person('hausangestellte_alter', period)
        dienstjahre = person('dienstjahre', period)
        # Art. 50: Mindestens 4 Wochen (20 Arbeitstage), 5 Wochen (25 Tage) fuer unter 20-Jaehrige
        return where(alter < 20, 25, 20)
