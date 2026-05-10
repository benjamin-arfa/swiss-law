"""SR 231.11 Art. 20c

Generated from: ch/231/de/231.11.md

Aufbewahrung von Beweismitteln: Proben oder Muster werden 1 Jahr
aufbewahrt. Danach 30 Tage Frist zur Uebernahme oder Kostenuebernahme.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class aufbewahrungsfrist_proben_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Aufbewahrungsfrist fuer Proben oder Muster in Jahren (1 Jahr)"
    reference = "SR 231.11 Art. 20c Abs. 1"

    def formula(person, period, parameters):
        return 1


class uebernahme_frist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Frist zur Uebernahme oder Kostenuebernahme nach Aufforderung in Tagen (30 Tage)"
    reference = "SR 231.11 Art. 20c Abs. 1"

    def formula(person, period, parameters):
        return 30


class uebernahme_oder_kostenuebernahme_erfolgt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Eigentuemer die Proben uebernimmt oder Kosten der Aufbewahrung traegt"
    reference = "SR 231.11 Art. 20c Abs. 1"


class proben_werden_vernichtet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Proben oder Muster vernichtet werden (keine Reaktion innert 30 Tagen)"
    reference = "SR 231.11 Art. 20c Abs. 1"

    def formula(person, period, parameters):
        return not_(person('uebernahme_oder_kostenuebernahme_erfolgt', period))
