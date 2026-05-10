"""SR 141.0 Art. 7 - Verlust bei Geburt im Ausland

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class im_ausland_geboren(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person wurde im Ausland geboren"
    reference = "SR 141.0 Art. 7 Abs. 1"


class schweizerischer_elternteil(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ein Elternteil ist schweizerisch"
    reference = "SR 141.0 Art. 7 Abs. 1"


class besitzt_andere_staatsangehoerigkeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person besitzt noch eine andere Staatsangehoerigkeit"
    reference = "SR 141.0 Art. 7 Abs. 1"


class alter(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Alter der Person in Jahren"
    reference = "SR 141.0 Art. 7 Abs. 1"


class bei_behoerde_gemeldet_oder_erklaerung_abgegeben(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person wurde bei einer schweizerischen Behoerde gemeldet oder hat erklaert das Buergerrecht beibehalten zu wollen"
    reference = "SR 141.0 Art. 7 Abs. 1"


class verwirkung_buergerrecht_auslandgeburt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Schweizer Buergerrecht verwirkt wegen Geburt im Ausland und fehlender Meldung bis 25"
    reference = "SR 141.0 Art. 7 Abs. 1"

    def formula(self, period, parameters):
        ausland = self('im_ausland_geboren', period)
        ch_elternteil = self('schweizerischer_elternteil', period)
        andere_staat = self('besitzt_andere_staatsangehoerigkeit', period)
        alter_person = self('alter', period)
        gemeldet = self('bei_behoerde_gemeldet_oder_erklaerung_abgegeben', period)

        # Verwirkung mit Vollendung des 25. Lebensjahres wenn nicht gemeldet
        alter_erreicht = alter_person >= 25
        return ausland * ch_elternteil * andere_staat * alter_erreicht * not_(gemeldet)
