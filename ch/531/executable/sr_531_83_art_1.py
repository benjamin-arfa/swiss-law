"""SR 531.83 Art. 1 — Geltungsbereich

Verordnung über die Beschränkung der Verwendung von Alteplase.
Generated from: ch/de/531/531.83.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_alteplase_ueber_2mg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist der Wirkstoff Alteplase mit einer Dosierung stärker als 2 mg (ATC-Code B01AD02)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2022/439/de#art_1"


class unterliegt_verwendungsbeschraenkung_alteplase(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unterliegt der Verwendungsbeschränkung für Alteplase (SR 531.83 Art. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2022/439/de#art_1"

    def formula(person, period, parameters):
        # Art. 1: Gilt für Alteplase (ATC-Code B01AD02) mit Dosierung > 2 mg.
        return person('ist_alteplase_ueber_2mg', period)
