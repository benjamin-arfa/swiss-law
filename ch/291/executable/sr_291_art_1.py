"""SR 291 Art. 1

Generated from: ch/291/de/291.md

Geltungsbereich: Dieses Gesetz regelt im internationalen Verhaeltnis die
Zustaendigkeit, das anzuwendende Recht, die Anerkennung und Vollstreckung
auslaendischer Entscheidungen, den Konkurs und die Schiedsgerichtsbarkeit.
Voelkerrechtliche Vertraege sind vorbehalten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class iprg_ist_anwendbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das IPRG im internationalen Verhaeltnis anwendbar ist"
    reference = "SR 291 Art. 1"

    def formula(person, period, parameters):
        hat_internationalen_bezug = person('hat_internationalen_bezug', period)
        kein_voelkerrechtlicher_vertrag = not_(
            person('voelkerrechtlicher_vertrag_anwendbar', period)
        )
        return hat_internationalen_bezug * kein_voelkerrechtlicher_vertrag


class hat_internationalen_bezug(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Sachverhalt einen internationalen Bezug aufweist"
    reference = "SR 291 Art. 1 Abs. 1"


class voelkerrechtlicher_vertrag_anwendbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein voelkerrechtlicher Vertrag vorrangig anwendbar ist"
    reference = "SR 291 Art. 1 Abs. 2"
