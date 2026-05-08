"""SR 851.1 Art. 28

Generated from: ch/851/de/851.1.md

Art. 28: Richtigstellung
- Abs. 1: Ein beteiligter Kanton kann Richtigstellung verlangen, wenn ein
  Unterstuetzungsfall offensichtlich unrichtig geregelt worden ist.
- Abs. 3: Der Anspruch auf Richtigstellung besteht nur fuer Unterstuetzungsleistungen,
  die in den letzten fuenf Jahren vor dem Begehren ausgerichtet worden sind.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class zug_richtigstellung_verjaehrung_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Verjaehrungsfrist fuer Richtigstellungsanspruch (Jahre)"
    reference = "SR 851.1 Art. 28 Abs. 3"

    def formula(person, period, parameters):
        return parameters(period).zug.richtigstellung_verjaehrung_jahre
