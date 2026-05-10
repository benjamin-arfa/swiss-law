"""SR 444.1 Art. 24

Generated from: ch/444/de/444.1.md

Vergehen: Vorsatz: Freiheitsstrafe bis 1 Jahr oder Geldstrafe.
Fahrlaessigkeit: Busse bis 20'000 CHF. Gewerbsmaessig: Freiheitsstrafe
bis 2 Jahre oder Geldstrafe.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kulturguetertransfer_vorsaetzlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Widerhandlung vorsaetzlich begangen wurde"
    reference = "SR 444.1 Art. 24 Abs. 1"


class kulturguetertransfer_fahrlaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Widerhandlung fahrlaessig begangen wurde"
    reference = "SR 444.1 Art. 24 Abs. 2"


class kulturguetertransfer_gewerbsmaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob gewerbsmaessig gehandelt wurde"
    reference = "SR 444.1 Art. 24 Abs. 3"


class max_busse_kulturguetertransfer(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Busse bei fahrlaessigem Kulturguetertransfer-Vergehen (CHF)"
    reference = "SR 444.1 Art. 24 Abs. 2"

    def formula(person, period, parameters):
        fahrlaessig = person('kulturguetertransfer_fahrlaessig', period)
        return fahrlaessig * 20000
