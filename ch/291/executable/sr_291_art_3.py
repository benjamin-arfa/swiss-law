"""SR 291 Art. 3

Generated from: ch/291/de/291.md

Notzustaendigkeit: Sieht das IPRG keine Zustaendigkeit in der Schweiz vor
und ist ein Verfahren im Ausland nicht moeglich oder unzumutbar, so sind die
schweizerischen Gerichte oder Behoerden am Ort zustaendig, mit dem der
Sachverhalt einen genuegenden Zusammenhang aufweist.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class keine_iprg_zustaendigkeit_in_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das IPRG keine Zustaendigkeit in der Schweiz vorsieht"
    reference = "SR 291 Art. 3"


class verfahren_im_ausland_unmoeglich_oder_unzumutbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Verfahren im Ausland nicht moeglich oder unzumutbar ist"
    reference = "SR 291 Art. 3"


class genuegender_zusammenhang_mit_schweizer_ort(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Sachverhalt genuegenden Zusammenhang mit einem Schweizer Ort aufweist"
    reference = "SR 291 Art. 3"


class notzustaendigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Notzustaendigkeit schweizerischer Gerichte gegeben ist"
    reference = "SR 291 Art. 3"

    def formula(person, period, parameters):
        keine_zustaendigkeit = person('keine_iprg_zustaendigkeit_in_schweiz', period)
        ausland_unmoeglich = person(
            'verfahren_im_ausland_unmoeglich_oder_unzumutbar', period
        )
        zusammenhang = person('genuegender_zusammenhang_mit_schweizer_ort', period)
        return keine_zustaendigkeit * ausland_unmoeglich * zusammenhang
