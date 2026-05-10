"""SR 141.0 Art. 23 - Staatenloses Kind

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class person_ist_staatenlos(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person ist staatenlos"
    reference = "SR 141.0 Art. 23 Abs. 1"


class aufenthalt_schweiz_jahre_art23(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Gesamtaufenthalt in der Schweiz in Jahren (fuer Art. 23)"
    reference = "SR 141.0 Art. 23 Abs. 1"


class aufenthalt_unmittelbar_vor_gesuch_art23(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Aufenthalt unmittelbar vor Gesuchstellung in Jahren (fuer Art. 23)"
    reference = "SR 141.0 Art. 23 Abs. 1"


class anspruch_erleichterte_einbuergerung_staatenloses_kind(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anspruch auf erleichterte Einbuergerung als staatenloses minderjaehriges Kind"
    reference = "SR 141.0 Art. 23"

    def formula(self, period, parameters):
        minderjaehrig = self('person_ist_minderjaehrig', period)
        staatenlos = self('person_ist_staatenlos', period)
        aufenthalt = self('aufenthalt_schweiz_jahre_art23', period)
        unmittelbar = self('aufenthalt_unmittelbar_vor_gesuch_art23', period)
        return minderjaehrig * staatenlos * (aufenthalt >= 5) * (unmittelbar >= 1)
