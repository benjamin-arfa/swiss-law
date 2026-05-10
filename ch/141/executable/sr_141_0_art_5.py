"""SR 141.0 Art. 5 - Verlust durch Aufhebung des Kindesverhaeltnisses

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kindesverhaeltnis_aufgehoben(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Kindesverhaeltnis zum vermittelnden Elternteil wurde aufgehoben"
    reference = "SR 141.0 Art. 5"


class verlust_buergerrecht_durch_aufhebung_kindesverhaeltnis(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Kind verliert das Schweizer Buergerrecht durch Aufhebung des Kindesverhaeltnisses"
    reference = "SR 141.0 Art. 5"

    def formula(self, period, parameters):
        aufgehoben = self('kindesverhaeltnis_aufgehoben', period)
        nicht_staatenlos = not_(self('wuerde_staatenlos_werden', period))
        return aufgehoben * nicht_staatenlos
