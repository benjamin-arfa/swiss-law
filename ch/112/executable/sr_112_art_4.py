"""SR 112 Art. 4

Generated from: ch/de/112.md

Building restrictions on Vannazhalde and obligation to maintain
the Bundesrathaus terrace as public space.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vannazhalde_bauverbot(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob auf der Vannazhalde ein Bauverbot gilt (Firste nicht ueber Terrasse)"
    reference = "SR 112 Art. 4 Abs. 1"


class terrasse_oeffentliche_anlage(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Terrasse als oeffentliche Anlage erhalten werden muss"
    reference = "SR 112 Art. 4 Abs. 2"


class kleine_schanze_promenade_pflicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Einwohnergemeinde die kleine Schanze als Promenade unterhalten muss"
    reference = "SR 112 Art. 4 Abs. 3"
