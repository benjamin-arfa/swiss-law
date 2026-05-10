"""SR 141.0 Art. 3 - Findelkind

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class in_schweiz_gefundenes_kind(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Kind wurde in der Schweiz gefunden"
    reference = "SR 141.0 Art. 3 Abs. 1"


class abstammung_unbekannt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Abstammung des Kindes ist unbekannt"
    reference = "SR 141.0 Art. 3 Abs. 1"


class abstammung_festgestellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Abstammung des Kindes wurde festgestellt"
    reference = "SR 141.0 Art. 3 Abs. 3"


class wuerde_staatenlos_werden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person wuerde durch den Verlust staatenlos werden"
    reference = "SR 141.0 Art. 3 Abs. 3"


class findelkind_erhaelt_schweizer_buergerrecht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Findelkind erhaelt das Schweizer Buergerrecht"
    reference = "SR 141.0 Art. 3 Abs. 1"

    def formula(self, period, parameters):
        gefunden = self('in_schweiz_gefundenes_kind', period)
        minderjaehrig = self('person_ist_minderjaehrig', period)
        unbekannt = self('abstammung_unbekannt', period)
        return gefunden * minderjaehrig * unbekannt


class findelkind_buergerrecht_erloschen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das durch Auffindung erworbene Buergerrecht erlischt"
    reference = "SR 141.0 Art. 3 Abs. 3"

    def formula(self, period, parameters):
        festgestellt = self('abstammung_festgestellt', period)
        minderjaehrig = self('person_ist_minderjaehrig', period)
        nicht_staatenlos = not_(self('wuerde_staatenlos_werden', period))
        return festgestellt * minderjaehrig * nicht_staatenlos
