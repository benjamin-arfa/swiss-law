"""SR 120.52 Art. 4

Generated from: ch/120/de/120.52.md

Gewalttaetiges Verhalten: Definition of violent behavior at sports events.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gewalttaetiges_verhalten_sportveranstaltung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person gewalttaetiges Verhalten anlaesslich einer Sportveranstaltung gezeigt hat"
    reference = "SR 120.52 Art. 4 Abs. 1"


class mitfuehren_waffen_sprengmittel_pyrotechnik(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Waffen, Sprengmittel oder pyrotechnische Gegenstaende in Sportstaetten mitgefuehrt werden"
    reference = "SR 120.52 Art. 4 Abs. 2"


class gewalttaetiges_verhalten_gesamt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob gewalttaetiges Verhalten im Sinne von Art. 4 vorliegt"
    reference = "SR 120.52 Art. 4"

    def formula(person, period, parameters):
        return (
            person('gewalttaetiges_verhalten_sportveranstaltung', period) +
            person('mitfuehren_waffen_sprengmittel_pyrotechnik', period)
        ) > 0
