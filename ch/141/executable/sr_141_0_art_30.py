"""SR 141.0 Art. 30 - Einbezug der Kinder

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kind_lebt_mit_bewerber_zusammen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das minderjaehrige Kind lebt mit der Bewerberin oder dem Bewerber zusammen"
    reference = "SR 141.0 Art. 30"


class alter_kind(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Alter des Kindes in Jahren"
    reference = "SR 141.0 Art. 30"


class kind_wird_in_einbuergerung_einbezogen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Kind wird in die Einbuergerung einbezogen"
    reference = "SR 141.0 Art. 30"

    def formula(self, period, parameters):
        zusammen = self('kind_lebt_mit_bewerber_zusammen', period)
        minderjaehrig = self('person_ist_minderjaehrig', period)
        return zusammen * minderjaehrig
