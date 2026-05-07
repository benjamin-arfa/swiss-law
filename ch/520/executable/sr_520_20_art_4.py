"""SR 520.20 Art. 4

Generated from: ch/520/de/520.20.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Art. 4: Legal effects of requisition. The requisition is a public-law
# restriction of ownership. Rights of disposal pass to the Confederation
# or the canton. Existing rights and obligations are suspended.


class requisition_ist_eigentumsbeschraenkung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Die Requisition ist eine oeffentlich-rechtliche Eigentumsbeschraenkung"
    reference = "SR 520.20 Art. 4 Abs. 1"

    def formula(person, period, parameters):
        return person('requisition_voraussetzungen_erfuellt', period)


class verfuegungsrecht_uebergegangen(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Das Verfuegungsrecht ist an den Bund oder Kanton uebergegangen"
    reference = "SR 520.20 Art. 4 Abs. 2"

    def formula(person, period, parameters):
        return person('requisition_voraussetzungen_erfuellt', period)


class rechte_pflichten_ruhen(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Oeffentlich-rechtliche und privatrechtliche Rechte und Pflichten ruhen waehrend der Requisition"
    reference = "SR 520.20 Art. 4 Abs. 3"

    def formula(person, period, parameters):
        return person('requisition_voraussetzungen_erfuellt', period)
