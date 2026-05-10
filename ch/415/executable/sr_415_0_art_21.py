"""SR 415.0 Art. 21

Generated from: ch/415/de/415.0.md

Dopingkontrollen - Wer kontrolliert werden kann und wer kontrollieren darf.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class nimmt_an_sportwettkaempfen_teil(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Nimmt an Sportwettkaempfen teil"
    reference = "SR 415.0 Art. 21 Abs. 1"


class kann_dopingkontrolle_unterzogen_werden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kann Dopingkontrollen unterzogen werden"
    reference = "SR 415.0 Art. 21 Abs. 1"

    def formula(person, period, parameters):
        return person('nimmt_an_sportwettkaempfen_teil', period)
