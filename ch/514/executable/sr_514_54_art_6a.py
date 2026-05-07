"""SR 514.54 Art. 6a

Generated from: ch/514/de/514.54.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class hat_verbotene_waffe_durch_erbgang_erworben(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person hat verbotene Waffe (Art. 5 Abs. 1) durch Erbgang erworben"


class erbgang_frist_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist zur Beantragung einer Ausnahmebewilligung nach Erbgang in Monaten (Art. 6a Abs. 1 SR 514.54)"
    reference = "SR 514.54 Art. 6a"

    def formula(person, period, parameters):
        # Innerhalb von sechs Monaten eine Ausnahmebewilligung beantragen
        return 6
