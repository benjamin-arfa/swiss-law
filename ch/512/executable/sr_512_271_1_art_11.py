"""SR 512.271.1 Art. 11 – Fortzahlung der Entschädigung bei vorübergehender Einstellung

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


class einstellung_wegen_krankheit_unfall_mutterschaft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vorübergehend eingestellt wegen Krankheit/Unfall (nicht flugbezogen) oder Mutterschaftsurlaub"
    reference = "SR 512.271.1 Art. 11 Abs. 1 lit. a"
    default_value = False


class einstellung_wegen_auslandaufenthalt_unter_6m(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vorübergehend eingestellt wegen Auslandaufenthalt < 6 Monate mit Wohnsitz Schweiz"
    reference = "SR 512.271.1 Art. 11 Abs. 1 lit. b"
    default_value = False


class fortzahlung_max_monate_art11(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Fortzahlung der Entschädigung in Monaten bei vorübergehender Einstellung (Art. 11)"
    reference = "SR 512.271.1 Art. 11 Abs. 1"

    def formula(person, period, parameters):
        grund_a = person('einstellung_wegen_krankheit_unfall_mutterschaft', period)
        grund_b = person('einstellung_wegen_auslandaufenthalt_unter_6m', period)

        # Höchstens 3 Monate pro Kalenderjahr
        return where(grund_a + grund_b, 3, 0)
