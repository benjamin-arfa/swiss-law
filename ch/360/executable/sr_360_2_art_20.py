"""SR 360.2 Art. 20

Generated from: ch/360/de/360.2.md

Weitere Bestimmungen zur Datenweitergabe.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class nes_verwertungsverbot_besteht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Verwertungsverbot fuer NES-Daten besteht"
    reference = "SR 360.2 Art. 20 Abs. 1"


class nes_ueberwiegende_interessen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ueberwiegende oeffentliche oder private Interessen stehen der Weitergabe entgegen"
    reference = "SR 360.2 Art. 20 Abs. 2"


class nes_weitergabe_verweigert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Weitergabe von NES-Daten wird verweigert"
    reference = "SR 360.2 Art. 20 Abs. 2"

    def formula(person, period, parameters):
        return person('nes_ueberwiegende_interessen', period)
