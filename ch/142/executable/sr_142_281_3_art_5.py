"""SR 142.281.3 Art. 5

Generated from: ch/142/de/142.281.3.md

Zuschlag fuer Ausstattungskosten bei Neubauten: 5.7 Prozent der anerkannten
Kosten nach Gruppen 1-3 und 5 des Baukostenplans Hochbau.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class zuschlag_ausstattungskosten_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Zuschlag fuer Ausstattungskosten bei Neubauten (Prozent)"
    reference = "SR 142.281.3 Art. 5"
    default_value = 5.7
