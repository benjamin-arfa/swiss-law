"""SR 837.21 Art. 6 - Berechnung bei Trennung der Ehe (Calculation upon marital separation)

When spouses are separated:
- Non-entitled spouse is not considered in the calculation
- If both are entitled, separate calculations for single persons
- Separation defined as: court-ordered, divorce pending, actual separation
  >= 1 year, or credibly long-term actual separation

Generated from: ch/837/de/837.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class uelv_ist_verheiratet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person ist verheiratet (Art. 6 UeLV)"
    reference = "SR 837.21 Art. 6"


class uelv_ehe_getrennt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ehepaar lebt getrennt (Art. 6 Abs. 3 UeLV)"
    reference = "SR 837.21 Art. 6 Abs. 3"


class uelv_ehepartner_anspruchsberechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ehepartnerin/Ehepartner ist ebenfalls anspruchsberechtigt (Art. 6 Abs. 2 UeLV)"
    reference = "SR 837.21 Art. 6 Abs. 2"


class uelv_berechnung_als_alleinstehend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ueberbrueckungsleistungen werden als Alleinstehende berechnet (Art. 6 UeLV)"
    reference = "SR 837.21 Art. 6"

    def formula(person, period, parameters):
        verheiratet = person('uelv_ist_verheiratet', period)
        getrennt = person('uelv_ehe_getrennt', period)
        partner_berechtigt = person('uelv_ehepartner_anspruchsberechtigt', period)
        # Unmarried: always single calculation
        # Married + separated + both entitled: single calculation (Abs. 2)
        # Married + separated + partner not entitled: single (partner excluded, Abs. 1)
        # Married + not separated: couple calculation
        return (1 - verheiratet) + verheiratet * getrennt
