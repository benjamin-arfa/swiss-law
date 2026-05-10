"""SR 221.213.2 Art. 16

Generated from: ch/221/de/221.213.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kuendigung_schriftlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kündigung erfolgte schriftlich"
    reference = "SR 221.213.2 Art. 16 Abs. 1"


class kuendigung_gueltig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kündigung des Pachtvertrags ist gültig"
    reference = "SR 221.213.2 Art. 16 Abs. 1"

    def formula(person, period, parameters):
        return person('kuendigung_schriftlich', period)


class kuendigungsfrist_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Kündigungsfrist in Monaten"
    reference = "SR 221.213.2 Art. 16 Abs. 2"

    def formula(person, period, parameters):
        # Die Kündigungsfrist beträgt ein Jahr (12 Monate)
        return person.filled_array(12)
