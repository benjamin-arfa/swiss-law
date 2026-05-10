"""SR 819.14 Art. 7

Generated from: ch/819/de/819.14.md

Art. 7 Uebergangsfrist fuer tragbare Befestigungsgeraete mit Treibladungen:
Portable fastening devices with propellant charges and other tool-type
shooting devices may be placed on the market under previous law until 29 June 2011.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

import datetime


class maschv_tragbares_befestigungsgeraet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob es sich um ein tragbares Befestigungsgeraet mit Treibladung handelt"
    reference = "SR 819.14 Art. 7"


class maschv_uebergangsfrist_bisheriges_recht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das bisherige Recht noch anwendbar ist (Uebergangsfrist bis 29.06.2011)"
    reference = "SR 819.14 Art. 7"

    def formula(person, period, parameters):
        ist_befestigungsgeraet = person('maschv_tragbares_befestigungsgeraet', period)
        # Transition period ended 29 June 2011
        stichtag = datetime.date(2011, 6, 29)
        innerhalb_frist = period.start.date < stichtag
        return ist_befestigungsgeraet * innerhalb_frist
