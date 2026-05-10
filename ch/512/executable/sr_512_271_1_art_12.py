"""SR 512.271.1 Art. 12 – Entschädigung bei Unfall und Erkrankung infolge von Einsätzen

Generated from: ch/512/de/512.271.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class einstellung_wegen_militaerflug_unfall(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eingestellt wegen Unfall bei Militärflug/Fallschirmabsprung oder damit zusammenhängender Tätigkeit"
    reference = "SR 512.271.1 Art. 12 Abs. 1 lit. a"
    default_value = False


class einstellung_wegen_erkrankung_durch_fluege(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eingestellt wegen Erkrankung als Folge von Militärflügen oder Fallschirmabsprüngen"
    reference = "SR 512.271.1 Art. 12 Abs. 1 lit. b"
    default_value = False


class fortzahlung_max_jahre_art12(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Fortzahlung der Entschädigung in Jahren bei einsatzbedingtem Unfall/Erkrankung"
    reference = "SR 512.271.1 Art. 12 Abs. 1"

    def formula(person, period, parameters):
        grund_a = person('einstellung_wegen_militaerflug_unfall', period)
        grund_b = person('einstellung_wegen_erkrankung_durch_fluege', period)

        # Höchstens 3 Jahre, bezogen auf gesamte Dienstzeit (Abs. 3)
        return where(grund_a + grund_b, 3, 0)
