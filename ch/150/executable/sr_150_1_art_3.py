"""SR 150.1 Art. 3

Generated from: ch/150/de/150.1.md

Definition Freiheitsentzug: Jede Form des Festhaltens oder der Inhaftierung
oder Unterbringung in einer Einrichtung, die die Person nicht nach Belieben
verlassen darf, auf Anordnung/Veranlassung oder im Einverstaendnis einer Behoerde.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_festgehalten_oder_inhaftiert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person festgehalten, inhaftiert oder in einer Einrichtung untergebracht ist"
    reference = "SR 150.1 Art. 3"


class darf_einrichtung_nicht_verlassen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person die Einrichtung nicht nach Belieben verlassen darf"
    reference = "SR 150.1 Art. 3"


class auf_anordnung_behoerde(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Freiheitsentzug auf Anordnung, Veranlassung oder im Einverstaendnis einer Behoerde geschieht"
    reference = "SR 150.1 Art. 3"


class liegt_freiheitsentzug_vor(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Freiheitsentzug im Sinne des Gesetzes vorliegt"
    reference = "SR 150.1 Art. 3"

    def formula(person, period, parameters):
        return (
            person('ist_festgehalten_oder_inhaftiert', period)
            * person('darf_einrichtung_nicht_verlassen', period)
            * person('auf_anordnung_behoerde', period)
        )
