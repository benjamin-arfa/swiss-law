"""SR 702.1 Art. 4

Generated from: ch/702/de/702.1.md

Strukturierter Beherbergungsbetrieb: A structured accommodation business
requires hotel-like services, hotel-like concept, and unified operation.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class beherbergung_hotelmaessige_dienstleistungen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Betrieb hotelmaessige Dienstleistungen und Infrastrukturen umfasst"
    reference = "SR 702.1 Art. 4 lit. a"


class beherbergung_hotelaehnliches_betriebskonzept(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Betrieb ein hotelaehnliches Betriebskonzept aufweist"
    reference = "SR 702.1 Art. 4 lit. b"


class beherbergung_einheitlicher_betrieb(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Bewirtschaftung im Rahmen eines einheitlichen Betriebs sichergestellt ist"
    reference = "SR 702.1 Art. 4 lit. c"


class strukturierter_beherbergungsbetrieb(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein strukturierter Beherbergungsbetrieb vorliegt"
    reference = "SR 702.1 Art. 4"

    def formula(person, period, parameters):
        return (
            person('beherbergung_hotelmaessige_dienstleistungen', period) *
            person('beherbergung_hotelaehnliches_betriebskonzept', period) *
            person('beherbergung_einheitlicher_betrieb', period)
        )
