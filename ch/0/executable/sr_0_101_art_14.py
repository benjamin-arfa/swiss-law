"""SR 0.101 Art. 14

Generated from: ch/0/de/0.101.md

Prohibition of discrimination: The enjoyment of Convention rights shall
be secured without discrimination on any ground such as sex, race, colour,
language, religion, political or other opinion, national or social origin,
association with a national minority, property, birth or other status.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class emrk_diskriminierungsverbot(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Diskriminierungsverbot beim Genuss der Konventionsrechte gilt"
    reference = "SR 0.101 Art. 14"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)
