"""SR 837.0 Art. 13

Generated from: ch/837/de/837.0.md

Art. 13: Beitragszeit (Contribution period)
- Abs. 1: The contribution period is fulfilled if the person has been in
  contribution-liable employment for at least 12 months within the framework
  period (Art. 9 Abs. 3).
- Abs. 2: Also counted:
  a. periods of employment before AHV contribution age
  b. Swiss military, civil, or protection service
  c. periods in employment but not working due to illness/accident
  d. maternity-related work interruptions as required by law or collective
     agreement
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alv_beitragszeit_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Monate beitragspflichtiger Beschaeftigung innerhalb der Rahmenfrist"
    reference = "SR 837.0 Art. 13 Abs. 1"


class alv_beitragszeit_erfuellt_art_13(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Beitragszeit nach Art. 13 AVIG erfuellt (mindestens 12 Monate)"
    reference = "SR 837.0 Art. 13 Abs. 1"

    def formula(person, period, parameters):
        monate = person('alv_beitragszeit_monate', period)
        mindest = parameters(period).alv.mindest_beitragszeit_monate
        return monate >= mindest
