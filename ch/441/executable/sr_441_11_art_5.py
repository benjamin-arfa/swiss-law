"""SR 441.11 Art. 5

Generated from: ch/441/de/441.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class voelkerrechtlicher_vertrag_in_englisch_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Völkerrechtlicher Vertrag darf in Englisch abgeschlossen werden"
    reference = "SR 441.11, Art. 5 Abs. 1"

    def formula(self, period, parameters):
        dringlichkeit = self.person('besondere_dringlichkeit_vertrag', period)
        form_erfordert = self.person('spezifische_form_erfordert_englisch', period)
        uebliche_praxis = self.person('uebliche_praxis_internationale_beziehungen', period)
        return dringlichkeit + form_erfordert + uebliche_praxis


class besondere_dringlichkeit_vertrag(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Besondere Dringlichkeit liegt vor (Art. 5 Abs. 1 lit. a SpV)"
    reference = "SR 441.11, Art. 5 Abs. 1 lit. a"


class spezifische_form_erfordert_englisch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Spezifische Form des Abkommens erfordert Englisch (Art. 5 Abs. 1 lit. b SpV)"
    reference = "SR 441.11, Art. 5 Abs. 1 lit. b"


class uebliche_praxis_internationale_beziehungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Entspricht üblicher Praxis der internationalen Beziehungen (Art. 5 Abs. 1 lit. c SpV)"
    reference = "SR 441.11, Art. 5 Abs. 1 lit. c"
