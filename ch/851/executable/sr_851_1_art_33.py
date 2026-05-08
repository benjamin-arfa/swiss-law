"""SR 851.1 Art. 33

Generated from: ch/851/de/851.1.md

Art. 33: Einsprache
- Abs. 1: Einsprachefrist von 30 Tagen.
- Abs. 2: Frist beginnt mit Empfang der Unterstützungsanzeige, der Abrechnung
  oder des Richtigstellungsbegehrens.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class zug_einsprachefrist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Einsprachefrist bei Nichtanerkennung des Anspruchs (Tage)"
    reference = "SR 851.1 Art. 33 Abs. 1"

    def formula(person, period, parameters):
        return parameters(period).zug.einsprachefrist_tage
