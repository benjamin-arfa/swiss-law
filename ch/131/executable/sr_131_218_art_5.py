"""SR 131.218 § 5

Generated from: ch/131/de/131.218.md

Equality before the law: All citizens are equal before the law.
The canton promotes the realization of actual equality between men and women.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class zuger_buerger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person ein Bürger oder eine Bürgerin des Kantons Zug ist"
    reference = "SR 131.218 § 5 Abs. 1"


class geschlecht(Variable):
    value_type = Enum
    possible_values = ['mann', 'frau', 'divers']
    default_value = 'divers'
    entity_key = 'person'
    definition_period = YEAR
    label = "Das Geschlecht der Person"
    reference = "SR 131.218 § 5"


class gleichstellung_vor_gesetz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob alle Bürger vor dem Gesetz gleich sind"
    reference = "SR 131.218 § 5 Abs. 1"

    def formula(person, period, parameters):
        return person('zuger_buerger', period)


class gleichstellung_mann_frau_gefoerdert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Kanton die tatsächliche Gleichstellung von Mann und Frau fördert"
    reference = "SR 131.218 § 5 Abs. 2"

    def formula(person, period, parameters):
        geschlecht = person('geschlecht', period)
        buerger = person('zuger_buerger', period)
        return buerger * ((geschlecht == 'mann') | (geschlecht == 'frau'))


class anspruch_auf_gleichbehandlung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Anspruch auf Gleichbehandlung vor dem Gesetz hat"
    reference = "SR 131.218 § 5"

    def formula(person, period, parameters):
        return person('gleichstellung_vor_gesetz', period)