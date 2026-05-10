"""SR 446.2 Art. 19

Generated from: ch/446/de/446.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class keine_verbindliche_jugendschutzregelung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es besteht keine fuer verbindlich erklaerte Jugendschutzregelung"
    reference = "SR 446.2 Art. 19 Abs. 1 Bst. a"


class gesetz_in_kraft_seit_mindestens_2_jahren(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das JSFVG ist seit mindestens 2 Jahren in Kraft"
    reference = "SR 446.2 Art. 19 Abs. 1 Bst. a"


class bundesrat_kann_subsidiaer_regeln(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bundesrat kann subsidiaere Jugendschutzregelung erlassen"
    reference = "SR 446.2 Art. 19 Abs. 1"

    def formula(person, period, parameters):
        keine_regelung = person('keine_verbindliche_jugendschutzregelung', period)
        seit_2_jahren = person('gesetz_in_kraft_seit_mindestens_2_jahren', period)
        widerrufen = person('verbindlicherklaerung_widerrufen', period)
        hinfaellig = person('verbindlicherklaerung_hinfaellig', period)
        grund_a = keine_regelung * seit_2_jahren
        grund_b = widerrufen + hinfaellig >= 1
        return grund_a + grund_b >= 1
