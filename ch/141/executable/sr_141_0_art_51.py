"""SR 141.0 Art. 51 - Erwerb des Schweizer Buergerrechts gemaess Uebergangsrecht

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kind_aus_ehe_schweizerin_mit_auslaender(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das auslaendische Kind stammt aus der Ehe einer Schweizerin mit einem Auslaender"
    reference = "SR 141.0 Art. 51 Abs. 1"


class mutter_hatte_ch_buergerrecht_bei_geburt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Mutter besass das Schweizer Buergerrecht vor oder bei der Geburt des Kindes"
    reference = "SR 141.0 Art. 51 Abs. 1"


class geboren_vor_2006(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person wurde vor dem 1. Januar 2006 geboren"
    reference = "SR 141.0 Art. 51 Abs. 2"


class anspruch_erleichterte_einbuergerung_uebergangsrecht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anspruch auf erleichterte Einbuergerung gemaess Uebergangsrecht"
    reference = "SR 141.0 Art. 51"

    def formula(self, period, parameters):
        eng_verbunden = self('mit_schweiz_eng_verbunden', period)

        # Abs. 1: Kind einer Schweizerin mit Auslaender
        abs1 = self('kind_aus_ehe_schweizerin_mit_auslaender', period) * self('mutter_hatte_ch_buergerrecht_bei_geburt', period) * eng_verbunden

        # Abs. 2: Vor 2006 geborenes Kind eines schweizerischen Vaters
        abs2 = self('geboren_vor_2006', period) * self('vater_schweizer_buerger', period) * eng_verbunden

        return abs1 + abs2 > 0
