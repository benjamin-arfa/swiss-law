"""SR 366.1 Art. 16

Generated from: ch/366/de/366.1.md

Auskunfts-, Berichtigungs- und Loeschungsrecht: Gesuch beim Datenschutzberater.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class auskunftsgesuch_eingereicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person hat ein Auskunftsgesuch beim Datenschutzberater von fedpol eingereicht"
    reference = "SR 366.1 Art. 16 Abs. 1"


class strafverfolgungsinteresse_ueberwiegt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Interessen der Strafverfolgung/-vollstreckung oder polizeilichen Verbrechensverhuetung ueberwiegen"
    reference = "SR 366.1 Art. 16 Abs. 4"


class auskunft_zu_erteilen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Auskunft ueber betreffende Informationen ist zu erteilen"
    reference = "SR 366.1 Art. 16"

    def formula(person, period, parameters):
        gesuch = person('auskunftsgesuch_eingereicht', period)
        ueberwiegt = person('strafverfolgungsinteresse_ueberwiegt', period)
        return gesuch * not_(ueberwiegt)
