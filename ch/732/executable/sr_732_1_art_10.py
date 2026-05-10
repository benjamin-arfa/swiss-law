"""SR 732.1 Art. 10

Generated from: ch/732/de/732.1.md

Lufttransport von plutoniumhaltigen Kernmaterialien: Absolutes Verbot
des Transports plutoniumhaltiger Kernmaterialien im schweizerischen
Luftraum.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_plutoniumhaltiges_kernmaterial(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um plutoniumhaltiges Kernmaterial handelt"
    reference = "SR 732.1 Art. 10"


class transport_im_schweizerischen_luftraum(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Transport im schweizerischen Luftraum stattfindet"
    reference = "SR 732.1 Art. 10"


class lufttransport_plutonium_verboten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Lufttransport plutoniumhaltiger Kernmaterialien verboten ist"
    reference = "SR 732.1 Art. 10"

    def formula(person, period, parameters):
        plutonium = person('ist_plutoniumhaltiges_kernmaterial', period)
        luftraum = person('transport_im_schweizerischen_luftraum', period)

        return plutonium * luftraum
