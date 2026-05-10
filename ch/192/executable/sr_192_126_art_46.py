"""SR 192.126 Art. 46

Generated from: ch/192/de/192.126.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class arbeitszeit_stunden_pro_woche(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Woechentliche Arbeitszeit in Stunden"
    reference = "SR 192.126 Art. 46"

class arbeitszeit_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Arbeitszeit ueberschreitet nicht 45 Stunden pro Woche (Art. 46)"
    reference = "SR 192.126 Art. 46"

    def formula(person, period, parameters):
        stunden = person('arbeitszeit_stunden_pro_woche', period)
        # Art. 46: Maximale woechentliche Arbeitszeit bei Vollzeit = 45 Stunden
        return stunden <= 45
