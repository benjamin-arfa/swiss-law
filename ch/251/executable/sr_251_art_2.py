"""SR 251 Art. 2

Generated from: ch/de/251.md

Scope: Applies to private and public law enterprises that participate
in cartels, exercise market power, or participate in mergers.
Applies to conduct with effects in Switzerland even if initiated abroad.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_unternehmen_kg(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Einheit als Unternehmen im Sinne des KG gilt"
    reference = "SR 251 Art. 2 Abs. 1bis"


class auswirkung_in_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob sich der Sachverhalt in der Schweiz auswirkt"
    reference = "SR 251 Art. 2 Abs. 2"


class kg_anwendbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das KG anwendbar ist"
    reference = "SR 251 Art. 2"

    def formula(person, period, parameters):
        return person('ist_unternehmen_kg', period) * person('auswirkung_in_schweiz', period)
