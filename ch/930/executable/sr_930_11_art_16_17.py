"""SR 930.11 Art. 16 & 17

Generated from: ch/930/de/930.11.md

Art. 16: Vergehen - Criminal offenses:
1. Intentionally placing non-conforming product endangering safety/health:
   imprisonment up to 1 year or monetary penalty
2. Commercial/profit-driven: imprisonment up to 3 years or monetary penalty
3. Negligent endangerment: monetary penalty up to 180 daily rates

Art. 17: Übertretungen - Misdemeanors:
1. Fine up to CHF 40,000 for: a. non-conforming labeling; b. violating
   cooperation/notification duties; c. violating regulations or orders
2. Negligent: fine up to CHF 20,000
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class prsg_vergehen_vorsaetzlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Vorsätzliches Vergehen nach Art. 16 Abs. 1 begangen"
    reference = "SR 930.11 Art. 16 Abs. 1"


class prsg_vergehen_gewerbsmaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gewerbsmässiges Vergehen oder aus Gewinnsucht (Art. 16 Abs. 2)"
    reference = "SR 930.11 Art. 16 Abs. 2"


class prsg_vergehen_fahrlaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Fahrlässige Gefährdung nach Art. 16 Abs. 3"
    reference = "SR 930.11 Art. 16 Abs. 3"


class prsg_uebertretung_vorsaetzlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Vorsätzliche Übertretung nach Art. 17 Abs. 1"
    reference = "SR 930.11 Art. 17 Abs. 1"


class prsg_uebertretung_fahrlaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Fahrlässige Übertretung nach Art. 17 Abs. 2"
    reference = "SR 930.11 Art. 17 Abs. 2"


class prsg_max_freiheitsstrafe_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Freiheitsstrafe bei Vergehen (Monate)"
    reference = "SR 930.11 Art. 16"

    def formula(person, period, parameters):
        vorsaetzlich = person('prsg_vergehen_vorsaetzlich', period)
        gewerbsmaessig = person('prsg_vergehen_gewerbsmaessig', period)
        # Commercial: up to 3 years (36 months); otherwise up to 1 year (12 months)
        return np.where(gewerbsmaessig, 36, np.where(vorsaetzlich, 12, 0))


class prsg_max_busse(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Busse bei Übertretung (CHF)"
    reference = "SR 930.11 Art. 17"

    def formula(person, period, parameters):
        vorsaetzlich = person('prsg_uebertretung_vorsaetzlich', period)
        fahrlaessig = person('prsg_uebertretung_fahrlaessig', period)
        return np.where(vorsaetzlich, 40000.0, np.where(fahrlaessig, 20000.0, 0.0))
