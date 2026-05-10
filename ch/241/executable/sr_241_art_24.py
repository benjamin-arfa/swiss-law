"""SR 241 Art. 24

Generated from: ch/de/241.md

Criminal penalties for violations of price disclosure obligations:
fine up to CHF 20,000 for intentional violations, fine for negligent ones.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class preisbekanntgabe_vorsaetzlich_verletzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Preisbekanntgabepflicht vorsaetzlich verletzt wird"
    reference = "SR 241 Art. 24 Abs. 1"


class preisbekanntgabe_fahrlaessig_verletzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Preisbekanntgabepflicht fahrlaessig verletzt wird"
    reference = "SR 241 Art. 24 Abs. 2"


class preisbekanntgabe_busse_max(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Busse fuer Preisbekanntgabeverletzung (CHF)"
    reference = "SR 241 Art. 24 Abs. 1"

    def formula(person, period, parameters):
        return person('preisbekanntgabe_vorsaetzlich_verletzt', period) * 20000.0
