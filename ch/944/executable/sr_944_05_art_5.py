"""SR 944.05 Art. 5

Generated from: ch/944/de/944.05.md

Verteilung der Finanzhilfen: Distribution when budget is insufficient.
Consumer orgs (Art. 1) receive at least 90% of funds (25% equally, 75%
proportional to costs). Other orgs receive at most 10%.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class konsorg_budget_reicht_nicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die bewilligten Mittel nicht ausreichen fuer 50% der anrechenbaren Kosten"
    reference = "SR 944.05 Art. 5 Abs. 1"
    default_value = False


class konsorg_anteil_art1_mindestens(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Mindestanteil der Gesamtsumme fuer Konsumentenorganisationen nach Art. 1"
    reference = "SR 944.05 Art. 5 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        return 0.90


class konsorg_anteil_andere_hoechstens(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hoechstanteil der Gesamtsumme fuer andere Organisationen nach Art. 2"
    reference = "SR 944.05 Art. 5 Abs. 1 Bst. b"

    def formula(person, period, parameters):
        return 0.10
