"""SR 360.2 Art. 12

Generated from: ch/360/de/360.2.md

Zugriff auf die Unterkategorie Ermittlungsfall: Einschraenkung auf
involvierte Strafverfolgungsbehoerden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class nes_involviert_in_ermittlungsverfahren(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Strafverfolgungsbehoerde ist in das Ermittlungsverfahren involviert"
    reference = "SR 360.2 Art. 12 Abs. 1"


class nes_zugriff_ermittlungsfall(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Online-Zugriff auf Unterkategorie Ermittlungsfall ist berechtigt"
    reference = "SR 360.2 Art. 12"

    def formula(person, period, parameters):
        return person('nes_involviert_in_ermittlungsverfahren', period)
