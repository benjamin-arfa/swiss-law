"""SR 362.1 Art. 13

Generated from: ch/362/de/362.1.md
Termination rules for the Schengen/Dublin agreement.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kuendigungsfrist_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Kuendigungsfrist der Vereinbarung in Monaten"
    reference = "SR 362.1 Art. 13 Abs. 1"

    def formula(person, period):
        # Kuendigung schriftlich unter Einhaltung einer Frist von 6 Monaten
        return person('kuendigungsfrist_monate', period) * 0 + 6


class laufende_verpflichtungen_einzuhalten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Laufende Verpflichtungen sind auch nach Kuendigung einzuhalten"
    reference = "SR 362.1 Art. 13 Abs. 2"

    def formula(person, period):
        # In jedem Fall einzuhalten
        return True + person('kuendigungsfrist_monate', period) * 0
