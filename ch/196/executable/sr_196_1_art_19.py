"""SR 196.1 Art. 19

Generated from: ch/196/de/196.1.md

Verfahrenskosten: Pauschalbetrag von hoechstens 2,5 Prozent der eingezogenen
Vermoegenswerte zur Deckung der Kosten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class eingezogene_vermoegenswerte_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Betrag der eingezogenen Vermoegenswerte in CHF"
    reference = "SR 196.1 Art. 19 Abs. 1"


class verfahrenskosten_pauschalbetrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximaler Pauschalbetrag fuer Verfahrenskosten (max 2.5% der eingezogenen Vermoegenswerte)"
    reference = "SR 196.1 Art. 19 Abs. 1"

    def formula(person, period, parameters):
        betrag = person('eingezogene_vermoegenswerte_betrag', period)
        return betrag * 0.025
