"""SR 150.1 Art. 10

Generated from: ch/150/de/150.1.md

Datenschutz: Die Kommission darf besonders schuetzenswerte Personendaten
bearbeiten, soweit zur Aufgabenerfuellung erforderlich. Personendaten
duerfen nur mit ausdruecklicher Einwilligung bekannt gegeben werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_ausdruecklich_eingewilligt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die betroffene Person ausdruecklich in die Bekanntgabe von Personendaten eingewilligt hat"
    reference = "SR 150.1 Art. 10 Abs. 2"


class darf_personendaten_bekanntgeben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Kommission Personendaten bekannt geben darf"
    reference = "SR 150.1 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        return person('hat_ausdruecklich_eingewilligt', period)
