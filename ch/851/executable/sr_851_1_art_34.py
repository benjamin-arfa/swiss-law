"""SR 851.1 Art. 34

Generated from: ch/851/de/851.1.md

Art. 34: Beschluss und Beschwerde
- Abs. 2: Beschwerdefrist von 30 Tagen nach Empfang des Abweisungsbeschlusses
  bei der zustaendigen richterlichen Behoerde.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class zug_beschwerdefrist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Beschwerdefrist nach Empfang des Abweisungsbeschlusses (Tage)"
    reference = "SR 851.1 Art. 34 Abs. 2"

    def formula(person, period, parameters):
        return parameters(period).zug.beschwerdefrist_tage
