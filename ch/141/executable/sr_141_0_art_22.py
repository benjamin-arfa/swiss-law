"""SR 141.0 Art. 22 - Irrtuemlich angenommenes Schweizer Buergerrecht

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class guter_glaube_schweizer_buergerrecht_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Jahre im guten Glauben das Schweizer Buergerrecht zu besitzen"
    reference = "SR 141.0 Art. 22 Abs. 1"


class als_schweizer_behandelt_von_behoerden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person wurde von kantonalen oder Gemeindebehoerden als Schweizer behandelt"
    reference = "SR 141.0 Art. 22 Abs. 1"


class anspruch_erleichterte_einbuergerung_irrtum(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anspruch auf erleichterte Einbuergerung wegen irrtuemlich angenommenen Buergerrechts"
    reference = "SR 141.0 Art. 22"

    def formula(self, period, parameters):
        jahre = self('guter_glaube_schweizer_buergerrecht_jahre', period)
        behandelt = self('als_schweizer_behandelt_von_behoerden', period)
        return (jahre >= 5) * behandelt
