"""SR 141.0 Art. 4 - Adoption

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class minderjaehriges_auslaendisches_kind(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person ist ein minderjaehriges auslaendisches Kind"
    reference = "SR 141.0 Art. 4"


class adoptiert_von_schweizer_buerger(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Kind wird von einer Person mit Schweizer Buergerrecht adoptiert"
    reference = "SR 141.0 Art. 4"


class erwerb_buergerrecht_durch_adoption(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Kind erwirbt das Schweizer Buergerrecht durch Adoption"
    reference = "SR 141.0 Art. 4"

    def formula(self, period, parameters):
        minderjaehrig_auslaendisch = self('minderjaehriges_auslaendisches_kind', period)
        adoptiert = self('adoptiert_von_schweizer_buerger', period)
        return minderjaehrig_auslaendisch * adoptiert
