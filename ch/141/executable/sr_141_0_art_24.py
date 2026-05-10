"""SR 141.0 Art. 24 - Kind eines eingebürgerten Elternteils

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class war_minderjaehrig_bei_einbuergerung_elternteil(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person war minderjaehrig zum Zeitpunkt der Einreichung des Einbuergerungsgesuchs eines Elternteils"
    reference = "SR 141.0 Art. 24 Abs. 1"


class nicht_in_einbuergerung_einbezogen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person wurde nicht in die Einbuergerung einbezogen"
    reference = "SR 141.0 Art. 24 Abs. 1"


class alter_unter_22(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person hat das 22. Altersjahr noch nicht vollendet"
    reference = "SR 141.0 Art. 24 Abs. 1"


class aufenthalt_schweiz_jahre_art24(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Gesamtaufenthalt in der Schweiz in Jahren (fuer Art. 24)"
    reference = "SR 141.0 Art. 24 Abs. 1"


class aufenthalt_unmittelbar_vor_gesuch_art24(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Aufenthalt unmittelbar vor Gesuchstellung in Jahren (fuer Art. 24)"
    reference = "SR 141.0 Art. 24 Abs. 1"


class anspruch_erleichterte_einbuergerung_kind_eingebuergert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anspruch auf erleichterte Einbuergerung als Kind eines eingebürgerten Elternteils"
    reference = "SR 141.0 Art. 24"

    def formula(self, period, parameters):
        minderjaehrig_damals = self('war_minderjaehrig_bei_einbuergerung_elternteil', period)
        nicht_einbezogen = self('nicht_in_einbuergerung_einbezogen', period)
        unter_22 = self('alter_unter_22', period)
        aufenthalt = self('aufenthalt_schweiz_jahre_art24', period)
        unmittelbar = self('aufenthalt_unmittelbar_vor_gesuch_art24', period)
        return minderjaehrig_damals * nicht_einbezogen * unter_22 * (aufenthalt >= 5) * (unmittelbar >= 3)
