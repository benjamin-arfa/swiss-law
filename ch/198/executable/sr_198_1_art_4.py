"""SR 198.1 Art. 4

Generated from: ch/198/de/198.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_schweizerischer_staatsangehoeriger(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist schweizerischer Staatsangehöriger"
    reference = "SR 198.1 Art. 4 Abs. 1 Bst. a"


class hat_wohnsitz_oder_sitz_in_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat Wohnsitz oder Sitz in der Schweiz"
    reference = "SR 198.1 Art. 4 Abs. 1 Bst. b"


class taetigkeit_in_schweiz_organisiert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tätigkeit wird in der Schweiz organisiert"
    reference = "SR 198.1 Art. 4 Abs. 1 Bst. c"


class taetigkeit_von_schweiz_aus_geleitet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tätigkeit wird von der Schweiz aus geleitet"
    reference = "SR 198.1 Art. 4 Abs. 1 Bst. d"


class umweltvertraeglichkeitspruefung_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Umweltverträglichkeitsprüfung ist nach Art. 8 des Protokolls vorgeschrieben"
    reference = "SR 198.1 Art. 4 Abs. 1"


class bewilligung_antarktis_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bewilligung des EDA für Tätigkeiten in der Antarktis ist erforderlich"
    reference = "SR 198.1 Art. 4 Abs. 1"

    def formula(person, period, parameters):
        uvp = person('umweltvertraeglichkeitspruefung_erforderlich', period)
        ch_nat = person('ist_schweizerischer_staatsangehoeriger', period)
        ch_sitz = person('hat_wohnsitz_oder_sitz_in_schweiz', period)
        ch_org = person('taetigkeit_in_schweiz_organisiert', period)
        ch_leit = person('taetigkeit_von_schweiz_aus_geleitet', period)
        schweiz_bezug = ch_nat + ch_sitz + ch_org + ch_leit > 0
        return uvp * schweiz_bezug


class frist_bewilligungsgesuch_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Mindestfrist in Monaten für Einreichung des Bewilligungsgesuchs vor der geplanten Tätigkeit"
    reference = "SR 198.1 Art. 4 Abs. 2"

    def formula(person, period, parameters):
        return 5
