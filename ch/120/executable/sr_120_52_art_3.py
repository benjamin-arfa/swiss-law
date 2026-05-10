"""SR 120.52 Art. 3

Generated from: ch/120/de/120.52.md

Beschlagnahme und Einziehung von Propagandamaterial.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class propagandamaterial_sichergestellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Propagandamaterial sichergestellt wurde"
    reference = "SR 120.52 Art. 3 Abs. 1"


class aufruf_zur_gewalt_konkret_und_ernsthaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Aufruf zur Gewalt konkret und ernsthaft ist"
    reference = "SR 120.52 Art. 3 Abs. 3"


class propagandamaterial_einziehung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob fedpol das Propagandamaterial einzieht"
    reference = "SR 120.52 Art. 3 Abs. 3"

    def formula(person, period, parameters):
        return (
            person('propagandamaterial_sichergestellt', period) *
            person('aufruf_zur_gewalt_konkret_und_ernsthaft', period)
        )
