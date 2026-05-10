"""SR 425.1 Art. 19

Generated from: ch/425/de/425.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kosten_ausbau_liegenschaft(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kosten fuer den Ausbau der Liegenschaft in CHF"
    reference = "SR 425.1 Art. 19 Abs. 2"


class maximaler_bundesbeitrag_liegenschaft(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximaler Bundesbeitrag an den Ausbau der Liegenschaft in CHF (hoechstens 50%)"
    reference = "SR 425.1 Art. 19 Abs. 2"

    def formula(person, period, parameters):
        kosten = person('kosten_ausbau_liegenschaft', period)
        return kosten * 0.5
