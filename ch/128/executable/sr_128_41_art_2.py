"""SR 128.41 Art. 2

Generated from: ch/128/de/128.41.md

Betroffene Betriebe: The operational security procedure is conducted for
enterprises based in Switzerland. International treaties govern foreign enterprises.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class betrieb_sitz_in_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Betrieb seinen Sitz in der Schweiz hat"
    reference = "SR 128.41 Art. 2 Abs. 1"


class betriebssicherheitsverfahren_anwendbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Betriebssicherheitsverfahren nach dieser Verordnung anwendbar ist"
    reference = "SR 128.41 Art. 2"

    def formula(person, period, parameters):
        return person('betrieb_sitz_in_schweiz', period)
