"""SR 141.0 Art. 14 - Kantonaler Einbuergerungsentscheid

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class einbuergerungsbewilligung_bund_erteilt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Einbuergerungsbewilligung des Bundes wurde erteilt"
    reference = "SR 141.0 Art. 14 Abs. 1"


class monate_seit_erteilung_bewilligung(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Anzahl Monate seit Erteilung der Einbuergerungsbewilligung des Bundes"
    reference = "SR 141.0 Art. 14 Abs. 1"


class einbuergerungsbewilligung_gueltig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Die Einbuergerungsbewilligung des Bundes ist noch gueltig (innerhalb eines Jahres)"
    reference = "SR 141.0 Art. 14 Abs. 1"

    def formula(self, period, parameters):
        erteilt = self('einbuergerungsbewilligung_bund_erteilt', period.this_year)
        monate = self('monate_seit_erteilung_bewilligung', period)
        return erteilt * (monate <= 12)
