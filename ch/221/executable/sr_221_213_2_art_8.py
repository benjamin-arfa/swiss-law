"""SR 221.213.2 Art. 8

Generated from: ch/221/de/221.213.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class pachtvertrag_nicht_gekuendigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pachtvertrag wurde nicht ordnungsgemäss gekündigt"
    reference = "SR 221.213.2 Art. 8 Abs. 1"


class pachtvertrag_stillschweigend_fortgesetzt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pachtvertrag nach vereinbarter Dauer stillschweigend fortgesetzt"
    reference = "SR 221.213.2 Art. 8 Abs. 1 lit. b"


class fortsetzungsdauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Fortsetzungsdauer der Pacht in Jahren"
    reference = "SR 221.213.2 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        # Der Pachtvertrag gilt für jeweils weitere sechs Jahre
        return person.filled_array(6)
