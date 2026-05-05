"""SR 142.281.3 Art. 4

Generated from: ch/142/de/142.281.3.md

Zuschlag fuer Umgebungsarbeiten bei Neubauten: 9.0 Prozent der anerkannten
Kosten nach Gruppen 1-3 und 5 des Baukostenplans Hochbau.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class zuschlag_umgebungsarbeiten_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Zuschlag fuer Umgebungsarbeiten bei Neubauten (Prozent)"
    reference = "SR 142.281.3 Art. 4"
    default_value = 9.0
