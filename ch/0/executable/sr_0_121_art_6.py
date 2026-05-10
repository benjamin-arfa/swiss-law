"""SR 0.121 Art. VI

Generated from: ch/0/de/0.121.md

The Treaty applies to the area south of 60 degrees South latitude,
including all ice shelves. Does not affect high seas rights under
international law.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class antarktis_gebiet_suedlich_60(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob sich die Taetigkeit im Gebiet suedlich von 60 Grad suedlicher Breite befindet"
    reference = "SR 0.121 Art. VI"


class antarktis_vertrag_anwendbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Antarktis-Vertrag raeumlich anwendbar ist"
    reference = "SR 0.121 Art. VI"

    def formula(person, period, parameters):
        return person('antarktis_gebiet_suedlich_60', period)
