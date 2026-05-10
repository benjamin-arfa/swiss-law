"""SR 192.126 Art. 7

Generated from: ch/192/de/192.126.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_private_hausangestellte(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl privater Hausangestellter im Haushalt"
    reference = "SR 192.126 Art. 7"

class ist_missionschef(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Arbeitgeber ist Missionschef/in oder hohe/r Beamte/r"
    reference = "SR 192.126 Art. 7"

class max_hausangestellte(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Anzahl privater Hausangestellter pro Haushalt"
    reference = "SR 192.126 Art. 7"

    def formula(person, period, parameters):
        # Art. 7: Grundsaetzlich max. Anzahl je nach Status - Einzelfallentscheid EDA
        # Keine feste Obergrenze im Gesetz, EDA entscheidet
        return where(person('ist_missionschef', period), 4, 2)
