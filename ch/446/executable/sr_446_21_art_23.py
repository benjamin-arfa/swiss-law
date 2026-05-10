"""SR 446.21 Art. 23

Generated from: ch/446/de/446.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anrechenbare_ausgaben_jsfvv(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anrechenbare Ausgaben: tatsaechlich entstandene und unbedingt erforderliche Kosten"
    reference = "SR 446.21 Art. 23 Abs. 3"


class finanzhilfe_hoechstbetrag_jsfvv(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hoechstbetrag der Finanzhilfe (max. 50% der anrechenbaren Ausgaben)"
    reference = "SR 446.21 Art. 23 Abs. 2"

    def formula(person, period, parameters):
        ausgaben = person('anrechenbare_ausgaben_jsfvv', period)
        return ausgaben * 0.50
