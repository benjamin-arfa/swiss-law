"""SR 141.0 Art. 21 - Ehefrau eines Schweizers oder Ehemann einer Schweizerin

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class auslaendische_staatsangehoerigkeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person besitzt eine auslaendische Staatsangehoerigkeit"
    reference = "SR 141.0 Art. 21 Abs. 1"


class verheiratet_mit_schweizer(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person ist mit einer Schweizerin oder einem Schweizer verheiratet"
    reference = "SR 141.0 Art. 21 Abs. 1"


class dauer_eheliche_gemeinschaft_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Dauer der ehelichen Gemeinschaft in Jahren"
    reference = "SR 141.0 Art. 21 Abs. 1 lit. a"


class aufenthalt_schweiz_jahre_art21(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Gesamtaufenthalt in der Schweiz in Jahren (fuer Art. 21)"
    reference = "SR 141.0 Art. 21 Abs. 1 lit. b"


class aufenthalt_unmittelbar_vor_gesuch_art21(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Aufenthalt unmittelbar vor Gesuchstellung in Jahren (fuer Art. 21)"
    reference = "SR 141.0 Art. 21 Abs. 1 lit. b"


class lebt_im_ausland(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person lebt im Ausland"
    reference = "SR 141.0 Art. 21 Abs. 2"


class mit_schweiz_eng_verbunden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person ist mit der Schweiz eng verbunden"
    reference = "SR 141.0 Art. 21 Abs. 2 lit. b"


# Computed variables

class anspruch_erleichterte_einbuergerung_ehegatte(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anspruch auf erleichterte Einbuergerung als Ehegatte eines Schweizers"
    reference = "SR 141.0 Art. 21"

    def formula(self, period, parameters):
        auslaendisch = self('auslaendische_staatsangehoerigkeit', period)
        verheiratet = self('verheiratet_mit_schweizer', period)
        ehe_dauer = self('dauer_eheliche_gemeinschaft_jahre', period)
        aufenthalt = self('aufenthalt_schweiz_jahre_art21', period)
        unmittelbar = self('aufenthalt_unmittelbar_vor_gesuch_art21', period)
        im_ausland = self('lebt_im_ausland', period)
        eng_verbunden = self('mit_schweiz_eng_verbunden', period)

        # Abs. 1: In der Schweiz lebend
        inland = auslaendisch * verheiratet * (ehe_dauer >= 3) * (aufenthalt >= 5) * (unmittelbar >= 1)

        # Abs. 2: Im Ausland lebend
        ausland = auslaendisch * verheiratet * im_ausland * (ehe_dauer >= 6) * eng_verbunden

        return inland + ausland > 0
