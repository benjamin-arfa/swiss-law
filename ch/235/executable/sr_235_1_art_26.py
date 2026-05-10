"""SR 235.1 Art. 26

Generated from: ch/235/de/235.1.md

Wahl und Stellung des Eidgenoessischen Datenschutz- und
Oeffentlichkeitsbeauftragten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_beauftragter_amtsdauer_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Amtsdauer des Datenschutz- und Oeffentlichkeitsbeauftragten in Jahren"
    reference = "SR 235.1 Art. 26 Abs. 1"

    def formula(person, period, parameters):
        return person('dsg_beauftragter_amtsdauer_jahre', period) * 0 + 4


class dsg_beauftragter_unabhaengig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Beauftragter uebt Funktion unabhaengig aus (keine Weisungen)"
    reference = "SR 235.1 Art. 26 Abs. 3"

    def formula(person, period, parameters):
        return person('dsg_beauftragter_unabhaengig', period) * 0 + 1
