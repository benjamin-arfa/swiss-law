"""SR 520.20 Art. 10

Generated from: ch/520/de/520.20.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class beschwerde_keine_aufschiebende_wirkung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Beschwerden gegen Verfuegungen des BABS im Zusammenhang mit der Requisition haben keine aufschiebende Wirkung"
    reference = "SR 520.20 Art. 10"

    def formula(person, period, parameters):
        # Always true by operation of law
        return person('requisition_voraussetzungen_erfuellt', period)
