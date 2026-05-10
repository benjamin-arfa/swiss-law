"""SR 837.21 Art. 12 - Pauschale fuer Heizkosten (Heating costs flat rate)

For persons who must heat their rented apartments themselves (not paying
heating costs to the landlord per Art. 257b(1) OR), half of the ancillary
costs flat rate (Art. 11 Abs. 3) is added for heating costs.

Generated from: ch/837/de/837.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class uelv_selbst_heizend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person muss Mietwohnung selbst beheizen (Art. 12 UeLV)"
    reference = "SR 837.21 Art. 12"


class uelv_heizkosten_pauschale(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Pauschale fuer Heizkosten in CHF pro Jahr (Art. 12 UeLV)"
    reference = "SR 837.21 Art. 12"

    def formula(person, period, parameters):
        selbst_heizend = person('uelv_selbst_heizend', period)
        # Half of the ancillary costs flat rate (CHF 3480 / 2 = CHF 1740)
        nebenkosten_pauschale = 3480
        return selbst_heizend * nebenkosten_pauschale / 2
