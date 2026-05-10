"""SR 112 Art. 2

Generated from: ch/de/112.md

Financial contribution: Bern pays CHF 500,000 to the Confederation.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bundessitz_beitrag_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Summe die Bern an die Eidgenossenschaft zahlt (CHF)"
    reference = "SR 112 Art. 2"

    def formula(person, period, parameters):
        return 500000.0
